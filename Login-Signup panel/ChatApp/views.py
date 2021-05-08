from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User, auth
from django.db.models import Exists
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Detail, Cast


def login(request):
    if request.method == "GET":
        return render(request, "Login.html")
    else:
        email = request.POST['email']
        email = email.lower()
        '''user = auth.authenticate(username=username)
        if user is None:
            messages.info(request, "Invalid User")
            return redirect("login")
        else:
            user=auth.authenticate(username=username,password=request.POST['password'])
            if user is None:
                messages.info(request, "Invalid Password")
                return redirect("login")
            else:
                auth.login(request, user)
                return redirect("home")'''
        if User.objects.filter(username=email).exists():
            var = User.objects.get(username=email)
            if var.is_active:
                user = auth.authenticate(username=email, password=request.POST['password'])
                if user is None:
                    messages.info(request, "Incorrect Password")
                    return redirect("login")
                else:
                    auth.login(request, user)
                    return redirect("home")
            else:
                messages.info(request, "User Inactive")
                return redirect("login")
        else:
            messages.info(request, "Firstly Create User Here")
            return redirect("create")


@login_required
def home(request):
    var = User.objects.all()
    return render(request, "Home.html", {'data': var})


def exist(request):
    return render(request, "Exist.html")


def create(request):
    if request.method == "GET":
        return render(request, "Create.html")
    else:
        email = request.POST['email']
        email = email.lower()
        if User.objects.filter(username=email).exists():
            print("hello --------------------------->")
            messages.info(request, "User Already Exists")
            # return render(request,"Create.html",{'message':'User Already exist'})
            return redirect("create")
        else:
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password == confirm_password:
                if len(request.POST['phone_no']) == 10:
                    if Detail.objects.filter(phone_no=request.POST['phone_no']).exists():
                        messages.info(request, "Phone No Already Exists")
                        return redirect("create")
                    else:
                        var = User.objects.create_user(username=email, password=request.POST['password'],
                                                       email=email)
                        var.save()
                        var2 = Detail(username=var, phone_no=request.POST['phone_no'])
                        var2.save()
                        return redirect("login")
                else:
                    messages.info(request, "Invalid Phone_no length")
            else:
                messages.info(request, "Confirm Password Not Matches")
                return redirect("create")


@login_required
def logout(request):
    if request.method == "GET":
        auth.logout(request)
        return redirect("login")


def forgotPassword(request):
    if request.method == "GET":
        return render(request, "Forgot.html")
    else:
        email = request.POST['email']
        email = email.lower()
        if User.objects.filter(username=email).exists():
            user = User.objects.get(username=email)
            print(user)
            user.set_password(request.POST['password'])
            user.save()
            return redirect("login")
        else:
            messages.info(request, "User Not Exists")
            return redirect("forgotPassword")


def enter(request):
    if request.method == "GET":
        return render(request, "Enter.html")
    else:
        if User.objects.filter(username=request.POST['email']).exists():
            var = User.objects.get(username=request.POST['email'])
            return render(request, "Permit.html", {'data': var})
        else:
            messages.info(request, "User Not Exists")
            return redirect("enter")


def permit(request, mid):
    if request.method == "GET":
        var = User.objects.get(id=mid)
        print(var.id)
        if var.is_active:
            var.is_active = False
        else:
            var.is_active = True
    var.save()
    return redirect("login")


def message(request,nid):
    var= Cast.objects.filter(username_id=nid)
    return render(request, "message.html",{'data':var})



#---------------------------------------------------Live LANGUAGE_CODE
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth,Group
from django.contrib import messages
from UserManagement.models import UserDetails, DepartmentVisibiltyDetails


# Create your views here.
def loginSignup(request):
    return render(request,"LoginSignup.html")

def signUp(request):
    email=request.POST['email']
    email=email.lower()
    if User.objects.filter(username=email).exists():
        messages.info(request,"User Already Exists")
        return redirect("LoginSignup")
    else:
        password= request.POST['password']
        phone_number=request.POST['phone_number']
        if len(phone_number) == 10:
                if UserDetails.objects.filter(phoneNumber=phone_number).exists():
                    messages.info(request,"Phone no Already Registered")
                    return redirect("LoginSignup")
                else:
                    user = User.objects.create_user(username=email,email=email,password=password)
                    user_details = UserDetails(user=user,phoneNumber=phone_number)
                    user.save()
                    user_details.save()
                    messages.info(request,"User Is Created")
                    return redirect("LoginSignup")
        else:
            messages.info(request,"Invalid Phone No Length")
            return redirect("LoginSignup")


def signIn(request):
    email=request.POST['email']
    email=email.lower()
    password=request.POST['password']
    if User.objects.filter(username=email).exists():
        user = auth.authenticate(username=email,password=password)
        if user is None:
            messages(request,"Incorrect Password")
            return redirect("LoginSignup")
        else:
            auth.login(request,user)
            return redirect("Dashboard")
    else:
        messages.info(request,"Invalid User")
        return redirect("LoginSignup")



def ManageDepartments(request):
    department=Group.objects.all()
    department_visibility=DepartmentVisibiltyDetails.objects.all()
    return render(request,"manageDepartments.html",{'department':department,'department_visibility':department_visibility})



def AddDepartment(request):
    if request.method == "GET":
        return render(request,"addDepartment.html")
    else:
        department_name = request.POST['department_name']
        department_name = department_name.capitalize()
        department = Group(name=department_name)
        department_visibility = DepartmentVisibiltyDetails(department=department)
        department.save()
        department_visibility.save()
        return redirect("ManageDepartments")


def EditDepartment(request,department_id):
    department = Group.objects.get(id=department_id)
    if request.method == "GET":
        return render(request,"editDepartment.html",{'data':department})
    else:
        department_name = request.POST['department_name']
        department_name = department_name.capitalize()
        department.name = department_name
        department.save()
        return redirect("ManageDepartments")


def DeleteDepartment(request,department_id):
    department = Group.objects.get(id=department_id)
    if request.method == "GET":
        department.delete()
        return redirect("ManageDepartments")


def DepartmentVisibilty(request,department_id):
    department_visibility = DepartmentVisibiltyDetails.objects.get(department=department_id)
    if department_visibility.is_active:
        department_visibility.is_active = False
    else:
        department_visibility.is_active = True
    department_visibility.save()
    return redirect("ManageDepartments")
'''