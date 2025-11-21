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

def random_number() -> int:
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
    random_number = int(''.join(map(str, random_list_number)))
    return random_number

def player_guess(number: int) -> bool:
    input(">>> ")





#def control_numbers(random_number: int, guess_number: int) -> bool:
#    if 


# Proč by měla fce greeting vracet int? to moc nedává smysl







greeting()
random_number()