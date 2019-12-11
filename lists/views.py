from lists.models import Item
from django.shortcuts import render, redirect

def home_page(request):
        '''домашняя страница'''
        if request.method == 'POST':
                Item.objects.create(text=request.POST['item_text'])
                return redirect('/lists/one-ones-list-in-world/')
        items = Item.objects.all()
        return render(request, 'home.html')

def view_list(request):
        '''представление списка'''
        items = Item.objects.all()
        return render(request, 'list.html', {'items': items})
