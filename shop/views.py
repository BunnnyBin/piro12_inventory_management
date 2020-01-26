from django.shortcuts import render, redirect
from django.urls import reverse

from shop.forms import ItemForm
from shop.models import Item, Account


def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'shop/item_list.html', context)


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item
    }
    return render(request, 'shop/item_detail.html', context)


def item_new(request, item=None):
    # 등록 버튼 누를 때의 처리
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(reverse('item_detail', kwargs={'pk': item.pk}))
    # 사이트 들어간 것에 대한 처리(또는 수정)
    elif request.method == 'GET':
        form = ItemForm(instance=item)
    return render(request, 'shop/item_form.html', {
        'form': form,
    })


def item_edit(request, pk):
    item = Item.objects.get(pk=pk)
    return item_new(request, item)
