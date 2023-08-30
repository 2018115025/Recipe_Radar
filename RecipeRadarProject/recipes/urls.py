from django.urls import path
from .views import CreateUserView, CustomTokenObtainView, ManageUserView

app_name = 'recipes'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CustomTokenObtainView.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me'),
]
