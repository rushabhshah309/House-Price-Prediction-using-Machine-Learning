from django.shortcuts import render,redirect
from main.models import HouseDetails
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import *

import pickle

regressor = pickle.load(open("C:/Users/RUSHABH/Desktop/SGH_files/KC_SAVED_RANDOM_FOREST_ORIGINAL.sav", "rb"))

import numpy as np


def waterfront_convert(bool_water):
    if bool_water == 'Yes':
        return 1
    else:
        return 0

def year_renovated_convert(year_built, year_reno):
    if year_reno < year_built:
        return 0
    else:
        return year_reno


def predict_user_values(inp):

    arr = np.array(inp)
    arr = np.reshape(arr, (1, len(inp)))
    pred = regressor.predict(arr)
    return (pred[0])




def home(request):
    return render(request, 'main/home.html')


def predict(request):
    if request.method == "POST":
        bedroom = request.POST.get('number1')
        bathroom = request.POST.get('number2')
        sqft_living = request.POST.get('number3')
        sqft_lot = request.POST.get('number4')
        floors = request.POST.get('number5')
        sqft_above = request.POST.get('number6')
        sqft_basement = request.POST.get('number8')
        zipcode = request.POST.get('number9')
        sqft_living15 = request.POST.get('number10')
        sqft_lot15 = request.POST.get('number11')
        waterfront = waterfront_convert(request.POST.get('waterfront'))
        year_built = request.POST.get('date')
        year_renovated = year_renovated_convert(year_built, request.POST.get('yesno'))
        viewss = request.POST.get('viewss')
        condition = request.POST.get('condition')
        grade = request.POST.get('grade')


        l = [bedroom, bathroom, sqft_living, sqft_lot, floors, waterfront,
             viewss, condition, grade, sqft_above, sqft_basement,
             year_built, year_renovated, zipcode, 47.560053, -122.213896,
             sqft_living15, sqft_lot15]

        final_price = predict_user_values(l)
        print(final_price)

        # messages.info(request, 'The predicted price is ${}'.format(final_price))


        val = HouseDetails(bedroom=bedroom, bathroom=bathroom, sqft_living=sqft_living, sqft_lot=sqft_lot, floors=floors, sqft_above=sqft_above, sqft_basement=sqft_basement,
                           zipcode=zipcode, sqft_living15=sqft_living15, year_renovated=year_renovated,
                           sqft_lot15=sqft_lot15, year_built=year_built, viewss=viewss, waterfront=waterfront,
                           condition=condition, grade=grade, price=final_price)
        #if user.status == "active":
        val.save()

        return render(request,'main/predict1.html',{'val':val})
    else:
        return render(request,'main/predict.html')

def about(request):
    return render(request, 'main/about.html')

def predict1(request):
    return render(request,'main/predict1.html')

@login_required
def data(request):
    items=HouseDetails.objects.all()
    return render(request, 'main/data.html', {'items': items})