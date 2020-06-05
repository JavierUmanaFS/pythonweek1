from room import Room
from player import Player
from item import Item

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

items = {
    "sword": Item("sword", "attack!"),
    "torch": Item("torch", "see the path")
}

room['outside'].items.append("sword")
room['foyer'].items.append("torch")

def move(player, direction):
    attribute = direction + '_to'

    if hasattr(player.current_room, attribute):
        player.current_room = getattr(player.current_room, attribute)
        print(f"You've entered the {player.current_room}")

    else:
        print("There's nothing in that direction!")



startingPoint = room['outside']
inventory = []

player_name = ''

player = Player(player_name, startingPoint, inventory)

playGame = input("Please press yes (y) to continue or (q) to quit:")

if playGame.lower().strip() == "y":
    player_name = input("Enter player name to continue:")
    print(f"Welcome to the Treasure Hunt! You are currently {player.current_room}")
    while True:
        
        if player.current_room.name == room['outside'].name:
            pickup = input(f"This room has items available {room['outside'].items[0]} press (g) to grab: ")
            print(f"inventory{player.inventory()}")

            if pickup.lower().strip() == "g":
                try:
                    player.pick_up_item([i for i in room['outside'].items])
                except:
                    print("Nothing to grab")
        
        
        userInput = input("(n) to move north, (s) to move back, \n (e) to move east, (w) to move west: ").lower().strip()

        if userInput == 'q':
            break
    
        elif userInput == 'n':
            move(player, userInput)

        elif userInput == 's':
            move(player, userInput)
  
        elif userInput == 'e':
            move(player, userInput)

        elif userInput == 'w':
            move(player, userInput)

elif playGame.lower().strip() == "q":
    print("Exiting game.....")
    exit(0)

