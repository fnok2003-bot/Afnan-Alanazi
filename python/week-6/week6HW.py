# Global leaderboard
high_score_board = []   # list of (player, total) tuples


def record_game(player, *scores, bonus=0, multiplier=1.0):
    """
    Records a player's game results.

    Parameters:
        player (str): Player name (positional argument).
        *scores: Any number of round scores.
        bonus (int/float, optional): Added to the total score.
        multiplier (float, optional): Applied to the final score.

    Returns:
        tuple: (player, rounds, total, status)
    """

    global high_score_board

    # No scores given
    if len(scores) == 0:
        return (player, 0, 0, "no rounds played")

    # Negative score check
    if any(score < 0 for score in scores):
        return (player, 0, 0, "negative score not allowed")

    # Calculate total
    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)

    rounds = len(scores)

    # Add to leaderboard
    high_score_board.append((player, total))

    # Sort leaderboard descending by score
    sorted_board = sorted(
        high_score_board,
        key=lambda item: item[1],
        reverse=True
    )

    # Find player's rank
    rank = 1
    for i, entry in enumerate(sorted_board, start=1):
        if entry == (player, total):
            rank = i
            break

    # Status
    if rank == 1:
        status = "high score!"
    else:
        status = f"rank {rank}"

    return (player, rounds, total, status)


# ===== Main Code =====

print(record_game("Ali", 20, 30, 25, bonus=5))
print(record_game("Sara", 50, 40, multiplier=1.2))
print(record_game("Omar", 35, 25, 20))

# Optional test cases
print(record_game("Mona"))
print(record_game("Khaled", 10, -5, 20))

print("\nFinal Leaderboard:")
for player, score in sorted(high_score_board,
                            key=lambda x: x[1],
                            reverse=True):
    print(f"{player}: {score}")