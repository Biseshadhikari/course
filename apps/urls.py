
from django.urls import path,include
from . import views
app_name = 'apps'
urlpatterns = [
   path("",views.home,name = 'home'),
   path('course/<str:slug>',views.course,name= 'course'),
   path('checkout/<str:slug>',views.checkout,name= 'checkout'),
]
