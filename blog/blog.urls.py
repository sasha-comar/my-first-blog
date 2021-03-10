# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:37:34 2021

@author: admin
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]