from .models import AppointmentModel,AmbulanceModel,DoctorModel,NursingStaffModel,RoomServiceStaffModel,CategoryModel,ProductModel,OrderModel
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
class AmbulanceForm(forms.Form):
    patient_name = forms.CharField(max_length=50)
    patient_age = forms.CharField(max_length=50)
    gender = forms.ChoiceField(choices=(('Male',"Male"),('Female',"Female"),('Others',"Others") ),widget=forms.RadioSelect,initial='Male',)
    contact_number = forms.CharField(max_length=12)
    location = forms.CharField(max_length=40)
    disease = forms.CharField(max_length=100)

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=60)
    gender = forms.ChoiceField(choices=(('Male',"Male"),('Female',"Female"),('Others',"Others") ),widget=forms.RadioSelect,initial='Male',)
    city = forms.CharField(max_length=60)
    Have_You_Attended_To_The_Facility_Before = forms.ChoiceField(choices=(('Yes', "Yes"), ('No', "No"),),widget=forms.RadioSelect,initial='option_one', )
    if_Yes_State_What_Condition_And_When = forms.CharField(max_length=100)
    appointment_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    Please_Select_Slot = forms.ChoiceField(choices=(('Afternoon', "Afternoon"), ('Morning', "Morning"),),widget=forms.RadioSelect, )
    contact_number = forms.CharField(max_length=20)

class DoctorForm(forms.Form):
    name= forms.CharField(max_length =50)
    gender = forms.ChoiceField(choices=(('Male',"Male"),('Female',"Female"),('Others',"Others") ),widget=forms.RadioSelect,initial='Male',)
    address = forms.CharField(max_length=50)
    age = forms.IntegerField()
    qualification = forms.CharField(max_length=50)
    adhaar_number = forms.CharField(max_length=30)

class NursingStaffForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=(('Male',"Male"),('Female',"Female"),('Others',"Others") ),widget=forms.RadioSelect,initial='Male',)
    
    class Meta:
        model = NursingStaffModel
        fields = "__all__"

class RoomServiceStaffForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=(('Male',"Male"),('Female',"Female"),('Others',"Others") ),widget=forms.RadioSelect,initial='Male',)
    
    class Meta:
        model = RoomServiceStaffModel
        fields = "__all__"



class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout('name',
                                    'amount',
                                    'address',
                                    'phone_number',
                                    Submit('submit','submit',css_class='button white btn-block btn-primary'))
