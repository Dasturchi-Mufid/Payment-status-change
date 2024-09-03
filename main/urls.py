from django.urls import path
from . import views

urlpatterns = [
    path('plans/',views.get_payment_plan),
    path('plans/create',views.create_payment_plan),
    path('plan/<int:id>/',views.payment_details),
    path('plan/update/',views.update_payment_status),
    
]
