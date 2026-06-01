import alchemy

if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using 'import alchemy' structure to access potions")

    strength_result = alchemy.strength_potion()
    print(f"Testing strength_potion: {strength_result}")

    heal_result = alchemy.heal()
    print(f"Testing heal alias: {heal_result}")