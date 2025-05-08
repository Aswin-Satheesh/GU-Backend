from rest_framework import generics
from .models import UserDetails
from .serializer import UserSerializer,UserFieldUpdateSerializer, ExpertFieldSerializer, ProfileEditSerializer
from .authentication import IsAuthenticated, generate_token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.conf import settings

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = UserDetails.objects.filter(Email_Address=email).first()
        
        if user and password==user.Password:
            token = generate_token(user)
            return Response({'token': token}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = generate_token(user)
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserListView(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [IsAuthenticated]


class ProfileView(APIView):
    authentication_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    

class Fieldofinterest(APIView):
    authentication_classes = [IsAuthenticated]

    def patch(self, request):

        user = request.user
        user_details = get_object_or_404(UserDetails, Email_Address=user.Email_Address)
        serializer = UserFieldUpdateSerializer(user_details, data=request.data, partial=True)
        
        if serializer.is_valid():
            # No need to manually convert, just save the list
            user_details.Field_of_Interest = request.data.get('Field_of_Interest', [])
            user_details.Requirements = request.data.get("Requirements","")

            user_details.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpertField(APIView):
    authentication_classes = [IsAuthenticated]

    def patch(self, request):

        user = request.user
        user_details = get_object_or_404(UserDetails, Email_Address=user.Email_Address)
        serializer = ExpertFieldSerializer(user_details, data=request.data, partial=True)
        
        if serializer.is_valid():
            user_details.Expertise = request.data.get('Expertise', [])
            user_details.Years_of_Experience = request.data.get('Years_of_Experience', '')
            user_details.organization_detail = request.data.get('organization_detail', '')

            user_details.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileUpdate(APIView):
    authentication_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        user_details = get_object_or_404(UserDetails, Email_Address=user.Email_Address)
        serializer = ProfileEditSerializer(user_details, data=request.data, partial=True)

        if serializer.is_valid():
            user_details.pincode = request.data.get('pincode', '')
            user_details.address = request.data.get('address', '')

            user_details.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MentorList(APIView):
    def get(self,request):
        user = request.user
        users = UserDetails.objects.filter(organization_detail__isnull=False)
        details = UserSerializer(users,many=True)
        return Response(details.data,status=status.HTTP_200_OK)

class Metrics(APIView):
    def get(self,request):
        count_stus = UserDetails.objects.all().count()
        count_ments = UserDetails.objects.filter(organization_detail__isnull=False).count()
        return Response({"students":count_stus, "ments":count_ments})