def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    mage_max = max(mages, key=lambda x: x["power"])
    mage_min = min(mages, key=lambda x: x["power"])
    max_power = mage_max["power"]
    min_power = mage_min["power"]
    avg_power = round(sum(map(lambda x: x["power"], mages))/len(mages), 2)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"}
    ]
    mages = [
        {"name": "Sage", "power": 98, "element": "shadow"},
        {"name": "Alex", "power": 90, "element": "fire"}
    ]
    spells_list = ["fireball", "heal", "shield"]

    print("Testing artifacts sorter...")
    artifacts_sorted = artifact_sorter(artifacts)

    print(
        f"{artifacts_sorted[0]['name']} ({artifacts_sorted[0]['power']} power)"
        f"comes before {artifacts_sorted[1]['name']}"
        f"({artifacts_sorted[1]['power']} power)"
    )

    print("\nTesting power filter...")
    filtered = power_filter(mages, 95)
    print(f"Mage >= 95 power: {filtered}")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells_list)
    for spell in transformed:
        print(spell)

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Stats: {stats}")
