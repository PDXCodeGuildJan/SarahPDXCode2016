from django.shortcuts import render

# Create your views here.
def port_home(request):
    return render(request, 'port_home/index.html')


# def adele(request):
    # return render(request, 'port_home/index.html')