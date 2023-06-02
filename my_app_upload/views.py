from django.shortcuts import render
from django.http import HttpResponse
from  .forms import StudentForm

from .functions.functions import handle_uploaded_file

def index(request):
    if request.method =='POST':
        student = StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfully")
    else:
        student = StudentForm()
        return render(request,"index.html",{'form':student})


