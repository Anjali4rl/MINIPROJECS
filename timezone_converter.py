import pytz , datetime
year=int(input())
month=int(input())
day=int(input())
hour=int(input())
min=int(input())
user_time=datetime.datetime(year,month,day,hour,min)
cairo_timezone=pytz.timezone('Africa/Cairo')
cairo_time=pytz.utc.localize(user_time).astimezone(cairo_timezone)

london_timezone=pytz.timezone('UTC')
london_time=pytz.utc.localize(user_time).astimezone(london_timezone)

delhi_timezone=pytz.timezone('Asia/Kolkata')
delhi_time=pytz.utc.localize(user_time).astimezone(delhi_timezone)

Sydney_timezone=pytz.timezone('Australia/Sydney')
sydney_time=pytz.utc.localize(user_time).astimezone(Sydney_timezone)


print("Cairo time is ",cairo_time.isoformat())
print("London time is ",london_time.isoformat())
print("Delhi time is ",delhi_time.isoformat())
print("Sydney time is ",sydney_time.isoformat())