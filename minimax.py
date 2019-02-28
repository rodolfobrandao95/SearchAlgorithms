def minimax(arr, depth):
    if (depth % 2 == 0):
        return get_max(arr)
    else:
        return get_min(arr)


def get_max(arr):
    if (len(arr) == 1):
        return arr[0]
    else:
        max_winners = []

        for i in range(0, len(arr), 2):
            max_winners.append(max(arr[i], arr[i + 1]))

    return get_min(max_winners)


def get_min(arr):
    if(len(arr) == 1):
        return arr[0]
    else:
        min_winners = []

        for i in range(0, len(arr), 2):
            min_winners.append(min(arr[i], arr[i + 1]))

    return get_max(min_winners)
