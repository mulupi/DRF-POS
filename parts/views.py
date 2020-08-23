from django.shortcuts import render
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status
from . import models
# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def Brand(request):
    if request.method == 'POST':
        try:
                brand = request.data
                serializer = serializers.Brands_Serializer(data=brand)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                res={"success":True}
                return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
                res={"success":False}
                return Response({**res, **serializer.errors})

    if request.method == 'GET':
        brands=models.Brands.objects.all()
        serializer=serializers.Brands_Serializer(brands, many=True)
        res={"success":True}
        return Response({**res, "data":serializer.data}, status=status.HTTP_201_CREATED)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def Body_type(request):
    if request.method == 'POST':
        try:
                body = request.data
                serializer = serializers.Body_types_Serializer(data=body)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                res={"success":True}
                return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
                res={"success":False}
                return Response({**res, **serializer.errors})

    if request.method == 'GET':
        body=models.Body_types.objects.all()
        serializer=serializers.Body_types_Serializer(body, many=True)
        res={"success":True}
        return Response({**res, "data":serializer.data}, status=status.HTTP_201_CREATED)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def Bike_models(request):
    if request.method == 'POST':
        try:
                bikemodel = request.data
                serializer = serializers.Bike_models_create_Serializer(data=bikemodel)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                res={"success":True}
                return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
                res={"success":False}
                return Response({**res, **serializer.errors})

    if request.method == 'GET':
        bikemodels=models.Bike_models.objects.all()
        serializer=serializers.Bike_models_Serializer(bikemodels, many=True)
        res={"success":True}
        return Response({**res, "data":serializer.data}, status=status.HTTP_201_CREATED)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def Parts_cat(request):
    if request.method == 'POST':
        try:
                partscat = request.data
                serializer = serializers.Parts_categories_Serializer(data=partscat)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                res={"success":True}
                return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
                res={"success":False}
                return Response({**res, **serializer.errors})

    if request.method == 'GET':
        partscat=models.Parts_categories.objects.all()
        serializer=serializers.Parts_categories_Serializer(partscat, many=True)
        res={"success":True}
        return Response({**res, "data":serializer.data}, status=status.HTTP_201_CREATED)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def Products(request):
    if request.method == 'POST':
        try:
                #print(request.user.ismanager())
                product = request.data
                serializer = serializers.Product_Create_Serializer(data=product)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                res={"success":True}
                return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
                res={"success":False}
                return Response({**res, **serializer.errors})

    if request.method == 'GET':
        product=models.Product.objects.all()
        serializer=serializers.Product_Serializer(product, many=True)
        res={"success":True}
        return Response({**res, "data":serializer.data}, status=status.HTTP_201_CREATED)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def Subcategory(request):
    if request.method == 'POST':
        try:
                #print(request.user.ismanager())
                subcat = request.data
                serializer = serializers.Subcategories_Serializer(data=subcat)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                res={"success":True}
                return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
                res={"success":False}
                return Response({**res, **serializer.errors})

    if request.method == 'GET':
        subcat=models.Subcategories.objects.all()
        serializer=serializers.Subcategories_Serializer(subcat, many=True)
        res={"success":True}
        return Response({**res, "data":serializer.data}, status=status.HTTP_201_CREATED)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def Suppliers(request):
    if request.method == 'POST':
        try:
                #print(request.user.ismanager())
                suppliers = request.data
                serializer = serializers.Suppliers_Serializer(data=suppliers)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                res={"success":True}
                return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
                res={"success":False}
                return Response({**res, **serializer.errors})

    if request.method == 'GET':
        suppliers=models.Suppliers.objects.all()
        serializer=serializers.Suppliers_Serializer(suppliers, many=True)
        res={"success":True}
        return Response({**res, "data":serializer.data}, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated,])
def Supplies(request):
    if request.method == 'PUT':
        try:
                #print(request.user.ismanager())
                supplies = request.data
                serializer = serializers.Supplies_create_Serializer(data=supplies)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                sup_id=serializer.data["id"]
                rem_units=serializer.data["units"]                
                models.Store(supply=models.Supplies.objects.get(id=sup_id),remaining_units=rem_units).save()
                res={"success":True}
                return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
                res={"success":False}
                return Response({**res, **serializer.errors})

    if request.method == 'GET':
        supplies=models.Supplies.objects.all()
        serializer=serializers.Supplies_Serializer(supplies, many=True)
        res={"success":True}
        return Response({**res, "data":serializer.data}, status=status.HTTP_201_CREATED)