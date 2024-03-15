def maxEvents(arrival, duration):
    if len(arrival) < 1:
        return len(arrival)
    merged = []  # [[1, 3], [3, 4], [3, 5], [5, 7], [7, 8]]
    for idx, el in enumerate(arrival):
        merged.append([el, el+duration[idx]])
    maxEvents = 1
    merged = sorted(merged)
    overlap = [merged[0]]
    endtime = merged[0][1]
    for interval in merged[1::]:
        # merged[-1][1] will always have the latest time/endtime
        if interval[0] > overlap[-1][1] & interval[1] > endtime:
            maxEvents += 1
        else:
            overlap.append(interval)

    return maxEvents


print(maxEvents([1, 3, 3, 5, 7], [2, 2, 1, 2, 1]))
