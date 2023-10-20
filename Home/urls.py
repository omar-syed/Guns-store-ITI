
from django.urls import path
from . views import home,contact,about,detail,delete,search,add_gun,edit_gun,category_list,category_detail
from. api import gun_list_api,gun_detail_api,GunListApi,GunDetailApi

urlpatterns = [

    path('', home,name="home"),
    path('detail/<int:id>', detail,name="detail"),
    path('delete/<int:id>', delete,name="delete"),
    path('about', about,name="about"),
    path('contact', contact,name="contact"),
    path('search', search, name="search"),
    path('add_gun/', add_gun, name='add_gun'),
    path('edit_gun/<int:id>/', edit_gun, name='edit_gun'),
    path('category_list',category_list,name='category_list'),
    path('category/<str:category>/', category_detail, name='category_detail'),
    
    #api
    path('api/guns',gun_list_api,name='gun_list_api'),
    path('api/guns/<int:id>',gun_detail_api,name='gun_detail_api'),
    path('api/v2/guns',GunListApi.as_view(),name='gun_list_api2'),
    path('api/v2/guns/<int:id>',GunDetailApi.as_view(),name='gun_detail_api2'),

]
