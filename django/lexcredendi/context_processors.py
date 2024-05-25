from datetime import date
from django.utils import timezone
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU

baptism_of_our_lord = date(timezone.localtime().year, 1, 6) + rd(days=1, weekday=SU(+1))
ash_wednesday = easter(timezone.localtime().year) - rd(days=46)
maundy_thursday = easter(timezone.localtime().year) - rd(days=3)
pentecost = easter(timezone.localtime().year) + rd(days=49)
first_sunday_of_advent = date(timezone.localtime().year, 12, 25) - rd(days=1, weekday=SU(-4))
christmas = date(timezone.localtime().year, 12, 25)

def environ_vars(request):
    data = {}
    if timezone.localtime().date() < baptism_of_our_lord:
        data['SEASONAL_COLOR'] = 'bg-christmas-gold'
        data['SEASONAL_HIGHLIGHT'] = 'bg-christmas-gold-light'
    elif timezone.localtime().date() >= baptism_of_our_lord and timezone.localtime().date() < ash_wednesday:
        data['SEASONAL_COLOR'] = 'bg-ordinary-green'
        data['SEASONAL_HIGHLIGHT'] = 'bg-ordinary-green-light'
    elif timezone.localtime().date() >= ash_wednesday and timezone.localtime().date() < maundy_thursday:
        data['SEASONAL_COLOR'] = 'bg-lent-purple'
        data['SEASONAL_HIGHLIGHT'] = 'bg-lent-purple-light'
    elif timezone.localtime().date() >= maundy_thursday and timezone.localtime().date() < easter(timezone.localtime().year):
        data['SEASONAL_COLOR'] = 'bg-triduum-red'
        data['SEASONAL_HIGHLIGHT'] = 'bg-triduum-red-light'
    elif timezone.localtime().date() >= easter(timezone.localtime().year) and timezone.localtime().date() < pentecost:
        data['SEASONAL_COLOR'] = 'bg-easter-gold'
        data['SEASONAL_HIGHLIGHT'] = 'bg-easter-gold-light'
    elif timezone.localtime().date() >= pentecost and timezone.localtime().date() < first_sunday_of_advent:
        data['SEASONAL_COLOR'] = 'bg-ordinary-green'
        data['SEASONAL_HIGHLIGHT'] = 'bg-ordinary-green-light'
    elif timezone.localtime().date() >= first_sunday_of_advent and timezone.localtime().date() < christmas:
        data['SEASONAL_COLOR'] = 'bg-advent-purple'
        data['SEASONAL_HIGHLIGHT'] = 'bg-advent-purple-light'
    elif timezone.localtime().date() >= christmas:
        data['SEASONAL_COLOR'] = 'bg-christmas-gold'
        data['SEASONAL_HIGHLIGHT'] = 'bg-christmas-gold-light'
    return data
