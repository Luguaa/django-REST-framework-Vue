# coding:utf-8
__author__ = 'Luguaa'
__date__ = '2020/4/21 15:30'

from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    """
    商品类别三级目录序列化
    """

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """
    商品类别二级目录序列化
    """
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品类别一级目录序列化
    """
    # sub_cat：models里的related_name
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"
