from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # Common fields for all users
    ROLES = (
        ('supplier', 'Supplier'),
        ('transporter', 'Transporter'),
        ('carrier', 'Carrier'),
        ('custom_clearance_agent', 'Custom Clearance Agent'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=100) 
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    contact_info = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    company_name = models.CharField(max_length=100)
    id_proof = models.FileField(upload_to='documents/id_proof', null=True, blank=True)  # for storing document images
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    is_verified = models.BooleanField(default=False)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    license_image = models.FileField(upload_to='documents/liscence', null=True, blank=True)

