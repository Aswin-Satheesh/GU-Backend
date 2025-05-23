import json
# Create your models here.
from django.db import models
from django.utils import timezone

class UserDetails(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email_Address = models.EmailField(unique=True)
    Phone_Number = models.CharField(max_length=15)
    Gender = models.CharField(max_length=50)
    DOB = models.DateTimeField(null=True, blank=True)
    Password = models.CharField(max_length=128)

    #o
    pincode = models.CharField(max_length=10,null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    #2
    Expertise = models.JSONField(null=True,blank=True)
    Years_of_Experience = models.IntegerField(default=0,null=True,blank=True)
    organization_detail = models.CharField(max_length=200,null=True,blank=True)
    Field_of_Interest = models.JSONField(null=True,blank=True)
    Requirements = models.TextField(null=True,blank=True)
    
    Proof = models.CharField(max_length=100,null=True,blank=True)
    
    #1
    User_ID = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True,auto_now=True)
    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.User_ID} {self.First_Name}"
    

class Educational_levels(models.Model):
    Institution_name = models.CharField(max_length=255)
    Education_level = models.CharField(max_length=100)
    Type_Description = models.TextField(blank=True, null=True)
    Created_At = models.DateTimeField(auto_now_add=True)
    User_ID = models.ForeignKey(UserDetails, to_field='User_ID', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.Institution_name} - {self.Education_level}"

class Booking(models.Model):
    Booking_ID = models.AutoField(primary_key=True)
    Mentor = models.ForeignKey(UserDetails, to_field='User_ID', on_delete=models.CASCADE, related_name='mentor_bookings')
    Mentee = models.ForeignKey(UserDetails, to_field='User_ID', on_delete=models.CASCADE, related_name='mentee_bookings')
    Description = models.TextField(blank=True, null=True)
    Details = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Booking {self.Booking_ID}"