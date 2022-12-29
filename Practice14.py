date1 = input("Enter Date 1: ")
day1 = date1.split(",")
day1 = int(day1[2])
date2 = input("Enter Date 2: ")
day2 = date2.split(",")
day2 = int(day2[2])
days = day1 - day2
print(f"{abs(days)} Days")