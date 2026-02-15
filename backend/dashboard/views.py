from django.shortcuts import render
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
    

    
        
        

            