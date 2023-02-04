def is_year_leap(year):
 

 year = int(year)
 
 if (year % 4 == 0):
    print("Год", year, ":True")

 if (year % 4 != 0):
    print("Год", year, ": False")
 

print (is_year_leap(input("Введите год: ")))
