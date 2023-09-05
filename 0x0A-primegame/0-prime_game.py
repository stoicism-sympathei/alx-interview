#!/usr/bin/python3
"""
This script defines a function to determine the winner of a prime number removal game.
"""

def isWinner(x, nums):
    """
    Determine the winner of each round in the game and find out who won the most rounds.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n for each round.

    Returns:
        str or None: The name of the player who won the most rounds or None if it's a tie.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def calculate_winner(n):
        if n == 1:
            return "Ben"
        if n % 2 == 0:
            return "Maria"
        return "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if is_prime(n):
            winner = calculate_winner(n)
            if winner == "Maria":
                maria_wins += 1
            elif winner == "Ben":
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print("Winner: {}".format(isWinner(x, nums)))
