# Write a program to input a number and print the sum of the even digits and product of the odd digits.
def sum_and_product_of_digits(number):

    sum_of_even = 0
    product_of_odd = 1
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            sum_of_even += digit
        else:
            product_of_odd *= digit
        number //= 10

    return sum_of_even, product_of_odd


number = int(input("Enter a number: "))

sum_even, product_odd = sum_and_product_of_digits(number)
print("Sum of even digits:", sum_even)
print("Product of odd digits:", product_odd)
