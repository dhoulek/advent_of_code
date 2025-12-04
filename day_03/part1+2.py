def joltage(bank, N=2):
    # Given a bank of battery ratings (digits 1–9),
    # choose exactly N batteries, keeping their left-to-right order,
    # such that the resulting N-digit number is as large as possible.
    #
    # This works by repeatedly selecting the next digit:
    #   At position i, we may only choose from the range of digits
    #   that still leaves enough batteries to pick the remaining ones.
    #
    # For part 1: N = 2 (pick two digits → largest 2-digit number).
    # For part 2: N = 12 (pick twelve digits under “friction” rules).
    #
    # This is the classic greedy algorithm for selecting the lexicographically
    # largest subsequence of fixed length.

    j = 0  # Accumulated output number as we append each chosen digit

    for i in range(N):
        l = len(bank)

        # We must pick N total digits. If we are picking digit i,
        # then there must remain (N - i - 1) digits AFTER the chosen one.
        #
        # Therefore, the search window ends at:
        #   l - (remaining_to_pick - 1) = l + i - (N - 1)
        #
        # We search only within this prefix of `bank`,
        # because picking beyond it would leave too few digits left.
        window_end = l + i - (N - 1)

        # The next chosen digit is simply the **maximum digit** in the allowed window.
        m = max(bank[:window_end])

        # Find where that maximum digit occurs.
        p = bank.index(m)

        # Cut the bank so that future choices must come after the selected digit.
        bank = bank[p + 1:]

        # Append this chosen digit to the joltage output.
        j = 10 * j + m

    return j


total_part1 = 0
total_part2 = 0

with open('input.txt') as f:
    for l in f.readlines():
        l = l.strip()

        # Parse digits in the bank
        digits = [int(i) for i in l]

        # Part 1: choose exactly 2 batteries → largest possible two-digit number
        total_part1 += joltage(digits)

        # Part 2: choose exactly 12 batteries → friction version
        total_part2 += joltage([int(i) for i in l], N=12)

print(f'The total output joltage is: {total_part1}')
print(f'The total output joltage with friction is: {total_part2}')