# bounce.py
#
# Exercise 1.5

height = 100 # ball starting height
bounce_back = 3/5 # bounce back rate
num_bounces = 10
bounce = 1 # bounce number

while bounce <= num_bounces:
    height *= bounce_back
    print(bounce, round(height, 4)) 
    bounce += 1
    