from django.shortcuts import render

# Create your views here.
def My_view(request):
    render(request, "car_list.html", )
    