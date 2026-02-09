from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection,IntegrityError
from django.contrib import auth


# Create your views here.
def index(request):
    user_id = request.session.get('user_id')
    if not user_id:
       return redirect ("users:login")
    with connection.cursor() as cursor:
        cursor.execute("""SELECT p.portfolio_id,p.quantity,p.purchase_price,p.date_added,e.symbol, e.equity_name,e.type,e.current_price
            FROM personal_portfolio p
            JOIN global_equities e
            ON p.equity_id = e.equity_id
            WHERE p.user_id = %s""",
            [user_id])
        holdings = cursor.fetchall()
        cursor.execute("SELECT username from users where user_id = %s",[user_id])
        user_row = cursor.fetchone()
    username = user_row[0]
    holding_list = []
    
    for holding in holdings:
        hold = (
            {"id":holding[0],
             "quantity":holding[1],
             "purchase_price":holding[2],
             "date_added":holding[3],
             "symbol":holding[4],
             "name":holding[5],
             "type":holding[6],
             "current_price":holding[7],
             "profit_loss": holding[1]*(holding[7]-holding[2]),
             "percentage":round(((holding[7]-holding[2])*(100))/holding[2],2)}
        )
        hold["percentage_abs"] = abs(hold['percentage'])
        holding_list.append(hold)
    
    context = {
        'username': username,
        'holdings':holding_list
    }
    return render(request, "portfolio/overview.html",context)

      