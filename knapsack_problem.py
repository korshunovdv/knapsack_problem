def knapsack_problen(weights, costs, capacity):    
    arr = []
    for i in range(len(weights) + 1):
        row = []
        for j in range(capacity + 1):
            row.append(0)
        arr.append(row)

    for i in range(1, len(weights) + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                arr[i][j] = arr[i - 1][j]
            else:
                if arr[i - 1][j] > arr[i - 1][j - weights[i - 1]] + costs[i - 1]:
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = arr[i - 1][j - weights[i - 1]] + costs[i - 1]

    i = len(weights)
    j = capacity
    indx = []
    while i > 0 and j > 0:
        if arr[i][j] == arr[i - 1][j]:
            i -= 1
        else:
            indx.append(i - 1)
            j -= weights[i - 1]
            i -= 1
    print('Max cost is ', arr[len(weights)][capacity])
    print(f'It\'s {len(indx)} elements')
    print('It\'s indexes of elements', ' '.join(map(str,sorted(indx))))


if __name__ == '__main__':
    capacity = 10
    weights = [1, 2, 3, 5, 6]
    costs = [100, 300, 200, 600, 700]
    knapsack_problen(weights, costs, capacity)

