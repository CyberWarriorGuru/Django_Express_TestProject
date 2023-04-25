from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import DataCSV
from rest_framework.response import Response
import csv
import json
# Create your views here.
def register_request(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if username != "" and email != "" and password != "": 
            user = User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({'register_state':'success'})
        else:
            return JsonResponse({'register_state':'Post Error'})

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return JsonResponse({'login_state':'success'})
        else:
            return JsonResponse({'llogin_state': 'login failed'})

def logout_request(request):
    logout(request)

def csv_to_json(csvFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    jsonString = json.dumps(jsonArray, indent=4)
    return jsonString
        

def fetchdata(request):
    if request.method == 'POST':
        # try:
            username = request.POST["username"]
            data_row  = DataCSV.objects.filter(username=username)
            csv_path = "data\\" + str(data_row[0]) + ".csv"

            json_result = csv_to_json(csvFilePath=csv_path)
            return JsonResponse({"fetch_result": json_result})
        # except:
        #     return JsonResponse({"fetch_state": "Failed"})
    return JsonResponse({"fetch_state": "There is no post data"})

        
