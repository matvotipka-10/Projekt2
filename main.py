import random
import time

separator = ("-----------------------------------------------")

def greeting():
    """Greets player."""
    print(f"""
Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter a number:
{separator}""")

def random_number() -> str:
    """
    Returns a string of a random four-digit number.
    The number must not start with 0 and the digits must not be repeated.
    If the number starts with 0, the function replaces it with a random digit
    that is not part of the four-digit number.
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
    Returns player's guess for a four-digit number.
    """
    player_number = (input(">>> "))        
    return (player_number)

def control_player_number(player_number: str) -> bool:
    """
    Accepts a string (player's guess). 
    It checks if: length is 4, contains only digits,
    does not start with "0", does not have duplicate characters. 
    If all is met it returns True, otherwise it returns False. 
    """
    if len(player_number) != 4:
        print(f"""You did not enter a 4 digit number.
{separator}""")
        return False
    if not player_number.isdigit():
        print(f"""You did not enter a number.
{separator}""")
        return False
    if player_number[0] == "0":
        print(f"""Your number starts with 0.
{separator}""")
        return False
    if not len(player_number) == len(set(player_number)):
        print(f"""There are duplicates in your number.
{separator}""")
        return False
    else:
        return True
 
def compare_numbers(player_number: str, random_number: str) -> int:
    """
    Compares the digits from player_number and random_number.
    If the digit is the same and in the same position, it means 1 bull.
    If the digit is in random_number but not at the same position, it is 1 cow.
    random_number = 2017
    player number = 2107
    bulls = 2
    cows = 2
    """
    bulls = 0
    cows = 0
    for index, digit in enumerate(player_number):
        if digit == random_number[index]:
            bulls += 1  
        else:    
            if digit in random_number:
                    cows += 1
    bull_or_bulls = ("bulls")
    if bulls == 1:
        bull_or_bulls = ("bull")
    cow_or_cows = ("cows")
    if cows == 1:
        cow_or_cows = ("cow")
    print(f"""{bulls} {bull_or_bulls}, {cows} {cow_or_cows}
{separator}""")
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
{separator}
That's amazing!""")
                break

                
        
