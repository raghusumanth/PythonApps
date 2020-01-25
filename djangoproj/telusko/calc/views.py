from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Raghu'})
    #return HttpResponse("<h1>Hello world</h1>")

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    #val1 = int(request.GET['num1'])
    #val2 = int(request.GET['num2'])

    res=val1+val2
    return render(request,'result.html',{'res':res})




#MVT or MTV
#User<--->Django<-->url<--->view<--->model<--->database
#view<-->template
#Download UI from travello colorlib






