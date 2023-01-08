from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    number1 = int(request.GET.get('number1'))
    number2 = int(request.GET.get('number2'))

    answer = number1+number2

    return render(request,'result.html',{'answer': answer})
