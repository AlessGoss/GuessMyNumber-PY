import random
while True:
 rnd = random
 number = rnd.randrange(1, 99999)
 answer = 0
 print("Press \"CTRL + C\" or close the window to exit.")
 while number != answer:
  while True:
   try:
    answer = int(input("Guess my number! "))
   except KeyboardInterrupt:
    print("Exiting.")
    print("Come back if you want to play again!")
    exit(0)
   except ValueError:
    print("Type a number.")
    continue
   if number > answer:
    print("Higher.")
    continue
   if number < answer:
    print("Lower.")
   if number == answer:
    print("You did it!")
    break
  break
 continue
