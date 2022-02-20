from django.db import models

# Create your models here.
from django.db import models
import datetime
# ----定义数据表


class Customer(models.Model):
    # ---CharField 对应 varchar 类型数据
    name = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class Medicine(models.Model):
    # 药品名
    name = models.CharField(max_length=200)
    # 药品编号
    sn = models.CharField(max_length=200)
    # 描述
    desc = models.CharField(max_length=200)


class Order(models.Model):
    # 订单名
    name = models.CharField(max_length=200, null=True, blank=True)
    # 创建日期
    create_date = models.DateTimeField(default=datetime.datetime.now)
    # 客户
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    # 订单购买的药品，和Medicine表是多对多 的关系
    medicines = models.ManyToManyField(Medicine, through='OrderMedicine')

    # 为了提高效率，这里存放 订单 medicines 冗余数据
    medicinelist = models.CharField(max_length=2000, null=True, blank=True)


class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)

    # 订单中药品的数量
    amount = models.PositiveIntegerField()