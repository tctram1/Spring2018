# Create a mapping of state to abbreviation
states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Floria': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louissiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgina': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


# Create capital for each state
capitals = {
    'AL': 'Montgomery',
    'AK': 'Juneau',
    'AZ': 'Phoenix',
    'AR': 'Little Rock',
    'CA': 'Sacramento',
    'CO': 'Denver',
    'CT': 'Hartford',
    'DE': 'Dover',
    'FL': 'Tallahassee',
    'GA': 'Atlanta',
    'HI': 'Honolulu',
    'ID': 'Boise',
    'IL': 'Springfield',
    'IN': 'Indianapolis',
    'IA': 'Des Moines',
    'KS': 'Topeka',
    'KY': 'Frankfort',
    'LA': 'Baton Rouge',
    'ME': 'Augusta',
    'MD': 'Annapolis',
    'MA': 'Boston',
    'MI': 'Lansing',
    'MN': 'Saint Paul',
    'MS': 'Jackson',
    'MO': 'Jefferson City',
    'MT': 'Helena',
    'NE': 'Lincoln',
    'NV': 'Carson City',
    'NH': 'Concord',
    'NJ': 'Trenton',
    'NM': 'Santa Fe',
    'NY': 'Albany',
    'NC': 'Raleigh',
    'ND': 'Bismarck',
    'OH': 'Columbus',
    'OK': 'Oklahoma City',
    'OR': 'Salem',
    'PA': 'Harrisburg',
    'RI': 'Providence',
    'SC': 'Columbia',
    'SD': 'Pierre',
    'TN': 'Nashville',
    'TX': 'Austin',
    'UT': 'Salt Lake City',
    'VT': 'Montpelier',
    'VA': 'Richmand',
    'WA': 'Olympia',
    'WV': 'Charleston',
    'WI': 'Madison',
    'WY': 'Cheyenne'
}


print("\nDICTIONARY")
print("\n1) Look Up State Abbreviations \n2) Look Up Capital in State")
print("\nEXAMPLE")
choice = input('Choose Option >> ' )
#print(input('Choose Option >> ' ))

if choice == '1':
    state = input('Choose a state >> ')
    if state in states:
        print('The abbreviation is >>' , states[state])
    else:
        print('The state is unvalid!')
elif choice == '2':
    capital = input('Enter the state abbreviation >> ')
    if capital in capitals:
        print('The capital is >>' , capitals[capital])
    else:
        print('The state abbreviation is unvalid!')
else:
    print("I don't know what you're talking about! \n")