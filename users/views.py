from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .serializers import Active_User_Serializer
from .serializers import MyTokenObtainPairSerializer
from .serializers import All_Active_User_Serializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.

@api_view(['post'])
@permission_classes([IsAuthenticated,])
def add_attendant(request):
    if(request.user.ismanager()):
        try:        
            user = request.data
            serializer = UserSerializer(data=user)
            serializer.is_valid(raise_exception=True)
            serializer.create_attendant(serializer.validated_data)
            res={"success":True}
            return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
            res={"success":False}
            return Response({**res, **serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        res={
            "success":False,
            "message":"Not authorized",
        }
        return Response(res, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['post'])
@permission_classes([IsAuthenticated,])
def add_manager(request):
    if(request.user.ismanager()):
        try:
            user = request.data
            serializer = UserSerializer(data=user)
            serializer.is_valid(raise_exception=True)
            serializer.create_manager(serializer.validated_data)
            res={"success":True}
            return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
        except:
            res={"success":False}
            return Response({**res, **serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        res={
            "success":False,
            "message":"Not authorized",
        }
        return Response(res, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def getUsers(request):
    if(request.user.ismanager()):
        try:
                user_data=User.objects.all() 
                serializer=All_Active_User_Serializer(user_data, many=True)
                for x in serializer.data:
                    if(x["is_manager"]):
                        x["role"]="Manager"
                        x.pop("is_manager")
                        x['name']=x['first_name']+" "+x['last_name']
                        x.pop("first_name")
                        x.pop("last_name")
                    else:
                        x["role"]="Attendant"
                        x.pop("is_manager")
                        x['name']=x['first_name']+" "+x['last_name']
                        x.pop("first_name")
                        x.pop("last_name")
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
                res={"success":false}
                return Response(res,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        res={
            "success":False,
            "message":"Not authorized",
        }
        return Response(res, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def getUser(request):
    try:
            user = request.user
            user_data=User.objects.get(user_name=user)  
            serializer=Active_User_Serializer(user_data, many=False)
            if(user.ismanager()):                
                res={"success":True,'Role':"Manager"}                
            else:
                res={"success":True,'Role':"Attendant"} 
            return Response({**res, **serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
            res={"success":False}
            return Response(res, status=status.HTTP_404_NOT_FOUND)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


    