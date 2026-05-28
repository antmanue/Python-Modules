import random


def main() -> None:
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
               'john', 'kevin', 'Liam']
    p_all_capitalized = [item.capitalize() for item in players]
    p_capt_og = [item for item in players if item[0].isupper() is True]

    score_dict = {player: random.randint(0, 1000)
                  for player in p_all_capitalized}

    score_avg = round((sum(score_dict.values()) / len(score_dict.keys())), 2)

    high_score_dict = {player: score for player,
                       score in score_dict.items() if score > score_avg}
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {p_all_capitalized}")
    print(f"New list of capitalized names only: {p_capt_og}")
    print()
    print(f"Score dict: {score_dict}")
    print(f"Score average is {score_avg}")
    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    main()
