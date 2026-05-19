import random
import string

print("\n Welcome to the Simple Password Generator!")
print("----------------------------------------")

while True:
    
    length = input("\nHow many characters password?: ")
    
    try:
        length = int(length)
        if length < 4:
            print(" That's too short.Randomly make it 8 characters for you.")
            length = 8
    except:
        print(" That's not a number.Randomly making it 8 characters.")
        length = 8
    
    characters = string.ascii_letters + string.digits + "!@#$%"
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"\n Your password: \033[92m{password}\033[0m")
    
    again = input("\nMake another? (y/n): ").lower()
    if again != 'y':
        print("\n Bye!!")
        break
