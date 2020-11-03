from django.db import models
from django.utils import timezone
# Create your models here.
class Brands(models.Model):
    brand_name = models.CharField(max_length=30, unique=True)
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return self.brand_name
class Body_types(models.Model):
    bodyname = models.TextChoices('body_name', 'sport touring standard cruiser dual-purpose dirt_bike others')
    body_name=models.CharField(max_length=30, choices=bodyname.choices, default='others', unique=True)
    image = models.ImageField(upload_to='images/body_types/')
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return self.body_name
class Bike_models(models.Model):
    model_name = models.CharField(max_length=30, unique=True)
    brand_name=models.ForeignKey(Brands, on_delete=models.CASCADE)
    body_type=models.ForeignKey(Body_types, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/bike_models/')
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return '%d: %s' % (self.id, self.model_name)
class Parts_categories(models.Model):
    category_name = models.CharField(max_length=30,unique=True)
    image = models.ImageField(upload_to='images/part_categories/')
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return self.category_name
class Subcategories(models.Model):
    title=models.CharField(max_length=30, unique=True)    
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
class Product(models.Model):
    product_code = models.IntegerField(primary_key=True)
    manufacturer = models.CharField(max_length=30)
    product_name = models.CharField(max_length=30)
    parts_category=models.ForeignKey(Parts_categories, on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/products/')
    description=models.TextField()
    bike_model=models.ManyToManyField(Bike_models)
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return '%d: %s' % (self.product_code,self.product_name)
class Suppliers(models.Model):
    supplier_name=models.CharField(max_length=60, unique=True)
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return self.supplier_name
class Supplies(models.Model):
    supplier=models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    units = models.PositiveIntegerField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
    cost_per_unit=models.FloatField()
    price_per_unit=models.FloatField()
    def __str__(self):
        return self.supplier.supplier_name
class Store(models.Model):
    supply=models.OneToOneField(Supplies, on_delete=models.CASCADE, primary_key=True)
    remaining_units=models.PositiveIntegerField()
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
class Sales(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    selling_price_per_unit=models.FloatField()
    units=models.PositiveIntegerField()
    entry_date = models.DateTimeField(default=timezone.now, editable=False)
    supply=models.ForeignKey(Supplies,on_delete=models.CASCADE)
    profit=models.FloatField()