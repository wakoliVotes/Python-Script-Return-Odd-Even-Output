# For this program, given a list of integers, determine whether the sum of its elements is even or odd
# The output needs to be a string, either "odd" or "even"
number1 = input ("Enter One number : ")
number2 = input ("Enter Second number : ")
sumOfNumbers = number1 + number2
if float (sumOfNumbers)%2 == 0:
    print("Even")
else:
    print("Odd, with a sum of " + sumOfNumbers + " and remainder of ", (float(sumOfNumbers)%2))