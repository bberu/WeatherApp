from django.shortcuts import render
import urllib.request
import json
from django.http import Http404

# Create your views here.
def index(request):
    if request.method =='POST':
        search = request.POST.get('search')
        search_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+search+'&appid=fbf3c9118153ceb4fd1cf651b1f2be5b').read()
        convert = json.loads(search_url) 
        #converting fahrenheit  to celcuis 
        fahrenheit = int(convert['main']['temp'])
        celcuis = fahrenheit -273

        feels_like_fahrenheit = int(convert['main']['feels_like'])
        feels_like_celcuis = feels_like_fahrenheit -273

        context = {
            'country_code': str(search.capitalize()) + ' ' + str(convert['sys']['country']),
            'wind_speed':str(convert['wind']['speed']),
            'humidity':str(convert['main']['humidity']) +' %',
            'temp':str(celcuis) +'C°',
            'feels_like':str(feels_like_celcuis) +'C°',
            'icon':(convert['weather'][0]['icon']),
           
        }
    else:
        context = {}
        search = ''

    return render(request,'index.html',context)