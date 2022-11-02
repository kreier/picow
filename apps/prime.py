import math, time, board, digitalio
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
last = 10000
found = 4     # we start from 11, know already 2, 3, 5, 7
led.value = True
print(f"Prime numbers to {last}")
start = time.monotonic()
for number in range(11, last, 2):
    prime = True
    for divider in range(3, int(math.sqrt(number))+1, 2):
        if number % divider == 0:
            prime = False
            break
    if prime:
        found += 1
end = time.monotonic()
print(f"This took: {(end - start)} seconds.")
print(f"I found {found} prime numbers.")
led.value = False

for i in range(10):
    time.sleep(0.1)
    led.value = True
    time.sleep(0.1)
    led.value = False

