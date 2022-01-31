lim = int(input())
velocity = int(input())
dif = velocity - lim
if dif <= 0:
    print('Congratulations, you are within the speed limit!')
else:
    fine = 100 if dif <= 20 else 270 if dif <= 30 else 500
    print(f'You are speeding and your fine is ${fine}.')
