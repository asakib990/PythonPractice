def within_hundred(n):
    return (abs(1000-n) <= 100) or (abs(2000-n) <= 100)

print(within_hundred(900))