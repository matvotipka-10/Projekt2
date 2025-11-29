import random
import time

def greeting():
    """Funkce pozdraví hráče."""
    print("""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------""")

def random_number() -> str:
    """
    Funkce vrací string náhodného čtyřmístného čísla.
    Nesmí začínat 0 a číslice se nejsmějí opakovat.
    """
    list_number = list(range(0,10))
    random_list_number = random.sample(list_number, 4)
    if random_list_number[0] == 0:
        for n in list_number:
            if n != 0 and n not in random_list_number:
                random_list_number[0] = n
    random_number = (''.join(map(str, random_list_number)))
    return random_number
    
def player_guess() -> str:
    """
    Funcke vrací hráčův tip na čtyřmístné číslo.
    """
    player_number = (input(">>> "))        
    return (player_number)

def control_player_number(player_number: str) -> bool:
    """
    Funkce přijme string (hráčův tip). Zkontroluje postupně: délka je 4, obsahuje jen číslice,
    nezačíná "0", nemá duplicitní znaky. Pokud je vše splněno vrátí True, jinak vrátí False.
    """
    if len(player_number) != 4:
        print("""You did not enter a 4 digit number.
-----------------------------------------------""")
        return False
    if not player_number.isdigit():
        print("""You did not enter a number.
-----------------------------------------------""")
        return False
    if player_number[0] == "0":
        print("""Your number starts with 0.
-----------------------------------------------""")
        return False
    if not len(player_number) == len(set(player_number)):
        print("""There are duplicates in your number.
-----------------------------------------------""")
        return False
    else:
        return True
 
def compare_numbers(player_number: str, random_number: str) -> int:
    """
    Funkce porovnává číslice z player_number a random_number. Pokud je číslice stejná
    a zároveň na stejné pozici, znamená to 1 bull. Pokud se číslice jen nachází,
    ale není na stejné pozici jedná se o cow.
    random_number = 2017
    player number = 2107
    bulls = 2
    cows = 2
    """
    bulls = 0
    cows = 0
    for i in range(len(player_number)):
        if player_number[i] == random_number[i]:
            bulls += 1  
        else:    
            if player_number[i] in random_number:
                    cows += 1
    
    if bulls <= 1 and cows <= 1:
        print(f"""{bulls} bull, {cows} cow
-----------------------------------------------""")
    elif bulls >= 2 and cows <= 1:
        print(f"""{bulls} bulls, {cows} cow
-----------------------------------------------""")
    elif bulls <= 1 and cows >= 2:
        print(f"""{bulls} bull, {cows} cows
-----------------------------------------------""")
    else:
        print(f"""{bulls} bulls, {cows} cows
-----------------------------------------------""")    
    return bulls
    
if __name__ == "__main__":
    greeting()
    random_num = random_number()
    guesses = 0
    start_time = time.time()
    while True:
        player_num = player_guess()
        guesses += 1
        if control_player_number(player_num) is True:
            if compare_numbers(player_num, random_num) == 4:
                end_time = time.time()
                duration = end_time - start_time
                print(f"""Correct, you've guessed the right number
in {guesses} guesses.
Time: {duration:.2f} seconds.
-----------------------------------------------
That's amazing!""")
                break

                
        
