import random


LOOT_CHANCE = 0.006


def hasLoot() -> bool:
    return random.random() < LOOT_CHANCE

def week_sequence(no_of_weeks : int) -> bool:
    return any([hasLoot() for _ in range(no_of_weeks)])


