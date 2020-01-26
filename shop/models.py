from django.contrib.auth.models import User
from django.db import models
from piro12.utils import uuid_upload_to



# 거래처
class Account(models.Model):
    name = models.CharField(max_length=100, verbose_name='이름')
    phone = models.TextField(verbose_name='전화번호')
    address = models.TextField(verbose_name='주소')

    def __str__(self):
        return self.name

# 상품
class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='제품명')
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to, verbose_name ='제품 사진')
    desc = models.TextField(blank=True, verbose_name='제품 설명')
    price = models.PositiveIntegerField(verbose_name='가격')
    count = models.PositiveIntegerField(verbose_name='남은 수량')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='거래처', related_name='items')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
