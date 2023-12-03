def calculate_percentile(dataset, value):
    sorted_dataset = sorted(dataset)
    # print(sorted_dataset)
    n = len(sorted_dataset)

    rank = sorted_dataset.index(value)
    if value == 100:
        return 100
    else:
        percentile = (rank / (n - 1)) * 100

    return percentile


# Example usage:
dataset = [60, 60, 64, 67, 80, 100, 71, 25, 50, 100 ]
value = int(input("enter number: "))

result = calculate_percentile(dataset, value)
print("The percentile of", value, "is:", result)

