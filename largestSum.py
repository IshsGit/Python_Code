def max_non_adjacent_sum(arr):
    incl = 0
    excl = 0

    for num in arr:

        new_excl = max(incl, excl)

        incl = excl + num
        excl = new_excl

    # Return the maximum of incl and excl
    return max(incl, excl)
