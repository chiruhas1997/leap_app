
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.cache import cache

from .utils import get_data
from . tasks import fetch_data_from_url
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
        #try:
        fetch_data_from_url.delay()
        return JsonResponse({"success":"True"},status=200)
        # except:
        #     return JsonResponse({"success":"False"},status=500)
    else:
        return HttpResponse("", status=405)

@csrf_exempt
def get_fact(request):
    if request.method == "GET":
        message = cache.get('message')
        print("message is :",message)
        if message is None or message is '':
            return JsonResponse({"error":"no_task_has_been_queued_yet"})
        else:
            cache.set('message','')

            return JsonResponse({"message":message},status=200)
    else:
        return HttpResponse("",status=405)

