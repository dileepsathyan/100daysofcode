# String Formatting

# The format() method allows you to format selected parts of a string
# curly brackets {} in the text are used to add foreign values to a string using the format() method.

txt1 = 'I bought {} pair of shoes..'
num = 2
# print(txt1.format(num))



# To add multiple variables into a string, use the below method.

txt2 = 'I bought {} pieces of apples at the cost of {} rupees per kilo...'
qty = 10
cost = 100
# print(txt2.format(qty, cost))



# To place the right variables at the right place, use the indexes as below.

txt3 = 'I bought {0} cars at {1} rupees each but I had to sell them for {2} rupees after few years...'
quantity = 2
bought = '5 Lakhs'
sold = '4.5 Lakhs'
# print(txt3.format(quantity, bought, sold))

# The order of the variables you parse into the format method can be customised as per the indexes in the text string.
txt4 = 'I bought {2} cars at {0} rupees each but I had to sell them for {1} rupees after few years...'
# print(txt4.format(bought, sold, quantity))



# Explicit names in the variables to assign values
txt5 = 'I want to buy a {item} from {shop_name} for my {relation}'
print()



# Format the numbers in a string

txt6 = 'It costs {:.2f} dollars'
val = 12.3
print(txt6.format(val))
