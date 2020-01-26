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
    # 등록 버튼 누르는 것에 대한 처리
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(reverse('item_detail', kwargs={'pk': item.pk}))
    # 사이트 보여주기 또는 수정하기
    else:
        form = ItemForm(instance=item)
    return render(request, 'shop/item_form.html', {
        'form': form,
    })


def item_edit(request, pk):
    item = Item.objects.get(pk=pk)
    return item_new(request, item)


def item_delete(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == 'GET':
        return redirect('item_detail', item.pk)
    elif request.method == 'POST':
        item.delete()
        return redirect('item_list')


def item_count(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['count'] == '-':
            item.count -= 1
        elif request.POST['count'] == '+':
            item.count += 1
        item.save()
    elif request.method == 'GET':
        return redirect('item_list')  #항상 list 화면이 나오게끔

    return redirect('item_list')


def account_list(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }
    return render(request, 'shop/account_list.html', context)


def account_detail(request, pk):
    account = Account.objects.get(pk=pk)
    context = {
        'account': account
    }
    return render(request, 'shop/account_detail.html', context)


def account_new(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']

        account = Account.objects.create(name=name, phone=phone, address=address)
        return redirect('account_detail', account.pk)
    elif request.method == 'GET':
        return render(request, 'shop/account_new.html')


def account_edit(request, pk):
    account = Account.objects.get(pk=pk)

    if request.method == 'POST':
        account.name = request.POST['name']
        account.phone = request.POST['phone']
        account.address = request.POST['address']

        account.save()
        return redirect('account_detail', account.pk)
    elif request.method == 'GET':
        context = {
            'account': account  # account_edit.html이라는 새로운 html로 이동하므로 변수 account가 다시 필요
        }
        return render(request, 'shop/account_edit.html', context)


def account_delete(request, pk):
    account = Account.objects.get(pk=pk)

    if request.method == 'GET':
        return redirect('account_detail', account.pk)
    elif request.method == 'POST':
        account.delete()
        return redirect('account_list')
