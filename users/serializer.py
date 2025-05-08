from rest_framework import serializers
from .models import UserDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = [
    'First_Name',
    'Last_Name',
    'Email_Address',
    'Phone_Number',
    'Password',
    'pincode',
    'address',
    'DOB',
    'Gender',
    'Expertise',
    'Field_of_Interest', 
    'Requirements'
    ,'Years_of_Experience'
    ,'organization_detail'
]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    


class UserFieldUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['Field_of_Interest', 'Requirements']  # Only allow these fields
    
class ExpertFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['Expertise','Years_of_Experience','organization_detail']  # Only allow these fields

class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = [  'pincode',
                    'address']  # Only allow these fields