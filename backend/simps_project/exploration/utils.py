from django.db import connection, transaction
from decimal import Decimal
from datetime import datetime

def get_current_savings(user_id):
    now = datetime.now()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT savings_amount
            FROM Savings
            WHERE user_id = %s
            ORDER BY year DESC, month DESC
            LIMIT 1
        """, [user_id])

        result = cursor.fetchone()

    return Decimal(result[0]) if result else Decimal("0")

# get another equity from the global equity table
def get_next_equity(user_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT equity_id, symbol, equity_name, current_price, sector
            FROM Global_Equities
            WHERE equity_id NOT IN (
                SELECT equity_id
                FROM Personal_Portfolio
                WHERE user_id = %s
            )
            ORDER BY RAND()
            LIMIT 1
        """, [user_id])

        return cursor.fetchone()

# when user decides to purchase a stock, add it to their personal portfolio 
# and log into expenses and recalculate savings
# make this atomic transaction -> either executes or rolls back 
@transaction.atomic
def process_purchase(user_id, equity_id, amount):

    now = datetime.now()
    amount = Decimal(amount)

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT savings_id, savings_amount
            FROM Savings
            WHERE user_id = %s
            ORDER BY year DESC, month DESC
            LIMIT 1
            FOR UPDATE
        """, [user_id])

        savings_row = cursor.fetchone()

        if not savings_row:
            return {"error": "No savings record"}

        savings_id = savings_row[0]
        current_savings = Decimal(savings_row[1])

        # Validate
        if amount < 1 or amount > current_savings:
            return {"error": "Invalid amount"}

        # Get equity price
        cursor.execute("""
            SELECT current_price
            FROM Global_Equities
            WHERE equity_id = %s
        """, [equity_id])

        price_row = cursor.fetchone()

        if not price_row:
            return {"error": "Equity not found"}

        price = Decimal(price_row[0])
        quantity = amount / price

        # Lock portfolio row if exists
        cursor.execute("""
            SELECT portfolio_id
            FROM Personal_Portfolio
            WHERE user_id = %s AND equity_id = %s
            FOR UPDATE
        """, [user_id, equity_id])

        existing = cursor.fetchone()

        if existing:
            # Update quantity
            cursor.execute("""
                UPDATE Personal_Portfolio
                SET quantity = quantity + %s
                WHERE portfolio_id = %s
            """, [quantity, existing[0]])
        else:
            # Insert new portfolio
            cursor.execute("""
                INSERT INTO Personal_Portfolio
                (user_id, equity_id, quantity, purchase_price, date_added)
                VALUES (%s, %s, %s, %s, %s)
            """, [
                user_id,
                equity_id,
                quantity,
                price,
                now.date()
            ])

        # Insert expense
        cursor.execute("""
            INSERT INTO Expenses
            (user_id, month, year, amount, category)
            VALUES (%s, %s, %s, %s, %s)
        """, [
            user_id,
            now.month,
            now.year,
            amount,
            "Equity Purchase"
        ])

        # Update savings safely
        cursor.execute("""
            UPDATE Savings
            SET total_expenses = total_expenses + %s,
                savings_amount = savings_amount - %s
            WHERE savings_id = %s
        """, [amount, amount, savings_id])

    return {"success": True}