from rest_framework import serializers
from .models import User
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
        fields = ('id_number','user_name', 'email', 'first_name', 'middle_name', 'last_name')