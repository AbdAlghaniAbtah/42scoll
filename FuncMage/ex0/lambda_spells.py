def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda x: x['power'] >= min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda s: f"*{s}*", spells)

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])
    min_power = min(mages, key=lambda x: x['power'])
    avg_power = sum(mage['power'] for mage in mages) / len(mages)
    return {
        'max_power': max_power['name'],
        'min_power': min_power['name'],
        'avg_power': avg_power
    }

def main():
    artifacts = [
        {'name': 'Fire Staff', 'power': 92},
        {'name': 'Crystal Orb', 'power': 85}
    ]
    
    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) comes before {sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)")

    spells = ["fireball", "heal", "shield"]
    
    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(*transformed)

if __name__ == "__main__":
    main()