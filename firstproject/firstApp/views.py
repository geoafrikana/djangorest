from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

def employeeView(request):
    emp = {
        'id':123,
        'name': 'Olagunju Nasiru Adebayo',
        'sal' : 10000
    }

    data = Employee.objects.all();
    print(data)
    response = {'employees': list(data.values('name', 'sal'))}

    return JsonResponse(response)
