# Playing with dictionaries.

# First - a simple key-value dictionary
character_0 = {'name': "Susie Queue", 'location': "Boston"}
print (character_0['name'])
print (character_0['location'])

# add more key-value pairs
character_0['type'] = "protagonist"
character_0['hair color'] = "red"
print (character_0)

# Time to remember.
# lists have [ ] 
chapters = range(1, 20)

# tuples have ( )
character_types = ('protagonist', 'antagonist', 'sidekick')

# dictionaries have { }
character_locations = {
    'susie': 'Boston',
    'Frankie': "New York",
}
print (character_locations)

# using get()
print ( {character_locations.get('Carrie','no location')})

# Now loop thru all and see if the new location is listed
for key, value in character_locations.items():
    print (f"key {key}")
    print (f"value {value}")

# try adding a new k-v pair to the dictionary
character_locations['Carrie'] = 'Melrose'
for name in character_locations.keys():
    print (name.title())

# Now let's make a list of characer dictionaries
character_1 = {'name': 'Frank', 'location':'New York'}
character_2 = {'name': 'Carrie', 'location':'Melrose'}

characters = [character_0, character_1, character_2]

for character in characters:
    print (f"My character name is {character['name']} and location is {character['location']}")