from django.shortcuts import render, redirect
from django.http import JsonResponse
from .utils import get_current_savings, get_next_equity, process_purchase


# explore page ko home
def explore_home(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("users:login")

    equity = get_next_equity(user_id)

    if not equity:
        return render(request, "exploration/explore.html", {"no_more": True})

    savings = get_current_savings(user_id)

    context = {
        "equity_id": equity[0],
        "symbol": equity[1],
        "name": equity[2],
        "price": equity[3],
        "sector": equity[4],
        "max_invest": savings,
        "default_value": 10 if savings >= 10 else savings
    }

    return render(request, "exploration/explore.html", context)


# if equity is to be bought
def buy_equity(request):
    if request.method != "POST":
        return redirect("explore:home")

    user_id = request.session.get("user_id")
    equity_id = request.POST.get("equity_id")
    amount = request.POST.get("amount")

    if not user_id or not equity_id or not amount:
        return JsonResponse({"error": "Invalid request parameters"}, status=400)

    result = process_purchase(user_id, equity_id, amount)

    if "error" in result:
        # alert if error
        return JsonResponse({"error": result["error"]}, status=400)

    # Return success JSON so the JS knows to refresh/redirect
    return JsonResponse({"status": "success", "message": "Purchase successful"})

# if user skips the current equity
def skip_equity(request):
    return redirect("explore:home")