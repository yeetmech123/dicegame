import random
import time
print("lets gamble its fun")

print("to play please say roll dice")
print("you can bet 150 50 or 100 200 pounds")

aa = random.randint(0, 150)
ab = random.randint(0,100)
ac = random.randint(0,50)
ad = random.randint(0,200)

name = input()
if name == "roll dice 150":
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("your winnings are")
    print(aa)

if name == "roll dice 50":
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("your winnings are")
    print(ac)

if name == "roll dice 100":
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("your wwinnings are")
    print(ab)

if name == "roll dice 200":
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("your winnings are")
    print(ad)

print("thanks for playing dicegame")
