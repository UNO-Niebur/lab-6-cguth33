#DiceRoll.py
#Name: Carter Guthrie
#Date: 3/1/2025
#Assignment: Lab 6
import random

def main():
    # Create a list with 13 slots (0-12). Sums 2-12 will be stored here.
    rolls = [0] * 13 
    trials = 10000

    for i in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        rolls[total] += 1

    print("Sum | Count | Percentage")
    print("-------------------------")
    for s in range(2, 13):
        percent = (rolls[s] / trials) * 100
        print(f"{s:>3} | {rolls[s]:>5} | {percent:>6.1f}%")

if __name__ == '__main__':
    main()