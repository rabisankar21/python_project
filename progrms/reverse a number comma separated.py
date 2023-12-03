#write a program to input a number and print the digits separated by comma(,) in reverse order
def reverse_digits_with_commas(number):
    digits = str(number)
    reversed_digits = ""
    index = len(digits) - 1

    while index >= 0:
        reversed_digits += digits[index]
        if index > 0:
            reversed_digits += ","
        index -= 1

    return reversed_digits


number = int(input("Enter a number: "))

result = reverse_digits_with_commas(number)
print("Digits in reverse order with commas:", result)
