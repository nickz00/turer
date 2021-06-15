from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('client', views.client),
    path('client/add', views.client_add),
    path('client/delite/<str:c_id>', views.client_delite),
    path('one_client/<str:c_id>', views.one_client),
    path('one_client/change/<str:c_id>', views.one_client_change),

    path('interested', views.interested_),
    path('interested/add', views.interested_add),
    path('interested/delite/<str:i_id>', views.interested_delite),
    path('one_interested/<str:i_id>', views.one_interested),
    path('one_interested/change/<str:i_id>', views.one_interested_change),

    path('all_advertising',views.all_advertising),
    path('add_advertising',views.add_advertising)

]
