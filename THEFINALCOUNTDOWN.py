#countdown to specific events
from datetime import date, timedelta
# import time

today = date.today()
ets = date(2027, 9, 30)
SBstart = date(2027, 5, 3)
SBend = date(2027, 7, 22)
app = date(2027, 2, 11)
leave = SBstart - timedelta(days=90)
form45 = leave - timedelta(days=30)


print(f"{(ets - today).days} days until ETS.")
print(f"{(SBstart - today).days} days until Skillbridge start.")
print(f"{(SBend - today).days} days until Skillbridge end.")
print(f"{(app - today).days} days until HoH application due.")
print(f"{(form45 - today).days} days until final Form 45 submission.")
print(f"{(leave - today).days} days until final leave/PAR submission.")