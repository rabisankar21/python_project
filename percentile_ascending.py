def calculate_percentile(dataset, value):
    sorted_dataset = sorted(dataset)
    # print(sorted_dataset)
    n = len(sorted_dataset)

    rank = sorted_dataset.index(value)
    percentile = (rank / (n-1)) * 100

    return percentile

# Example usage:
dataset = [100,100,100,95,91]
value = 95

result = calculate_percentile(dataset, value)
print("The percentile of", value, "is:", result)
print(add)
print("The percentile of", value, "is:", result)
