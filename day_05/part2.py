def find_range(ranges, i):
    """
    Given a sorted, non-overlapping list of ranges and a number i,
    determine where i fits relative to the existing ranges.

    Returns a pair (m, M):
      - If i lies inside ranges[r], return (r, r).
      - If i lies *between* ranges[r] and ranges[r+1], return (r, r+1).
      - If i is below the first range, return (None, 0).
      - If i is above the last range, return (len(ranges)-1, None).

    This function is used to figure out how a new interval should be merged
    with the already merged list of ranges.
    """

    if i < ranges[0][0]:
        # i is smaller than all known ranges
        return None, 0

    elif i > ranges[-1][1]:
        # i is larger than all known ranges
        return len(ranges) - 1, None

    else:
        # Scan existing ranges for placement
        for r in range(len(ranges)):
            if ranges[r][0] <= i <= ranges[r][1]:
                # i is inside ranges[r]
                return r, r

            # Check gap between ranges[r] and ranges[r+1]
            elif ranges[r][1] < i < ranges[r+1][0]:
                return r, r+1


def add_range(ranges, r):
    """
    Insert a new range r = [low, high] into a sorted, non-overlapping
    list of existing ranges, merging where appropriate.

    Handles all cases:
      - Inserting before all existing ranges
      - Inserting after all existing ranges
      - Overlapping with one or more ranges
      - Bridging two existing ranges
      - Being entirely contained or partially overlapping
    """

    # If there are no existing ranges, the new one becomes the entire list
    if len(ranges) == 0:
        return [r]

    # Determine where the start and end of r fall relative to current ranges
    m0, M0 = find_range(ranges, r[0])   # Placement of r.start
    m1, M1 = find_range(ranges, r[1])   # Placement of r.end

    # Case 1: r ends beyond all ranges → M1 == None
    if M1 is None:

        # Case 1a: r also begins beyond all ranges
        if M0 is None:
            # r is entirely after the last range → append it
            return ranges + [r]

        # Case 1b: r starts before everything
        elif m0 is None:
            # r fully covers everything → it becomes the only range
            return [r]

        # Case 1c: r starts somewhere inside or beyond a range,
        # and ends beyond all ranges
        else:
            # Merge r with the last overlapping/influenced range
            return ranges[:M0] + [[min(r[0], ranges[M0][0]), r[1]]]

    # Case 2: r begins before all ranges → m1 == None and the other endpoint is inside
    elif m1 is None:
        # r lies entirely before existing ranges → prepend
        return [r] + ranges

    # Case 3: r is fully internal (intersects middle portion)
    else:
        # Case 3a: r starts before the ranges but ends inside them
        if m0 is None:
            return [[r[0], max(r[1], ranges[m1][1])]] + ranges[m1+1:]

        # Case 3b: r overlaps a middle section or merges multiple ranges
        else:
            return (
                ranges[:M0] +
                [[min(r[0], ranges[M0][0]), max(r[1], ranges[m1][1])]] +
                ranges[m1+1:]
            )


ranges = []

# Read only the FIRST section of the input (fresh ID ranges)
with open('input.txt') as f:
    for l in f.readlines():
        l = l.strip()

        # Blank line marks the end of the fresh ranges section
        if len(l) == 0:
            break

        else:
            # Parse "a-b" into [a, b]
            r = [int(i) for i in l.split('-')]

            # Insert and merge the new range into our growing list
            ranges = add_range(ranges, r)

# Count all fresh IDs: sum of ranges' lengths
print(f'Number of fresh ingrediences according to the fresh ingredient ID ranges: '
      f'{sum([r[1] - r[0] + 1 for r in ranges])}')