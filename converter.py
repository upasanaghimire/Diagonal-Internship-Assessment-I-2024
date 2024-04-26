def number_to_words(number):
    # Define a dictionary mapping numbers to their word representations
    num_words = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
        10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
        14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
        18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty',
        40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
        80: 'Eighty', 90: 'Ninety'
    }

    # Check if the number is less than or equal to 20
    if number <= 20:
        return num_words[number]  # Return the word representation from the dictionary

    # Check if the number is less than 100
    elif number < 100:
        # Decompose the number into tens and units
        tens = number // 10 * 10
        units = number % 10
        return num_words[tens] + '-' + num_words[units]  # Return the combined word representation

    # If the number is out of range
    else:
        return 'Number out of range'  # Return a message indicating that the number is out of range


# Test the function
number = int(input("Enter a number: "))
print("Word representation:", number_to_words(number))
