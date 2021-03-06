from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('create', create, name = 'create'),
    path('create', CreateStudent.as_view(), name = 'create_class'),

    path('view', view, name = 'view'),
    path('student-record/<pk>', ViewStudent.as_view(), name = 'view_class'),
    path('student-details/<pk>',  ReadStudent.as_view(), name = 'read'),

    path('update/<pk>', UpdateStudent.as_view(), name = 'update'),
    path('update-via-func/<pk>', update_func, name = 'update_func'),


    path('delete/<pk>',  DeleteStudent.as_view(), name = 'delete_class'),
    path('view/<pk>',delete_fnc, name = 'delete_fnc'),
]
