#   ___            _              ___                
#  / __|_  _ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
# | (_ | || (_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
#  \___|\_,_/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
#                        |___/                       

secret_number = 9
guess_number = 0
guess_limit = 3
while guess_number < guess_limit:
    guess = int(input("Guess: "))
    guess_number += 1
    if guess == secret_number:
        print("Good Guess")
        break
else:
    print("You FAILED, please try again")