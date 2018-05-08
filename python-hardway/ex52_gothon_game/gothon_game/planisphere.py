class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed 
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow up the ship after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a
Gothon jumps out, red scary skin, dark grimy teeth, and evil clown
costume flowing around his hate filled body. He's blocking the door to 
the Armory and about to pull a weapon to blast you.
""")


laser_weapon_armory = Room("Laser Weapon Armory",
"""
You tell the one Gothon joke you know: Lbhe zbgure vf bf sng, 
jura fur fvgf nebhaq gur ubhfr. The Gothon stops, tries not to laugh, 
then busts out laughing and can't move. You shout him while he's laughing.

You do a dive roll into the Weapon Armory, crouch and scan the room for
more Gothons that might be hiding. It's dead quite. You stand up and run
to the far side of the room and find the neutron bomb. There's a keypad
lock on the box. You need the code to get the bomb.
You only have 10 attempts. It's 3 digits code.
""")


the_bridge = Room("The Bridge",
"""
You grab the neutron bomb and run to the bridge. You must place 
the bomb in the right spot.
""")


escape_pod = Room("Escape Pod",
"""
You placed the bomb in the correct spot. Now you're in the escape pod entrance.

There are 5 pods, which one do you take?
""")

the_end_winner = Room("The End",
"""
You choose pod 2. Correct. You won!
""")

the_end_loser = Room("The End",
"""
You chose the wrong pod. You loose!
""")

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died!")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '123': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot': generic_death,
    'dodge': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    """
    There is a potential security porblem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution thatn this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key