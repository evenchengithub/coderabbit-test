# test_simple_utils.py - Comprehensive unit tests for simple_utils
import unittest
from simple_utils import reverse_string, count_words, celsius_to_fahrenheit


class TestReverseString(unittest.TestCase):
    """Test cases for the reverse_string function."""
    
    def test_reverse_simple_string(self):
        """Test reversing a simple word."""
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(reverse_string(""), "")
    
    def test_reverse_single_character(self):
        """Test reversing a single character."""
        self.assertEqual(reverse_string("a"), "a")
    
    def test_reverse_palindrome(self):
        """Test reversing a palindrome returns the same string."""
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("noon"), "noon")
    
    def test_reverse_with_spaces(self):
        """Test reversing a string with spaces."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
    
    def test_reverse_with_special_characters(self):
        """Test reversing strings with special characters."""
        self.assertEqual(reverse_string("hello!"), "!olleh")
        self.assertEqual(reverse_string("@#$%"), "%$#@")
    
    def test_reverse_with_numbers(self):
        """Test reversing strings containing numbers."""
        self.assertEqual(reverse_string("abc123"), "321cba")
    
    def test_reverse_unicode_characters(self):
        """Test reversing strings with unicode characters."""
        self.assertEqual(reverse_string("hello 🌍"), "🌍 olleh")
        self.assertEqual(reverse_string("café"), "éfac")
    
    def test_reverse_multiline_string(self):
        """Test reversing a multiline string."""
        self.assertEqual(reverse_string("line1\nline2"), "2enil\n1enil")
    
    def test_reverse_string_with_tabs(self):
        """Test reversing strings with tabs."""
        self.assertEqual(reverse_string("hello\tworld"), "dlrow\tolleh")
    
    def test_reverse_very_long_string(self):
        """Test reversing a very long string."""
        long_string = "a" * 10000
        self.assertEqual(reverse_string(long_string), long_string)
        
        varied_string = "abcdefgh" * 1000
        expected = "hgfedcba" * 1000
        self.assertEqual(reverse_string(varied_string), expected)


class TestCountWords(unittest.TestCase):
    """Test cases for the count_words function."""
    
    def test_count_single_word(self):
        """Test counting a single word."""
        self.assertEqual(count_words("hello"), 1)
    
    def test_count_multiple_words(self):
        """Test counting multiple words separated by single spaces."""
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words("one two three"), 3)
    
    def test_count_empty_string(self):
        """Test counting words in an empty string."""
        self.assertEqual(count_words(""), 1)  # split() on empty string returns ['']
    
    def test_count_whitespace_only(self):
        """Test counting words in strings with only whitespace."""
        self.assertEqual(count_words(" "), 1)
        self.assertEqual(count_words("   "), 1)
        self.assertEqual(count_words("\t"), 1)
    
    def test_count_multiple_spaces_between_words(self):
        """Test counting words with multiple spaces between them."""
        self.assertEqual(count_words("hello  world"), 2)
        self.assertEqual(count_words("one   two    three"), 3)
    
    def test_count_leading_trailing_spaces(self):
        """Test counting words with leading and trailing spaces."""
        self.assertEqual(count_words(" hello"), 2)  # split() counts empty strings
        self.assertEqual(count_words("hello "), 2)
        self.assertEqual(count_words("  hello  "), 3)
    
    def test_count_newlines_and_tabs(self):
        """Test counting words separated by newlines and tabs."""
        self.assertEqual(count_words("hello\nworld"), 1)  # split() only splits on spaces by default
        self.assertEqual(count_words("hello\tworld"), 1)
    
    def test_count_punctuation(self):
        """Test counting words with punctuation."""
        self.assertEqual(count_words("hello, world!"), 2)
        self.assertEqual(count_words("it's working"), 2)
    
    def test_count_numbers(self):
        """Test counting numeric strings."""
        self.assertEqual(count_words("123 456"), 2)
        self.assertEqual(count_words("one 2 three"), 3)
    
    def test_count_mixed_content(self):
        """Test counting words in mixed content sentences."""
        self.assertEqual(count_words("Hello, World! How are you?"), 5)
    
    def test_count_very_long_sentence(self):
        """Test counting words in a very long sentence."""
        long_sentence = " ".join(["word"] * 1000)
        self.assertEqual(count_words(long_sentence), 1000)
    
    def test_count_special_characters_only(self):
        """Test counting special character 'words'."""
        self.assertEqual(count_words("@#$"), 1)
        self.assertEqual(count_words("!!! ???"), 2)


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Test cases for the celsius_to_fahrenheit function."""
    
    def test_freezing_point(self):
        """Test conversion at water's freezing point."""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
    
    def test_boiling_point(self):
        """Test conversion at water's boiling point."""
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
    
    def test_negative_temperature(self):
        """Test conversion of negative temperatures."""
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67, places=2)
    
    def test_positive_temperature(self):
        """Test conversion of positive temperatures."""
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77.0, places=1)
    
    def test_room_temperature(self):
        """Test conversion of room temperature."""
        self.assertAlmostEqual(celsius_to_fahrenheit(20), 68.0, places=1)
    
    def test_zero_fahrenheit_equivalent(self):
        """Test temperature that converts to approximately 0°F."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-17.78), 0.004, places=1)
    
    def test_very_high_temperature(self):
        """Test conversion of very high temperatures."""
        self.assertEqual(celsius_to_fahrenheit(1000), 1832.0)
    
    def test_very_low_temperature(self):
        """Test conversion of very low temperatures (near absolute zero)."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67, places=2)
    
    def test_decimal_temperatures(self):
        """Test conversion with decimal values."""
        self.assertAlmostEqual(celsius_to_fahrenheit(36.5), 97.7, places=1)
        self.assertAlmostEqual(celsius_to_fahrenheit(22.5), 72.5, places=1)
    
    def test_small_increments(self):
        """Test conversion with small temperature increments."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0.5), 32.9, places=1)
        self.assertAlmostEqual(celsius_to_fahrenheit(1.0), 33.8, places=1)
    
    def test_formula_accuracy(self):
        """Test the mathematical accuracy of the conversion formula."""
        # Test several known conversions
        test_cases = [
            (0, 32),
            (10, 50),
            (20, 68),
            (30, 86),
            (40, 104),
            (50, 122),
        ]
        for celsius, expected_fahrenheit in test_cases:
            self.assertEqual(celsius_to_fahrenheit(celsius), expected_fahrenheit)
    
    def test_return_type_is_float(self):
        """Test that the function returns a float."""
        result = celsius_to_fahrenheit(25)
        self.assertIsInstance(result, float)
    
    def test_extreme_negative(self):
        """Test conversion with extreme negative values."""
        result = celsius_to_fahrenheit(-1000)
        self.assertAlmostEqual(result, -1768.0, places=1)
    
    def test_extreme_positive(self):
        """Test conversion with extreme positive values."""
        result = celsius_to_fahrenheit(10000)
        self.assertAlmostEqual(result, 18032.0, places=1)


class TestIntegrationScenarios(unittest.TestCase):
    """Integration tests combining multiple utility functions."""
    
    def test_reverse_then_count(self):
        """Test reversing a string then counting its words."""
        text = "hello world"
        reversed_text = reverse_string(text)
        word_count = count_words(reversed_text)
        self.assertEqual(word_count, 2)
    
    def test_temperature_string_manipulation(self):
        """Test converting temperature value to string and reversing."""
        fahrenheit = celsius_to_fahrenheit(25)
        temp_string = str(fahrenheit)
        reversed_temp = reverse_string(temp_string)
        self.assertEqual(reversed_temp, "0.77"[::-1])
    
    def test_count_words_in_temperature_description(self):
        """Test counting words in a temperature description."""
        description = "The temperature is {} degrees".format(celsius_to_fahrenheit(20))
        word_count = count_words(description)
        self.assertEqual(word_count, 5)


class TestEdgeCasesAndErrorHandling(unittest.TestCase):
    """Test edge cases and potential error conditions."""
    
    def test_reverse_string_type_handling(self):
        """Test that reverse_string handles different input types."""
        # These will raise AttributeError if not strings
        with self.assertRaises(AttributeError):
            reverse_string(123)
        
        with self.assertRaises(AttributeError):
            reverse_string(None)
    
    def test_count_words_type_handling(self):
        """Test that count_words handles different input types."""
        # These will raise AttributeError if not strings
        with self.assertRaises(AttributeError):
            count_words(123)
        
        with self.assertRaises(AttributeError):
            count_words(None)
    
    def test_celsius_to_fahrenheit_type_handling(self):
        """Test celsius_to_fahrenheit with non-numeric inputs."""
        # These should raise TypeError
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("25")
        
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit(None)
    
    def test_function_immutability(self):
        """Test that functions don't modify their inputs."""
        original = "test"
        reverse_string(original)
        self.assertEqual(original, "test")
        
        original_sentence = "hello world"
        count_words(original_sentence)
        self.assertEqual(original_sentence, "hello world")


if __name__ == '__main__':
    unittest.main()