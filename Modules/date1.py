import datetime as dt
print(dt.datetime.now()) 
x= dt.datetime.now()
x= dt.datetime(2022,6,22) #yyyy,mm,dd
print("Year: ",x.year)
print("Month: ",x.month)
print("Day: ",x.day)

# Format Directive / Wildcards to format the date and time
print("Hour: ",x.hour)
print("Minute: ",x.minute)
print("Second: ",x.second)
print("Microsecond: ",x.microsecond)
print("Weekday: ",x.strftime("%A")) #Full Version of Weekday
print("Weekday: ",x.strftime("%a")) #Short Version of Weekday
print("Month: ",x.strftime("%B")) #Full Version of Month
print("Month: ",x.strftime("%b")) #Short Version of Month
print("Date: ",x.strftime("%d/%m/%Y")) #Date in DD/MM/YYYY format
print("Weekday as a Number: ",x.strftime("%w")) 
print("Month as a Number: ",x.strftime("%m"))
print("Year as a Number: ",x.strftime("%y")) #Last 2 digits of Year
print("Year as a Number: ",x.strftime("%Y")) #Full Year