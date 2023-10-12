
from django.urls import path
from . views import home,contact,about,detail,delete,search,add_gun,edit_gun,category_list,category_detail

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
]
