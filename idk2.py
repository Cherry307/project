
def counting_sort(arr):
    # Step 1: Find the range
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Step 2: Create count array
    count_arr = [0] * range_of_elements

    # Step 3: Count occurrences
    for num in arr:
        count_arr[num - min_val] += 1

    # Step 4: Cumulative count
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Step 5: Build output array
    output_arr = [0] * len(arr)
    for num in reversed(arr):
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1

    # Step 6: Copy to original array
    for i in range(len(arr)):
        arr[i] = output_arr[i]

    return arr

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
