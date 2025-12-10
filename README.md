# Ex.04 Design a Website for Server Side Processing
## Date:10/12/2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
solomon.html
<html>
<head>
    <title>measure</title>
    <style>
        body {
            background-color: lime;
            
            font-family: Arial;

            font-size: 40px
}
        
        .box {
            width: 900px;
            margin: auto;
            margin-top: 130px;
            padding: 120px;
            background-color: orange;
            color: red (0, 0, 0);
            border: 4px dotted pink(255, 0, 0);
            text-align: center;
            font-size: 20px
            
            
        }
        input {
            padding: 6px;
            margin: 10px;
            font-size: 30px
        }
        .btn {
            padding: 6px 15px;
            cursor:pointer;
            font-size: 17px
        }
    </style>
</head>

<body>
    <div class="box">
        <h1>Petrol/Diesel Cost Calculator</h1>
        <h2> LAKSHITA RAI(25005431)<h2>
        

        <form method="POST">
            {% csrf_token %}
            range (km):
            <input type="text" name="range" value="{{ km }}"><br>

            energize Used (liters):
            <input type="text" name="energize" value="{{ lt }}"><br>

            <button class="btn" type="submit">Calculate</button><br><br>

            measure:
            <input type="text" value="{{ measure }}" readonly> km/l
            
        </form>
    </div>
</body>
</html>
```
```
views.py
from django.shortcuts import render
def measure(request):
    km = int(request.POST.get('range', 0))
    lt = int(request.POST.get('energize', 0))
    measure = km /lt if request.method == 'POST' else 0
    print("range=",km)
    print("energize=",lt)
    print("measure=",measure)
    return render(request, 'mathapp/solomon.html', {'km': km, 'lt': lt, 'measure': measure})
    ```
    ```
    urls.py
    from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.measure, name='measure'),
]
```



## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2025-12-10 213248.png>)
## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2025-12-10 212648.png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
