import random

def greeting():
    """Funkce pozdraví hráče a získá od něj čtyřmístné číslo."""
    print("""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
""")

def random_number() -> str:
    """
    Funkce vrací náhodné čtyřmístné číslo.
    Nesmí začínat 0 a číslice se nejsmějí opakovat.
    """
    list_number = list(range(0,10))
    random_list_number = random.sample(list_number, 4)
    if random_list_number [0] == 0:
        for n in list_number:
            if n != 0 and n not in random_list_number:
                random_list_number[0] = n
    random_number = (''.join(map(str, random_list_number)))
    print(random_number)
    return random_number
    
def player_guess() -> str:
    """
    Hráč zadává svůj tip na čtyřmístné číslo.
    """
    player_number = (input(">>> "))        
    return (player_number)

def control_player_number(player_number: str) -> str:
    """
    Funkce přijme string. Zkontroluje postupně: délka je 4, obsahuje jen číslice,
    nezačíná "0", nemá duplicitní znaky. Pokud je vše splněno vrátí True, jinak vždy vrátí False.
    """
    if len(player_number) != 4:
        print("You did not enter a 4 digit number.")
        return False
    if not player_number.isdigit():
        print("You did not enter a number.")
        return False
    if player_number [0] == "0":
        print("Your number starts with 0.")
        return False
    if not len(player_number) == len(set(str(player_number))):
        print("There are duplicates in your number.")
        return None
    else:
        return player_number
 
def compare_numbers(player_number: str, random_number: str) -> tuple:
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
    for n in range(len(player_number)):
        if random_number[n] != random_number[n]:  
            if player_number(n) in random_number:
                cows += 1
    print(bulls)
    print(cows)

    return bulls, cows
    


greeting()
compare_numbers(control_player_number(player_guess()), random_number())