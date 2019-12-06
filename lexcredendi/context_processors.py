from datetime import datetime, date, time
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU

baptism_of_our_lord = date(datetime.now().year, 1, 6) + rd(days=1, weekday=SU(+1))
ash_wednesday = easter(datetime.now().year) - rd(days=46)
maundy_thursday = easter(datetime.now().year) - rd(days=3)
pentecost = easter(datetime.now().year) + rd(days=49)
first_sunday_of_advent = date(datetime.now().year, 12, 25) - rd(days=1, weekday=SU(-4))
christmas = date(datetime.now().year, 12, 25)

def environ_vars(request):
    data = {}
    if datetime.now().date() < baptism_of_our_lord:
        data['SEASONAL_COLOR'] = 'bg-gold'
    elif datetime.now().date() >= baptism_of_our_lord and datetime.now().date() < ash_wednesday:
        data['SEASONAL_COLOR'] = 'bg-success'
    elif datetime.now().date() >= ash_wednesday and datetime.now().date() < maundy_thursday:
        data['SEASONAL_COLOR'] = 'bg-purple'
    elif datetime.now().date() >= maundy_thursday and datetime.now().date() < easter(datetime.now().year):
        data['SEASONAL_COLOR'] = 'bg-danger'
    elif datetime.now().date() >= easter(datetime.now().year) and datetime.now().date() < pentecost:
        data['SEASONAL_COLOR'] = 'bg-gold'
    elif datetime.now().date() >= pentecost and datetime.now().date() < first_sunday_of_advent:
        data['SEASONAL_COLOR'] = 'bg-success'
    elif datetime.now().date() >= first_sunday_of_advent and datetime.now().date() < christmas:
        data['SEASONAL_COLOR'] = 'bg-purple'
    elif datetime.now().date() >= christmas:
        data['SEASONAL_COLOR'] = 'bg-gold'
    return data
