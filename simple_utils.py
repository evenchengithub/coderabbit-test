# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Return the input string with characters in reverse order.
    
    Parameters:
        text (str): String to reverse.
    
    Returns:
        str: Reversed string.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the number of words in a sentence.
    
    Parameters:
        sentence (str): Input string whose words are separated by whitespace.
    
    Returns:
        int: Number of whitespace-separated words in the input sentence.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32