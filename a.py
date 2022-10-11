from datetime import date, timedelta

#Día actual
today = date.today()
ayer = today - timedelta(days = 1)
print(ayer)
