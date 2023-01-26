import time
import random

def random_color():
    return random.choice(['\033[31m', '\033[32m', '\033[33m', '\033[35m'])

def firework():
    print(random_color() + "*" * random.randint(5, 15))

while True:
    firework()
    time.sleep(0.1)
