def leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return "it is a Leap Year"
            
            else:
              return "it is a not leap year"
        else:
            return "it is a Leap Year"
    else:
        return "it is a not Leap year"
    

print(leap(1990))