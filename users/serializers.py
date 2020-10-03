from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        user_data=User.objects.get(user_name=user)
        serializer=Active_User_Serializer(user_data, many=False)

        # Add custom claims
        token['image'] = serializer.data["file_upload"]
        if(user.ismanager()): 
            token['role']="Manager"
        else:
            token['role']="Attendant"
        # ...

        return token


class UserSerializer(serializers.ModelSerializer):
 
    date_joined = serializers.ReadOnlyField()
 
    class Meta(object):
        model = User
        fields = ('id_number','user_name', 'email', 'first_name', 'middle_name', 'last_name',
                  'date_joined', 'password', 'file_upload')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, v):
        user=User.objects.create_user(**v)
        return user
    def create_manager(self, v):
        user=User.objects.create_manager(**v)
        return user
    def create_attendant(self, v):
        user=User.objects.create_attandant(**v)
        return user
class Active_User_Serializer(serializers.ModelSerializer): 
    class Meta(object):
        model = User
        fields = ('id_number','user_name', 'email', 'first_name', 'middle_name', 'last_name','file_upload')
class DateTimeFieldWihTZ(serializers.DateTimeField):
    '''Class to make output of a DateTime Field timezone aware
    '''
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)
class All_Active_User_Serializer(serializers.ModelSerializer): 
    class Meta(object):
        model = User
        fields = ('id_number','first_name', 'last_name','date_joined','is_manager')
    date_joined = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')