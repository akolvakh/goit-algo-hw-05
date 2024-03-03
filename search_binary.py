def search_binary(arr, item):
    low = 0
    high = len(arr) - 1
    num_of_iterations = 0
    boundary = None
    while low <= high:
        num_of_iterations += 1
        mid = (low + high) // 2
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1
            boundary = arr[high + 1]
        else:
            boundary = arr[mid]
            break
    return f"Кількість ітерацій: {num_of_iterations}", f"Межа: {boundary}"

if __name__ == "__main__":
    dataset = [
        72.4,
        42.2,
        11.4,
        8.1,
        9.4,
        9.99,
        2.1,
        5.03,
        6.1,
        14.14,
        4.2
    ]
    print(search_binary(sorted(dataset), 11.12))
    print(search_binary(sorted(dataset), 1.89))
    print(search_binary(sorted(dataset), 40.99))
    assert isinstance(search_binary(dataset, 11.12), tuple)
    