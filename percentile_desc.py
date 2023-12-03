def calculate_percentile(dataset, value):
    def sort_array_descending(arr):
        sorted_arr = sorted(arr, reverse=True)
        return sorted_arr

    sorted_dataset = sort_array_descending(dataset)

    # print(sorted_dataset)
    n = len(sorted_dataset)

    rank = sorted_dataset.index(value)
    percentile = (rank / (n-1)) * 100

    return percentile

# Example usage:
dataset = [4,1, 10, 2, 1, 3, 4, 3, 8 ,5]
value =4

result = calculate_percentile(dataset, value)
print("The percentile of", value, "is:", result)
