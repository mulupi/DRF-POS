from rest_framework import serializers
from . import models
from django.utils import timezone


class DateTimeFieldWihTZ(serializers.DateTimeField):
    '''Class to make output of a DateTime Field timezone aware
    '''
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)
#brands serializer       
class Brands_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Brands
        fields = '__all__'
    entry_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')
class Brands_Serializer_post(serializers.ModelSerializer): 
    class Meta(object):
        model = models.Brands
        fields = ['brand_name']

#bodytype
class Body_types_Serializer(serializers.ModelSerializer): 
    class Meta(object):
        model = models.Body_types
        exclude=['entry_date']
class Body_types_Serializer_get(serializers.ModelSerializer): 
    class Meta(object):
        model = models.Body_types
        fields = '__all__'
    entry_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')

#bike models
class Bike_models_Serializer(serializers.ModelSerializer):
    brand_name=serializers.StringRelatedField(many=False)
    body_type=serializers.StringRelatedField(many=False)
    entry_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')
    class Meta(object):
        model = models.Bike_models
        fields = '__all__'
class Bike_models_create_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Bike_models
        exclude=['entry_date']
#categories
class Parts_categories_Serializer_create(serializers.ModelSerializer):
    class Meta(object):
        model = models.Parts_categories
        exclude=['entry_date','image']
class Parts_categories_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Parts_categories
        fields = '__all__'
    entry_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')
#products
class Product_Serializer(serializers.ModelSerializer):
    #bike_model=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    parts_category=serializers.StringRelatedField(many=False)
    bike_model=serializers.StringRelatedField(many=True)
    class Meta(object):
        model = models.Product
        fields = '__all__'
    entry_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')
class Product_Create_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Product
        exclude=['entry_date']
#subcategories
class Subcategories_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Subcategories
        exclude=['entry_date']
class Subcategories_Serializer_Get(serializers.ModelSerializer):
    class Meta(object):
        model = models.Subcategories
        fields = '__all__'
    entry_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')

#suppliers
class Suppliers_Serializer_Get(serializers.ModelSerializer):
    class Meta(object):
        model = models.Suppliers
        fields = '__all__'
    entry_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')
class Suppliers_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Suppliers
        fields = ['supplier_name']
#supplies
class Supplies_Serializer(serializers.ModelSerializer):
    supplier=serializers.StringRelatedField(many=False)
    product=serializers.StringRelatedField(many=False)
    entry_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')
    class Meta(object):
        model = models.Supplies
        fields = '__all__'
class Supplies_create_Serializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Supplies
        exclude=['entry_date']
#store
class Store_Serializer(serializers.ModelSerializer):
    supplier_name=serializers.ReadOnlyField(source='supply.supplier.supplier_name')
    supplier_id=serializers.ReadOnlyField(source='supply.supplier.id')
    product_name=serializers.ReadOnlyField(source='supply.product.product_name')
    product_code=serializers.ReadOnlyField(source='supply.product.product_code')
    image=serializers.ImageField(source='supply.product.image')
    product_description=serializers.ReadOnlyField(source='supply.product.description')
    cost_per_unit=serializers.ReadOnlyField(source='supply.cost_per_unit')
    Price_per_unit=serializers.ReadOnlyField(source='supply.price_per_unit')
    class Meta(object):
        model = models.Store
        fields='__all__'