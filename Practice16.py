n = int(input("Enter a Number: "))
res = 0
if n > 17:
    res = n - 17
    print(f"Final Result is: {res*2}")
else:
    res = n - 17
    print(f"Final Result is: {abs(res)}")
