import time
import random

word = "bottles"

for i in range(99, 0, -1):
    print(i, word, "of beer on the wall")
    print(i, word, "of beer!")
    print("Take one down, pass it around")
    if i == 1:
        print("No more bottles of beer on the wall")
    else:
        n = i - 1
        if n == 1:
            word = "bottle"
        print(n, word, "of beer on the wall")
    print()
    s = random.randint(1, 5)
    time.sleep(s)
