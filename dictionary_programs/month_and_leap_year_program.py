month = {'JANUARY' : 31 ,
         'FEBRUARY': 28 ,
         'MARCH' : 31 ,
         'APRIL': 30 ,
         'MAY' : 31 ,
         'JUNE' : 30 ,
         'JULY' : 31 ,
         'AUGUST': 31 ,
         'SEPTEMBER' : 30 ,
         'OCTOBER' : 31 ,
         'NOVEMBER' : 30 ,
         'DECEMBER' : 31}

year = int(input("Enter the Year : "))

month_input = input("Enter a month to find its days : ")
month_input = month_input.strip().upper()

content = "The month {} has {} days {}"
if year >= 2020:
    if year % 2020 == 0:
        month['FEBRUARY'] = 29

elif year < 2020:
    if 2020 % year == 0:
        month['FEBRUARY'] = 29

if month['FEBRUARY'] == 29:
    print(content.format(month_input.lower().capitalize(), month.get(month_input), f"because {year} is an leap year"))
    quit()

print(content.format(month_input.lower().capitalize(), month.get(month_input), ""))
