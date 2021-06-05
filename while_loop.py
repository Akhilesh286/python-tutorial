i=1
while i<=5:
    print('#' * i)
    i +=1
print ("done")
"game"

secret_number=9
guess_count = 0

guess_limit = 3

while guess_count < guess_limit: 
    guess = int(input('Guess: ')) 
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break

else:
    print ("soory")
"car game"

çommand = ""
staterd = False
while True:
    command = input("> ").lower()

    if command == "start":
        if staterd:
            print ("car is alldredi staterd")
        else:
            staterd == True
            print ("Car started...")

    elif command == "stop":
        if not started:
            print ("car is alldredi staterd")
        else:
            staterd == False
            print("Car stopped.")
        

    elif command == "help": 
        print("""
start to start the car  
stop - to stop the car    
quit - to quit
    """)
    elif command == "quit":
        break
    
    else:
        print ("icant now")















