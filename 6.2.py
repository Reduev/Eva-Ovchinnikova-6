def is_palindrome(text: str) -> bool:
    """
    Проверяет, является ли строка палиндромом (игнорирует регистр, пробелы, знаки препинания).
    """
    cleaned = ''.join(char.lower() for char in text if char.isalpha())
    return cleaned == cleaned[::-1]

print("assert is_palindrome(\"Лёша на полке клопа нашёл\") == True")
assert is_palindrome("Лёша на полке клопа нашёл") == True

print("assert is_palindrome(\"А роза упала на лапу Азора\") == True")
assert is_palindrome("А роза упала на лапу Азора") == True

print("assert is_palindrome(\"Madam\") == True")
assert is_palindrome("Madam") == True

print("assert is_palindrome(\"Hello, world!\") == False")
assert is_palindrome("Hello, world!") == False

print("assert is_palindrome(\"12321\") == True")
assert is_palindrome("12321") == True

