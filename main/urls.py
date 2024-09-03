from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('plans/',views.get_payment_plan),
    path('plans/create',views.create_payment_plan),
    path('plan/<int:id>/',views.payment_details),
    path('plan/update/',views.update_payment_status),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]
