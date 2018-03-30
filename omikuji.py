import random

omikuji = random.randint(1,6)
if omikuji == 1:
    print("大吉")
elif omikuji == 2:
    print("中吉")
elif omikuji == 3:
    print("小吉")
elif omikuji == 4:
    print("吉")
elif omikuji == 5:
    print("凶")
else:
    print("大凶")
