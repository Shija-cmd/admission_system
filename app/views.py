from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DataForm
from . models import Data
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
from io import BytesIO  

@login_required
def index(request):
    shortlisted_applicants = Data.objects.all()
    context = {'shortlisted_applicants': shortlisted_applicants
    }
    return render(request, 'app/index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username = username):
            messages.error(request, "Username already exist!")
            return redirect('register')
            
        if User.objects.filter(email = email):
            messages.error(request, "Email already exist!")
            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, "The usename must be Alpha-Numeric")
            return redirect('register')    
        
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "Your account has been created successfully!")
        return redirect('login')
        
    return render(request, 'app/register.html', {})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        
        else:
            return HttpResponse('Error, user does not exist!')
        
    return render(request, 'app/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login')

def data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:    
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'app/data.html', context)


def base(request):
    return render(request, 'app/base.html', {})

def nav(request):
    return render(request, 'app/nav.html', {})

# graphs class and functions starts here
class ChartDataView(APIView):
    def get(self, request, format=None):
        data_entries = Data.objects.all().order_by('NAME')
        labels = [entry.NAME for entry in data_entries]
        chartdata = [entry.UGPA for entry in data_entries]
        chartLabel = "GPA"

        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
        }
        return Response(data)
    
# functions for downloading files
# for pdf files
def download_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "GPA STATUS DATA")

    data_entries = Data.objects.all().order_by('NAME')
    y = 700
    for entry in data_entries:
        p.drawString(100, y, f"Name: {entry.NAME}, UGPA: {entry.UGPA}, Research Concept Note: {entry.RCN}, English Test: {entry.TOEFL}, Letter of Recommendation: {entry.LOR}, ACSEE: {entry.HIGH_SCHOOL_POINTS}, Eligibility: {entry.STATUS}")
        y -= 20

    p.showPage()
    p.save()

    buffer.seek(0)
    response.write(buffer.read())
    return response

# for excel files
def download_excel(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=data.xlsx'

    data_entries = Data.objects.all().values('NAME', 'UGPA', 'RCN', 'TOEFL', 'LOR', 'HIGH_SCHOOL_POINTS', 'STATUS')
    df = pd.DataFrame(data_entries)

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Data')

    return response

# view to render the file
def download_page(request):
    return render(request, 'app/download.html')