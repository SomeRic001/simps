from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .db_utils import execute_query

#INCOME VIEWS
@csrf_exempt
def add_income(request):
    if request.method=='POST':
        try:
            data=json.loads(request.body)

            user_id = data.get('user_id')
            month = data.get('month')
            year = data.get('year')
            amount = data.get('amount')
            source = data.get('source', '')

            query="""
                INSERT INTO income(user_id, month,year,amount,source)
                VALUES (%s, %s, %s, %s, %s)
            """
            params=(user_id,month,year,amount,source)

            income_id=execute_query(query,params, fetch=False)

            return JsonResponse({
                'status':'success',
                'message':'Income added successfully',
                'income_id': income_id  
            })
        except Exception as e:
            return JsonResponse({
                'status':'error',
                'message':str(e)
            },status=400)  #statuscode-> bad request
    return JsonResponse({'status':'error','message':'Invalid request method'},status=405) #stautscode->MethodNotAllowed
    
@csrf_exempt
def get_income(request):
    if request.method =='GET':
        try:
            user_id= request.GET.get('user_id')

            query="""
                SELECT * FROM income
                WHERE user_id = %s
                ORDER BY year DESC, month DESC
            """
            params= (user_id,)

            income_list= execute_query(query, params, fetch=True)

            return JsonResponse({
                'status':'success',
                'data':income_list
            })
        except Exception as e:
            return JsonResponse({
                'status':'error',
                'message':str(e)
            },status=400)
        
    return JsonResponse({'status':'error','message':'Invalid request method'}, status=405)


@csrf_exempt
def update_income(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            income_id = data.get('income_id')
            amount = data.get('amount')
            source = data.get('source')
            
            query = """
                UPDATE income 
                SET amount = %s, source = %s
                WHERE income_id = %s
            """
            params = (amount, source, income_id)
            
            execute_query(query, params, fetch=False)
            
            return JsonResponse({
                'status': 'success',
                'message': 'Income updated successfully'
            })
        
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
        
@csrf_exempt
def delete_income(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            income_id = data.get('income_id')
            
            query = "DELETE FROM income WHERE income_id = %s"
            params = (income_id,)
            
            execute_query(query, params, fetch=False)
            
            return JsonResponse({
                'status': 'success',
                'message': 'Income deleted successfully'
            })
        
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


#EXPENSES VIEW
@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            month = data.get('month')
            year = data.get('year')
            amount = data.get('amount')
            category = data.get('category', '')
            
            query = """
                INSERT INTO expenses (user_id, month, year, amount, category)
                VALUES (%s, %s, %s, %s, %s)
            """
            params = (user_id, month, year, amount, category)
            
            expense_id = execute_query(query, params, fetch=False)
            
            return JsonResponse({
                'status': 'success',
                'message': 'Expense added successfully',
                'expense_id': expense_id
            })
        
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def get_expenses(request):
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            
            query = """
                SELECT * FROM expenses 
                WHERE user_id = %s
                ORDER BY year DESC, month DESC
            """
            params = (user_id,)
            
            expenses_list = execute_query(query, params, fetch=True)
            
            return JsonResponse({
                'status': 'success',
                'data': expenses_list
            })
        
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def update_expense(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            expense_id = data.get('expense_id')
            amount = data.get('amount')
            category = data.get('category')
            
            query = """
                UPDATE expenses 
                SET amount = %s, category = %s
                WHERE expense_id = %s
            """
            params = (amount, category, expense_id)
            
            execute_query(query, params, fetch=False)
            
            return JsonResponse({
                'status': 'success',
                'message': 'Expense updated successfully'
            })
        
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def delete_expense(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            expense_id = data.get('expense_id')
            
            query = "DELETE FROM expenses WHERE expense_id = %s"
            params = (expense_id,)
            
            execute_query(query, params, fetch=False)
            
            return JsonResponse({
                'status': 'success',
                'message': 'Expense deleted successfully'
            })
        
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


#SAVINGS VIEW
@csrf_exempt
def calculate_savings(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            month = data.get('month')
            year = data.get('year')
            
            #Calculates the total income
            income_query = """
                SELECT SUM(amount) as total_income 
                FROM income 
                WHERE user_id = %s AND month = %s AND year = %s
            """
            income_result = execute_query(income_query, (user_id, month, year), fetch=True)
            total_income = income_result[0]['total_income'] or 0
            
            #Calculates the total expenses
            expense_query = """
                SELECT SUM(amount) as total_expenses 
                FROM expenses 
                WHERE user_id = %s AND month = %s AND year = %s
            """
            expense_result = execute_query(expense_query, (user_id, month, year), fetch=True)
            total_expenses = expense_result[0]['total_expenses'] or 0
            
            #Calculate savings
            savings_amount = total_income - total_expenses
            
            check_query = """
                SELECT savings_id FROM savings 
                WHERE user_id = %s AND month = %s AND year = %s
            """
            existing = execute_query(check_query, (user_id, month, year), fetch=True)
            
            if existing:
                update_query = """
                    UPDATE savings 
                    SET total_income = %s, total_expenses = %s, savings_amount = %s
                    WHERE user_id = %s AND month = %s AND year = %s
                """
                execute_query(update_query, (total_income, total_expenses, savings_amount, user_id, month, year), fetch=False)
            else:
                insert_query = """
                    INSERT INTO savings (user_id, month, year, total_income, total_expenses, savings_amount)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                execute_query(insert_query, (user_id, month, year, total_income, total_expenses, savings_amount), fetch=False)
            
            return JsonResponse({
                'status': 'success',
                'message': 'Savings calculated successfully',
                'data': {
                    'total_income': float(total_income),
                    'total_expenses': float(total_expenses),
                    'savings_amount': float(savings_amount)
                }
            })
        
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def get_savings(request):
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            
            query = """
                SELECT * FROM savings 
                WHERE user_id = %s
                ORDER BY year DESC, month DESC
            """
            params = (user_id,)
            
            savings_list = execute_query(query, params, fetch=True)
            
            return JsonResponse({
                'status': 'success',
                'data': savings_list
            })
        
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
            

def dashboard_home(request):
    user_id = request.session.get('user_id')
    if not user_id:
       return redirect("users:login")
    return render(request, 'dashboard/dashboard.html')


def add_income_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
       return redirect("users:login")
    return render(request, 'dashboard/add_income.html')


def add_expense_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
       return redirect("users:login")
    return render(request, 'dashboard/add_expense.html')

def view_income_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
       return redirect("users:login")
    return render(request, 'dashboard/view_income.html')

def view_expenses_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
       return redirect("users:login")
    return render(request, 'dashboard/view_expenses.html')

def view_savings_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
       return redirect("users:login")
    return render(request, 'dashboard/view_savings.html')