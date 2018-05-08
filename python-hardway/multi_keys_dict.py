# Create a multiples key same value in dictionary

# Download multi_key_dict from https://pypi.python.org/pypi/multi_key_dict#downloads
# Go through normal install process

# OR

# run in cmd: "python -m pip install -U pip"

from multi_key_dict import multi_key_dict

me = multi_key_dict()
me['Tuyen', 'Li', 'Amie', 'Yumie'] = 'ME!'

print('This is' , me[input('Enter my name >> ')])