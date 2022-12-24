# create a string
amount1 = u"₹50"
amount2 = u"$200"
print('Default string1: ', amount1, '\n', 'Type of string', type(amount1), '\n')
print('Default string2: ', amount2, '\n', 'Type of string', type(amount2), '\n')

print("=========================================")

# encode to UTF-8 byte format
amount_encoded1 = amount1.encode('utf-8')
amount_encoded2 = amount2.encode('utf-8')
amount_encoded3 = amount2.encode('utf-16')
print('Encoded to UTF-8 for string1: ', amount_encoded1, '\n', 'Type of string', type(amount_encoded1), '\n')
print('Encoded to UTF-8 for string2 with UTF-8: ', amount_encoded2, '\n', 'Type of string', type(amount_encoded2), '\n')
print('Encoded to UTF-8 for string2 with UTF-16: ', amount_encoded3, '\n', 'Type of string', type(amount_encoded3), '\n')

print("=========================================")

# sometime later in another computer...
# decode from UTF-8 byte format
amount_decoded1 = amount_encoded1.decode('utf-8')
amount_decoded2 = amount_encoded2.decode('utf-8')
amount_decoded3 = amount_encoded3.decode('utf-16')
print('Decoded from UTF-8 for string1: ', amount_decoded1, '\n', 'Type of string', type(amount_decoded1), '\n')
print('Decoded from UTF-8 for string2 with UTF-8: ', amount_decoded2, '\n', 'Type of string', type(amount_decoded2), '\n')
print('Decoded from UTF-8 for string2 with UTF-16: ', amount_decoded3, '\n', 'Type of string', type(amount_decoded3), '\n')