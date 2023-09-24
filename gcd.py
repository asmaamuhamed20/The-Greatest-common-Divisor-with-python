#program to find GCD (recursive)
from typing import List

#method to calculate gcd 
def gcd_two_numbers(number1: int, number2: int) -> int:
    while number2:
        number1, number2 = number2, number1 % number2
    return number1

#method to handle errors if there more or less than 2 numbers 
def gcd_numbers(numbers: List[int]) -> int:
    if len(numbers) < 2:
        raise ValueError("Enter at least two numbers to calculate their GCD.(two numbers are required! )")
    
    result = numbers[0]  #initialize result as 0
    for num in numbers[1:]:   #loop start iterate from index 2  
        result = gcd_two_numbers(result, num)
    
    return result

def get_numbers() -> List[int]:
    """
    Read a list of positive integers from the user,it will return the list.

    Returns:
        List[int]:list of two positive integers entered by the user.
    """
    while True:
        try:
            input_num = input("Enter two positive integers separated by spaces: ")
            numbers = [int(x) for x in input_num.split()]  #to update the list if the user entered more than 2 numbers 
            
            if not numbers:
                raise ValueError("No numbers entered,  Please enter two positive integers.") #i
            
            if any(num <= 0 for num in numbers):
                raise ValueError("All numbers must be positive integers.")
            
            return numbers
        except ValueError as e:           #if the user input any value except integer
            print(f"Invalid input: {e}. Please try again.")
try:
    numbers = get_numbers()
    result = gcd_numbers(numbers)
    print(f"The GCD of the numbers {numbers} is {result}.")
except ValueError as e:
    print(f"Error: {e}") #handling errors 
           
