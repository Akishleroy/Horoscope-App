import http
import re
# from termios import CKILL
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass
import horoscope

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'geminaurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types={
    'fire':['aries','leo','sagittarius'],
    'earth':['taurus','virgo','capricorn'],
    'air':['gemini','libra','aquarius'],
    'water':['cancer','scorpio','pisces']

}
def get_info_style(request):
    type_list=list(types)
    # name_zodiac=zodiacs[znak_zodiaka-1]
    li_elements=" "
    for sign in type_list:
        reverse_url=reverse("styles-name")
        li_elements+=f"<li> <a href={reverse_url}/{sign}>{sign.title()}</a></li>"
    response=f"""
    <ul>
    {li_elements}
    </ul>

    """
    return HttpResponse(response)

def get_style_fire(request):
    li_elements=" "
    for sign in types["fire"]:
        reverse_url=reverse("horoscope-name",args=[sign])
        li_elements+=f"<li><a href={reverse_url}>{sign.title()}</a></li>"
    response=f"""
    <ul>
    {li_elements}
    </ul>

    """
    return HttpResponse(response)
    # return HttpResponse("aries,leo,pisces")

def get_style_earth(request):
    li_elements=" "
    for sign in types["earth"]:
        reverse_url=reverse("horoscope-name",args=[sign])
        li_elements+=f"<li><a href={reverse_url}>{sign.title()}</a></li>"
    response=f"""
    <ul>
    {li_elements}
    </ul>

    """
    return HttpResponse(response)

def get_style_air(request):
    li_elements=" "
    for sign in types["air"]:
        reverse_url=reverse("horoscope-name",args=[sign])
        li_elements+=f"<li><a href={reverse_url}>{sign.title()}</a></li>"
    response=f"""
    <ul>
    {li_elements}
    </ul>

    """
    return HttpResponse(response)

def get_style_water(request):
    li_elements=" "
    for sign in types["water"]:
        reverse_url=reverse("horoscope-name",args=[sign])
        li_elements+=f"<li><a href={reverse_url}>{sign.title()}</a></li>"
    response=f"""
    <ul>
    {li_elements}
    </ul>

    """
    return HttpResponse(response)



def index(request):
    zodiacs=list(zodiac_dict)
    data={
        'my_dict':zodiac_dict,
        'my_list':zodiacs
    }
    return render(request,'horoscope/index.html',context=data)

@dataclass
class Person:
    name:str
    age:int

    def __str__(self):
        return f'this is {self.name}'

def get_info_znak_zodiaka(request,znak_zodiaka:str):
    description=zodiac_dict.get(znak_zodiaka)
    zodiacs=list(zodiac_dict)
    data={
        'description_zodiac':description,
        'description_namezodiac':znak_zodiaka,
        'zodiacs':zodiacs,
        'zodiac_dict':zodiac_dict
    }

    return render(request,'horoscope/info_zodiac.html',context=data)
    
def get_info_znak_number(request,znak_zodiaka:int):
    zodiacs=list(zodiac_dict)
    if znak_zodiaka>len(zodiacs):
        return HttpResponseNotFound(f'neizvesnyi numberrrrr-{znak_zodiaka}')
    name_zodiac=zodiacs[znak_zodiaka-1]
    reverse_url=reverse("horoscope-name",args=[name_zodiac])
    return HttpResponseRedirect(reverse_url)

def get_sign(request,month,day):
    zod = ['','capricorn',21,'aquarius',20,'pisces',21,'aries',21,'taurus',22,'gemini',22,'cancer',23,'leo',22,'virgo',24,'libra',24,'scorpio',23,'sagittarius',23,'capricorn']
    index=month*2
    zod_index=0
    if day<zod[index]:
        zod_index=zod[index-1]
        return HttpResponseRedirect(f'/{zod_index}')
    zod_index=zod[index+1]
    return HttpResponseRedirect(f'/{zod_index}')

