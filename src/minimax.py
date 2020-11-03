def minimax(arr, depth):
    if depth == 1:
        return print(arr[0])
    else:
        winners = []

        if depth % 2 == 0:
            for i in range(0, len(arr), 2):
                winners.append(max(arr[i], arr[i + 1]))
        else:
            for i in range(0, len(arr), 2):
                winners.append(min(arr[i], arr[i + 1]))

        depth -= 1
        minimax(winners, depth)
