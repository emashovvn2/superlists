from django.shortcuts import render
from django.http import HttpResponse

# Создайте здесь ваши представления.
def home_page(request):
    '''домашняя страница'''
    return HttpResponse('<html><title>To-Do lists</title></html>')