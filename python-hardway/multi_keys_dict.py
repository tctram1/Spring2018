# Create a multiples key same value in dictionary

from multi_keys_dict import multi_key_dict

me = multi_key_dict()
me['Tuyen', 'Li', 'Amie', 'Yumie'] = 'ME'

print('This is' , me[input('Enter my name >> ')])