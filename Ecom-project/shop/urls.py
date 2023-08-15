from django.urls import path

from shop import views
app_name='shop'

urlpatterns = [

    path('logout/', views.user_logout, name='logout'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodDetail, name='prodcatDetail'),
    path('<slug:c_slug>/', views.allProdCat, name='product_by_category'),
    path('',views.allProdCat,name='allProdCat'),
    path('login',views.login,name='login'),
    path('register', views.register, name='register'),

]