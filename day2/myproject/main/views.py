from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader

def home(request):
    return render(request,'home.html')
def home1(request):
    return render(request,'home1.html')
def about(request):
    return render(request,'about.html')

#def about(request):
    #temp=loader.get_template('about.html')
    #return render(temp.render())
# Create your views here.
