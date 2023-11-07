from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def registration(request):
    if 'id' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            address = request.POST['address']
            emp_code = request.POST['emp_code']
            password = request.POST['password']
            data = staff.objects.create(emp_code = emp_code, password=password, mobile_number=mobile, email=email, emp_name=name, address=address)
            data.save()
            return redirect(loginn)
        return render(request,'registration.html')
    else:
        return HttpResponse("<script>window.alert('Please login first!')</script>")

def loginn(request):
    if request.method == 'POST':
        u=request.POST['emp_code']
        v=request.POST['password']
        try:
            data = staff.objects.filter(emp_code = u)
            if data:
                data = staff.objects.get(emp_code = u)
                if data.password == v:
                    print(data.password)
                    request.session['id'] = u
                    return redirect(index)
            else:
                return HttpResponse("<script>window.alert('Incorrect Password. Please check!')</script>")
        except Exception:
            return HttpResponse("<script>window.alert('Incorrect Username. Please check!')</script>")
    return render(request,'login.html')

def admin_log(request):
    if request.method == 'POST':
        u=request.POST['admin_code']
        v=request.POST['password']
        try:
            data = staff.objects.filter(emp_code = u)
            if data:
                data = staff.objects.get(emp_code = u)
                if data.password == v:
                    print(data.password)
                    request.session['ids'] = u
                    return redirect(index)  
            else:
                return HttpResponse("<script>window.alert('Incorrect Password. Please check!')</script>")
        except Exception:
            return HttpResponse("<script>window.alert('Incorrect Username. Please check!')</script>")
    return render(request,'login.html')

def logout_data(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(loginn)
    else:
        return HttpResponse("<script>window.alert('Please login first!')</script>")

def add_customer(request):
    if 'id' in request.session:
        if request.method == 'POST':
            rollno = request.POST['rollno']
            mobile_model = request.POST['mobile_model']
            cust_name = request.POST['cust_name']
            mobile = request.POST['mobile']
            complaint = request.POST['complaint']
            remark_status = request.POST['remark_status']
            technition = request.POST['technition']
            current_date = request.POST['current_date']
            condition = request.POST['condition']
            data = details.objects.create(roll_number = rollno, mobile_model = mobile_model, customer_name = cust_name, mobile_number = mobile, complaint = complaint, remark_status = remark_status, technition = technition, date_time = current_date, condition = condition)
            data.save()
        return render(request,'add_customer.html')
    else:
        return HttpResponse("<script>window.alert('Please login!')</script>")
    
def update_details(request,id):
    if 'id' in request.session:
        context = {
            'data':details.objects.filter(id = id)
        }
        if request.method == 'POST':
            rollno = request.POST['rollno']
            mobile_model = request.POST['mobile_model']
            cust_name = request.POST['cust_name']
            mobile = request.POST['mobile']
            complaint = request.POST['complaint']
            remark_status = request.POST['remark_status']
            technition = request.POST['technition']
            current_date = request.POST['current_date']
            condition = request.POST['condition']
            details.objects.filter(id = id).update(roll_number = rollno, mobile_model = mobile_model, customer_name = cust_name, mobile_number = mobile, complaint = complaint, remark_status = remark_status, technition = technition, date_time = current_date, condition = condition)
            return HttpResponse('<script>window.alert("Updated")</script>')
    return render(request,'update_details.html',context)

def service(request):
    if 'id' in request.session:
        context = {
            'data':details.objects.all()
        }
        return render(request,'service.html',context)
    else:
        return HttpResponse("<script>window.alert('Please login!')</script>")

def search_deatails(request):
    if 'id' in request.session:
        if request.method == 'POST':
            search = request.POST['search']
            context ={
                'search_data':details.objects.all().filter(mobile_number = search)
            } 
            return render(request,'search_result.html',context)
        else:
            return render(request,'service.html')
    else:
        return HttpResponse("<script>window.alert('Please login!')</script>")

def delete_service(request,pk):
    if 'id' in request.session:
        data = details.objects.get(id = pk)
        data.delete()
        return redirect(service)
    else:
        return HttpResponse("<script>window.alert('Please login!')</script>")

def delete_search_service(request,pk):
    if 'id' in request.session:
        data = details.objects.get(id = pk)
        data.delete()
        return redirect(search_deatails)
    else:
        return HttpResponse("<script>window.alert('Please login!')</script>")

