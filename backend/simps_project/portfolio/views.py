from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection,IntegrityError
from django.contrib import auth
from decimal import Decimal, ROUND_HALF_UP


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
    total_p_l=total_invest=total_current=total_prcnt = 0
    for holding in holdings:
        hold = (
            {"id":holding[0],
             "quantity":holding[1],
             "purchase_price":round(holding[2],2),
             "date_added":holding[3],
             "symbol":holding[4],
             "name":holding[5],
             "type":holding[6],
             "current_price":round(holding[7],2),
             "profit_loss": holding[1]*(holding[7]-holding[2]),
             "percentage":round(((holding[7]-holding[2])*(100))/holding[2],2)}
        )
        total_p_l += round(hold['profit_loss'],2)
        total_invest += round(hold['quantity']*hold['purchase_price'],2)
        total_current+= round(hold['quantity']*hold['current_price'],2)
        total_prcnt = round( ((total_current - total_invest) * 100) / total_invest, 2)
        holding_list.append(hold)
    context = {
        'username': username,
        'holdings':holding_list,
        'total_p_l':total_p_l,
        'invest':total_invest,
        'current':total_current,
        'total_prcnt':total_prcnt
    }
    return render(request, "portfolio/overview.html",context)

      