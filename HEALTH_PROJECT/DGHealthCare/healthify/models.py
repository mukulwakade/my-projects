from django.db import models


# Create your models here.

class AmbulanceModel(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_age = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=12)
    location = models.CharField(max_length=40)
    disease = models.CharField(max_length=100)

    def __str__(self):
        return self.patient_name

class AppointmentModel(models.Model):
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=60)
    #Have_You_Attended_To_The_Facility_Before = models.CharField(max_length=100)
    previous_visit = models.CharField(max_length=100)
    if_before_visited_visit_detail = models.CharField(max_length=100)
    appointment_date = models.DateField()
    slot  = models.CharField(max_length=60)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class DoctorModel(models.Model):
    name= models.CharField(max_length =50)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    qualification = models.CharField(max_length=50)
    adhaar_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class NursingStaffModel(models.Model):
    name= models.CharField(max_length =50)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    qualification = models.CharField(max_length=50)
    adhaar_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class RoomServiceStaffModel(models.Model):
    name= models.CharField(max_length =50)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    adhaar_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class CategoryModel(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class ProductModel(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,default=1)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to ='images/',default='')

    def __str__(self):
        return self.name



class OrderModel(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100,blank=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True)
    paid = models.BooleanField(default = False)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()