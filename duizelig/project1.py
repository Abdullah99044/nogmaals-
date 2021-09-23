import time
a = 30
while a < 31:
    print(a)
    a = a - 1
    if a == 0:
        break
    time.sleep(1)
print("lanceer de raket!!")