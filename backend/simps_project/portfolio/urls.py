from django.urls import path
from . import views
app_name = 'portfolio'
urlpatterns =[path('',views.index, name = 'index'),
              path('delete/<int:portfolio_id>/',views.delete_holding,name = 'delete_holding'),
              path('edit/<int:portfolio_id>/',views.edit_holding, name = 'edit_holding')]