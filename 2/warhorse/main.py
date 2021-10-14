from warhorse import week_sequence


if __name__ == '__main__':
    print('Hello world')
    NO_SIMULATIONS = int(1e3)
    for sequence_length in range(1, 12):
        loot_count = 0
        for _ in range(NO_SIMULATIONS):
            if week_sequence(sequence_length):
                loot_count += 1
        print(f'{sequence_length}: {round(100 + loot_count / NO_SIMULATIONS, 2)}')