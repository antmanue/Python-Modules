import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []

    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            scores.append(num)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not scores:
        print(f"No scores provided. Usage: python3 "
              f"{sys.argv[0]} <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores)/len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores)- min(scores)}")


if __name__ == "__main__":
    main()
