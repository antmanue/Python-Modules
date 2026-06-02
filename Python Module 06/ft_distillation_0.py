from alchemy.potions import healing_potion, strength_potion

if __name__ == "__main__":
    print("== Distillation 0 ==")
    print("Direct access to alchemy/potion.py")

    strength_result = strength_potion()
    print(f"Testing strength_potion: {strength_result}")

    heal_result = healing_potion()
    print(f"Testing healing_potion: {heal_result}")
