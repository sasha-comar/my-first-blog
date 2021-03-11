# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:41:10 2021

@author: admin
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]