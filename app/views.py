from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .utils import get_data
# Create your views here.
def index(request):
    return render(request,'index.html')

@csrf_exempt
def check(request):
    if request.method == "GET":
        return HttpResponse("Application is running.", status=200)
    else:
        return HttpResponse("", status=405)

@csrf_exempt
def fetch(request):
    if request.method == "GET":
        try:
            data = get_data()
            return JsonResponse({"success":"True","data":data},status=200)
        except:
            return JsonResponse({"success":"False"},status=500)
    else:
        return HttpResponse("", status=405)

@csrf_exempt
def get_fact(request):
    if request.method == "GET":
        return JsonResponse({"text":"this is a cat fact"},status=200)