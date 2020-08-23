from rest_framework import serializers
from . import models
class Brands_Serializer(serializers.ModelSerializer): 
    class Meta(object):
        model = models.Brands
        exclude=['entry_date']

class Body_types_Serializer(serializers.ModelSerializer): 
    class Meta(object):
        model = models.Body_types
        exclude=['entry_date']
class Bike_models_Serializer(serializers.ModelSerializer):
    brand_name=serializers.StringRelatedField(many=False)
    body_type=serializers.StringRelatedField(many=False)
    class Meta(object):
        model = models.Bike_models
        exclude=['entry_date']
class Bike_models_create_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Bike_models
        exclude=['entry_date']
class Parts_categories_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Parts_categories
        exclude=['entry_date']
class Product_Serializer(serializers.ModelSerializer):
    #bike_model=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    parts_category=serializers.StringRelatedField(many=False)
    bike_model=serializers.StringRelatedField(many=True)
    class Meta(object):
        model = models.Product
        exclude=['entry_date']
class Product_Create_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Product
        exclude=['entry_date']
class Subcategories_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Subcategories
        exclude=['entry_date']
class Suppliers_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Suppliers
        exclude=['entry_date']
class Supplies_Serializer(serializers.ModelSerializer):
    supplier=serializers.StringRelatedField(many=False)
    product=serializers.StringRelatedField(many=False)
    class Meta(object):
        model = models.Supplies
        exclude=['entry_date']
class Supplies_create_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Supplies
        exclude=['entry_date']
class Store_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Supplies
        exclude=['entry_date']