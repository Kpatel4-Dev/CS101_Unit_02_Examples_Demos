'''
Formatting Strings With Python’s F-String:

The expressions that you embed in an f-string are evaluated at runtime. 

Then, Python formats the result using the .__format__() special method under the hood. 

This method supports the string formatting protocol. This protocol underpins both the .format() method, which you already saw in the notes, and the built-in format() function:
'''

print(format(5425.9292, ".2f"))
#'5425.93'

'''
The format() function takes a value and a format specifier as arguments. Then, it applies the specifier to the value to return a formatted value. The format specifier must follow the rules of the string formatting mini-language.

The f-string is a convenient way to embed expressions inside a string. It’s a shorter way 

Just like the .format() method, f-strings also support the string formatting mini-language. So, you can use format specifiers in your f-strings too:
'''
balance = 5425.9292
print(f"Balance: ${balance:.2f}")
#'Balance: $5425.93'

heading = "Centered string"
print(f"\n{heading:=^30}")
#'Centered string'

'''
        =======Centered string========
Note that the format specifiers in these examples are the same ones that you used in the section on .format(). 

In this case, the embedded expression comes before the format specifier, which always starts with a colon. This syntax makes the string literals readable and concise.
'''
#------------------------------------------------------

'''
You can create a wide variety of format specifiers. 

Some common formats include currencies, dates, and the representation of numeric values. 

Consider the following examples of string formatting:

'''
integer = -1234567
print(f"\nComma as thousand separators: {integer:,}")
#'Comma as thousand separators: -1,234,567'

sep = "_"
print(f"User's thousand separators: {integer:{sep}}")
#'User's thousand separators: -1_234_567'

floating_point = 1234567.9876
print(f"Comma as thousand separators and two decimals: {floating_point:,.2f}")
#'Comma as thousand separators and two decimals: 1,234,567.99'

date = (9, 6, 2023)
print(f"Date: {date[0]:02}-{date[1]:02}-{date[2]}")
#'Date: 09-06-2023'

#importing modules/package from outside of you main file.
from datetime import datetime
date = datetime(2023, 9, 26)
print(f"Date: {date:%m/%d/%Y}")
#'Date: 09/26/2023'

'''
These examples show how flexible the format specifiers can be. You can use them to create almost any string format. 

Note how in the second example, you’ve used curly brackets to embed variables or expressions in your format specifiers. This possibility allows you to create dynamic specifiers, which is pretty cool. In the last example, you format a datetime which can be formatted with special date format specifiers.
'''
