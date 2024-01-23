import random
game_counter = 0
count_win_run = 0
while True:
    game_counter += 1
    guess_count = 0
    num_ran = random.randint(1, 100)
    print(num_ran)

    while True:
        guess_count += 1
        num1 = int(input("Guess the number (1: 100): "))

        if num1 < num_ran:
            print("Higher ")
            continue
        elif num1 > num_ran:
            print("Below")
            continue
        else:
            print(f"Well done! Guessed the number after {guess_count} tries!")
            count_win_run += guess_count
            break

    repeat = input("Do you want to replay the game? (Y/N)? ")
    if repeat.upper() != "Y":

        print(f"Today you play {game_counter} games.\n"
              f"Weighted average of successful moves {(count_win_run / game_counter):.2f} \n"
              f"Thank you! ")
        break
