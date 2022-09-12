from time import time
import requests
import datetime
import time
from django.shortcuts import render


# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Jakarta'

    appid = 'b3fbfdc6bd795970734a975b5779173e'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'units': 'metric', 'appid': appid}

    req = requests.get(url=URL, params=PARAMS)
    res = req.json()
    description = res['weather'][0]['description']
    main = res['weather'][0]['main']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today().strftime('%A, %d %b %Y')
    clock = time.strftime('%H.%M')

    return render(
        request, 'weatherapp/index.html', {
            'descriptions': description,
            'main': main,
            'icon': icon,
            'temp': temp,
            'day': day,
            'clock': clock,
            'city': city,
        }
    )
