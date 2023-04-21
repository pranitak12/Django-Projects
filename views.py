from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import service,service_booking,car,car_details,team,reviews,Customer
from .forms import services,book_service,teams,review,cars,car_info
# from .forms import NewUserForm
# from django.contrib.auth import login
# from django.contrib import messages
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.hashers import check_password
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    t = loader.get_template('index.html')
    return HttpResponse(t.render())

def about(request):
    t = loader.get_template('about.html')
    return HttpResponse(t.render())

@login_required
def contact(request):
    t = loader.get_template('contact.html')
    return HttpResponse(t.render())

@login_required
def disp_service(request):
    t = loader.get_template('service.html')
    data = service.objects.all().values()
    d={
        'service_data':data
    }
    return HttpResponse(t.render(d))

@login_required
def add_service(request):
    serv = services()
    if request.method == 'POST':
        serv = services(request.POST)
        if serv.is_valid():
            serv.save()
            return redirect('service')

    return render(request,'addservice.html',{'service':serv})

@login_required
def book_services(request):
    book = book_service()
    if request.method == 'POST':
        book = book_service(request.POST)
        if book.is_valid():
            book.save()
            return redirect('home')

    return render(request,'servicebooking.html',{'book':book})

@login_required
def disp_car(request):
    t = loader.get_template('car.html')
    data = car.objects.all().values()
    d={
        'car_data':data
    }
    return HttpResponse(t.render(d))

@login_required
def add_car(request):
    car = cars()
    if request.method == 'POST':
        car = cars(request.POST,request.FILES)
        if car.is_valid():
            car.save()
            return redirect('cars')

    return render(request,'addcar.html',{'cars':car})

def disp_team(request):
    t = loader.get_template('team.html')
    data = team.objects.all().values()
    d={
        'team_data':data
    }
    return HttpResponse(t.render(d))

def add_team_member(request):
    team_m = teams()
    if request.method == 'POST':
        team_m = teams(request.POST,request.FILES)
        if team_m.is_valid():
            team_m.save()
            return redirect('team')

    return render(request,'adddteam.html',{'teams':team_m})

def disp_review(request):
    t = loader.get_template('testimonial.html')
    data = reviews.objects.all().values()
    d={
        'review_data':data
    }
    return HttpResponse(t.render(d))

def add_review(request):
    rev = review()
    if request.method == 'POST':
        rev = review(request.POST,request.FILES)
        if rev.is_valid():
            rev.save()
            return redirect('review')

    return render(request,'addreview.html',{'reviews':rev})

def edit_service(request,service_id):
    service_id = int(service_id)
    serv = service.objects.get(id=service_id)
    serv_f = services(request.POST or None,instance=serv)
    if serv_f.is_valid():
        serv_f.save()
        return redirect('service')
    return render(request, 'addservice.html',{'service':serv_f})

def delete_service(request,service_id):
    service_id = int(service_id)
    serv = service.objects.get(id=service_id)
    serv.delete()
    return redirect('service')
    
def edit_team(request,team_id):
    team_id = int(team_id)
    team_d = team.objects.get(id=team_id)
    teamf = teams(request.POST or None,instance=team_d)
    if teamf.is_valid():
        teamf.save()
        return redirect('team')
    return render(request, 'adddteam.html',{'teams':teamf})

def delete_team(request,team_id):
    team_id = int(team_id)
    serv = team.objects.get(id=team_id)
    serv.delete()
    return redirect('team')

def edit_car(request,car_id):
    car_id = int(car_id)
    car_d = car.objects.get(id=car_id)
    carf = cars(request.POST or None,instance=car_d)
    if carf.is_valid():
        carf.save()
        return redirect('cars')
    return render(request, 'addcar.html',{'cars':carf})

def delete_car(request,car_id):
    car_id = int(car_id)
    serv = car.objects.get(id=car_id)
    serv.delete()
    return redirect('cars')

# def register_request(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful." )
#             return redirect("login")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render (request=request, template_name="register.html", context={"register_form":form})

# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("home")
#             else:
#                 messages.error(request,"Invalid username or password.")
#         else:
#             messages.error(request,"Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="login.html", context={"login_form":form})

class Signup(View):
	def get(self, request):
		return render(request, 'register.html')

	def post(self, request):
		postData = request.POST
		first_name = postData.get('firstname')
		last_name = postData.get('lastname')
		phone = postData.get('phone')
		email = postData.get('email')
		password = postData.get('password')
		# validation
		value = {
			'first_name': first_name,
			'last_name': last_name,
			'phone': phone,
			'email': email
		}
		error_message = None

		customer = Customer(first_name=first_name,
							last_name=last_name,
							phone=phone,
							email=email,
							password=password)
		error_message = self.validateCustomer(customer)

		if not error_message:
			print(first_name, last_name, phone, email, password)
			customer.password = make_password(customer.password)
			customer.register()
			return redirect('login')
		else:
			data = {
				'error': error_message,
				'values': value
			}
			return render(request, 'register.html', data)

	def validateCustomer(self, customer):
		error_message = None
		if (not customer.first_name):
			error_message = "Please Enter your First Name !!"
		elif len(customer.first_name) < 3:
			error_message = 'First Name must be 3 char long or more'
		elif not customer.last_name:
			error_message = 'Please Enter your Last Name'
		elif len(customer.last_name) < 3:
			error_message = 'Last Name must be 3 char long or more'
		elif not customer.phone:
			error_message = 'Enter your Phone Number'
		elif len(customer.phone) < 10:
			error_message = 'Phone Number must be 10 char Long'
		elif len(customer.password) < 5:
			error_message = 'Password must be 5 char long'
		elif len(customer.email) < 5:
			error_message = 'Email must be 5 char long'
		elif customer.isExists():
			error_message = 'Email Address Already Registered..'
		# saving

		return error_message

class Login(View):
    return_url = None
  
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
  
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                # messages('You are looged in as '+ email)
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('/home')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid Email or Password Please Check !!'
  
        print(email, password)
        return render(request, 'login.html', {'error': error_message})
  
  
def logout(request):
    request.session.clear()
    return redirect('login')
