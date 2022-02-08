from django.shortcuts import render,redirect
from razorpay import client
from DGHealthCare.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from .decorators import custom_login_required
from .forms import AmbulanceForm,AppointmentForm, CategoryForm,DoctorForm,RoomServiceStaffForm,NursingStaffForm,ProductForm,OrderForm
from .models import AmbulanceModel,AppointmentModel,DoctorModel,NursingStaffModel,RoomServiceStaffModel,CategoryModel,ProductModel,OrderModel
from .filter import ProductFilter
from django.views import View
import razorpay
# Create your views here.
def homeView(request):
    template_name = 'healthify/home.html'
    context = {}
    return render(request,template_name,context)

def adminView(request):
    template_name = 'healthify/admin.html'
    context = {}
    return render(request,template_name,context)    


@custom_login_required
def addAppointmentView(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            g = form.cleaned_data['gender']
            c = form.cleaned_data['city']
            p = form.cleaned_data['Have_You_Attended_To_The_Facility_Before']
            i = form.cleaned_data['if_Yes_State_What_Condition_And_When']
            a = form.cleaned_data['appointment_date']
            s = form.cleaned_data['Please_Select_Slot']
            con = form.cleaned_data['contact_number']
            data = AppointmentModel(name=n,gender=g,city=c,previous_visit=p,if_before_visited_visit_detail=i,appointment_date=a,slot=s,contact_number=con)
            data.save()           
            return redirect('home')
    template_name = 'healthify/addappointment.html'
    context = {'form':form}
    return render(request,template_name,context)

def showAppointmentView(request):
    template_name = 'healthify/showappointments.html'
    appointments = AppointmentModel.objects.all()
    context = {'appointments':appointments}
    return render(request,template_name,context)


def deleteAppointmentView(request,id):
    appoint = AppointmentModel.objects.get(id=id)
    appoint.delete()
    return redirect('show')


def addAmbulanceView(request):
    form = AmbulanceForm()
    if request.method == 'POST':
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['patient_name']
            a = form.cleaned_data['patient_age']
            g = form.cleaned_data['gender']
            c = form.cleaned_data['contact_number']
            l = form.cleaned_data['location']
            d = form.cleaned_data['disease']            
            data = AmbulanceModel(patient_name=n,patient_age=a,gender=g,contact_number=c,location=l,disease=d)
            data.save()           
            return redirect('home')
    template_name = 'healthify/addambulance.html'
    context = {'form':form}
    return render(request,template_name,context)

def showAmbulanceView(request):
    template_name = 'healthify/showambulance.html'
    ambulance = AmbulanceModel.objects.all()
    context = {'ambulance':ambulance}
    return render(request,template_name,context)


def deleteAmbulanceView(request,id):
    appoint = AmbulanceModel.objects.get(id=id)
    appoint.delete()
    return redirect('showambulance')


def addDoctorView(request):
    if request.method == 'POST':
        n = request.POST['name']            
        g = request.POST['gender']
        a = request.POST['address']
        age = request.POST['age']
        q = request.POST['qualification']            
        aad = request.POST['adhaar_number']            
        data = DoctorModel(name=n,gender=g,address=a,age=age,qualification=q,adhaar_number=aad)
        data.save()           
        return redirect('home')
    template_name = 'healthify/adddoctor.html'
    context = {}
    return render(request,template_name,context)

def showDoctorView(request):
    template_name = 'healthify/showdoctor.html'
    doctor = DoctorModel.objects.all()
    context = {'doctor':doctor}
    return render(request,template_name,context)

def updateDoctorView(request,id):
    mov = DoctorModel.objects.get(id=id)
    if request.method == 'POST':
        n = request.POST['name']            
        g = request.POST['gender']
        a = request.POST['address']
        age = request.POST['age']
        q = request.POST['qualification']            
        aad = request.POST['adhaar_number']   
        DoctorModel.objects.filter(id=id).update(name=n,gender=g,address=a,age=age,qualification=q,adhaar_number=aad)         
        #data = DoctorModel(name=n,gender=g,address=a,age=age,qualification=q,adhaar_number=aad)
        #data.save()           
        return redirect('showdoctor')               
    template_name = 'healthify/adddoctor.html'
    context = {'mov':mov}
    return render(request,template_name,context)


def deleteDoctorView(request,id):
    appoint = DoctorModel.objects.get(id=id)
    appoint.delete()
    return redirect('showdoctor')

def addNursingStaffView(request):
    form = NursingStaffForm()
    if request.method == 'POST':
        form = NursingStaffForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect('shownursingstaff')
    template_name = 'healthify/addnursingstaff.html'
    context = {'form':form}
    return render(request,template_name,context)

def showNursingStaffView(request):
    template_name = 'healthify/shownursingstaff.html'
    nursing = NursingStaffModel.objects.all()
    context = {'nursing':nursing}
    return render(request,template_name,context)

def updateNursingStaffView(request,id):
    mov = NursingStaffModel.objects.get(id=id)
    form = NursingStaffForm(instance=mov)
    if request.method == 'POST':
        form = NursingStaffForm(request.POST,instance=mov)
        if form.is_valid():
            form.save()
            return redirect('shownursingstaff')
    template_name = 'healthify/addnursingstaff.html'
    context = {'form':form}
    return render(request,template_name,context)


def deleteNursingStaffView(request,id):
    appoint = NursingStaffModel.objects.get(id=id)
    appoint.delete()
    return redirect('shownursingstaff')

def addRoomServiceStaffView(request):
    form = RoomServiceStaffForm()
    if request.method == 'POST':
        form = RoomServiceStaffForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect('showroomservicestaff')
    template_name = 'healthify/addroomservicestaff.html'
    context = {'form':form}
    return render(request,template_name,context)

def showRoomServiceStaffView(request):
    template_name = 'healthify/showroomservicestaff.html'
    roomservice = RoomServiceStaffModel.objects.all()
    context = {'roomservice':roomservice}
    return render(request,template_name,context)

def updateRoomServiceStaffView(request,id):
    mov = RoomServiceStaffModel.objects.get(id=id)
    form = RoomServiceStaffForm(instance=mov)
    if request.method == 'POST':
        form = RoomServiceStaffForm(request.POST,instance=mov)
        if form.is_valid():
            form.save()
            return redirect('showroomservicestaff')
    template_name = 'healthify/addroomservicestaff.html'
    context = {'form':form}
    return render(request,template_name,context)


def deleteRoomServiceStaffView(request,id):
    appoint = RoomServiceStaffModel.objects.get(id=id)
    appoint.delete()
    return redirect('showroomservicestaff')

 
def addCategoryView(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect('showcategory')
    template_name = 'healthify/addcategory.html'
    context = {'form':form}
    return render(request,template_name,context)

def showCategoryView(request):
    template_name = 'healthify/showcategory.html'
    category = CategoryModel.objects.all()
    context = {'category':category}
    return render(request,template_name,context)

def deleteCategoryView(request,id):
    appoint = CategoryModel.objects.get(id=id)
    appoint.delete()
    return redirect('showcategory')

def addProductView(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()           
            return redirect('showproduct')
    template_name = 'healthify/addproduct.html'
    context = {'form':form}
    return render(request,template_name,context)

def showProductView(request):
    template_name = 'healthify/showproduct.html'
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products':products,'category':categories}
    return render(request,template_name,context)



def deleteProductView(request,id):
    appoint = ProductModel.objects.get(id=id)
    appoint.delete()
    return redirect('showproduct')

def updateProductView(request,id):
    mov = ProductModel.objects.get(id=id)
    form = ProductForm(instance=mov)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=mov)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name = 'healthify/addproduct.html'
    context = {'form':form}
    return render(request,template_name,context)


#this if for rendering store page 

class StoreHomeView(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        categories = CategoryModel.objects.all()
        category_id = request.GET.get('category')
        print(category_id)
        if category_id:
            products = ProductModel.objects.filter(category=category_id)
        else:
            products = ProductModel.objects.all()        
        template_name = 'healthify/storehome.html'
        #products = ProductModel.objects.all()
        categories = CategoryModel.objects.all()
        myfilter = ProductFilter(request.GET,queryset=products)
        product = myfilter.qs
        context = {'product':product,'categories':categories,'myfilter':'myfilter'}
        return render(request,template_name,context)
 

    def post(self,request):
            product = request.POST["product"]
            remove = request.POST.get('remove')
            print(product)     
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity<=1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity-1
                    else:
                        cart[product] = quantity+1
                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1

            request.session['cart'] = cart
            print('cart',request.session['cart'])
            return redirect('storehome')                         
            
#this is for rendering cart page

def cartView(request):
    cartlist = list(request.session.get('cart').keys())
    cartproducts = ProductModel.objects.filter(id__in=cartlist)
    template_name = 'healthify/cart.html'
    context = {'cartproducts':cartproducts}
    return render(request,template_name,context)


def orderView(request):  
    
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")

       #create razorpay client
        client = razorpay.Client(auth=('rzp_test_nf2QitQ9XiFGMm','yLSp6iJvUwqXVQ3haTfJXL5q'))

       #create order
        response_payment = client.order.create(dict(amount=amount,currency='INR'))

        order_id = response_payment['id']
        order_status = response_payment['status']
        

        if order_status == 'created':
            order = OrderModel(name=name,amount=amount,address=address,phone_number=phone_number)
            order.save()
            response_payment['name'] = name

            form = OrderForm(request.POST or None)
            template_name = 'healthify/order.html'
            context = {'form':form,'payment':response_payment}
            return render(request,template_name,context)
        
    form = OrderForm()     
    template_name = 'healthify/order.html'
    context = {'form':form}
    return render(request,template_name,context)
     

def successView(request):
    response = request.POST
    print(response)
    template_name = "healthify/success.html"
    context = {}
    return render(request,template_name,context)

