number_of_seconds = int(input("Input number of seconds:"))
number_of_days = number_of_seconds // 86400
number_of_hours = number_of_seconds % 86400 // 3600 
number_of_minutes = number_of_seconds%86400%3600//60
number_of_seconds2 = number_of_seconds%86400%3600%60

print(number_of_days, ": " "{:02d}".format(number_of_hours), ": " "{:02d}".format(number_of_minutes),": " "{:02d}".format(number_of_seconds2))