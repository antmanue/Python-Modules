import random

achivement_list = [
                   "Crafting Genius", "World Savior", "Master Explorer",
                   "Collector Supreme", "Untouchable", "Boss Slayer",
                   "Strategist", "Unstoppable", "Speed Runner", "Survivor",
                   ]


def gen_player_achievements() -> set:
    player_achivements_number = random.randint(1, len(achivement_list))
    random_achivments = set(random.sample(achivement_list,
                            player_achivements_number))
    return random_achivments


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    achiv_all_dist = alice.union(bob, charlie, dylan)
    achiv_common = alice.intersection(bob, charlie, dylan)

    achiv_alice_diff_others = alice.difference(bob, charlie, dylan)
    achiv_bob_diff_others = bob.difference(alice, charlie, dylan)
    achiv_charlie_diff_others = charlie.difference(alice, bob, dylan)
    achiv_dylan_diff_others = dylan.difference(alice, bob, charlie)

    achiv_alice_diff_all = set(achivement_list).difference(alice)
    achiv_bob_diff_all = set(achivement_list).difference(bob)
    achiv_charlie_diff_all = set(achivement_list).difference(charlie)
    achiv_dylan_diff_all = set(achivement_list).difference(dylan)

    print(f"Player Alice: {alice}")
    print(f"Player Bob : {bob}")
    print(f"Player Charlie : {charlie}")
    print(f"Player Dylan : {dylan}")
    print()
    print(f"All distinct achievements: {achiv_all_dist}")
    print()
    print(f"Common achievements: {achiv_common}")
    print()
    print(f"Only Alice has: {achiv_alice_diff_others}")
    print(f"Only Bob has: {achiv_bob_diff_others}")
    print(f"Only Charlie has: {achiv_charlie_diff_others}")
    print(f"Only Dylan has: {achiv_dylan_diff_others}")
    print()
    print(f"Alice is missing: {achiv_alice_diff_all}")
    print(f"Bob is missing: {achiv_bob_diff_all}")
    print(f"Charlie is missing: {achiv_charlie_diff_all}")
    print(f"Dylan is missing: {achiv_dylan_diff_all}")


if __name__ == "__main__":
    main()
