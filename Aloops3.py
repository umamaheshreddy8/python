#13.	Write a program to find the factorial of a large number using the concept of big integers.
#In the context of programming, "big integers" refer to the capability of handling integers that are larger than the maximum representable value of a standard integer data type. In many programming languages, integers are stored using a fixed number of bits, and there is a limit to the maximum value that can be represented. When dealing with very large numbers, such as factorials of large numbers, the result might exceed the maximum representable value, causing overflow issues.
#To handle large integers, you need to use libraries or data types that support arbitrary-precision arithmetic. Python, for example, has a built-in library called math that provides a factorial function, and it can handle large integers automatically. Here's an example:
import math

# Enter the number for which you want to find the factorial
num = int(input("Enter a number: "))

# Calculate the factorial using the math library
result = math.factorial(num)

# Print the result
print(f"The factorial of {num} is: {result}")
#In this example, the math.factorial function automatically handles the concept of big integers, allowing you to find the factorial of large numbers without worrying about overflow issues.
#If you were working in a language without built-in support for arbitrary-precision arithmetic, you might need to use external libraries or implement your own custom solution to handle large integers.




