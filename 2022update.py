import random
import string

def charactercreation():
    global strx, dexx, conx, intx, wisx, chax, strmodif, dexmodif, conmodif, intmodif, wismodif, chamodif
    global cname, cgender, crace, cclass, armorchoice, weaponchoice, ac, hitpoints

    # Generate random attribute scores
    STR = [random.randint(1, 6) for _ in range(4)]
    DEX = [random.randint(1, 6) for _ in range(4)]
    CON = [random.randint(1, 6) for _ in range(4)]
    INT = [random.randint(1, 6) for _ in range(4)]
    WIS = [random.randint(1, 6) for _ in range(4)]
    CHA = [random.randint(1, 6) for _ in range(4)]
    strx = sum(STR) - min(STR)
    dexx = sum(DEX) - min(DEX)
    conx = sum(CON) - min(CON)
    intx = sum(INT) - min(INT)
    wisx = sum(WIS) - min(WIS)
    chax = sum(CHA) - min(CHA)

    # Prompt user for name and gender
    cname = input("What is your name?\n")
    cname = string.capwords(cname)
    cgender = input("Are you a Male or Female\n")
    cgender = string.capwords(cgender)

    # Prompt user for race and handle invalid input
    choosingrace = True
    while choosingrace:
        characterrace = input("Choose a race:\nOrc\nHuman\nElf\nHalfling\nMind Flayer\nNord\nHalf Elf"
                              "\nHalf Orc\nDwarf\n")
        crace = string.capwords(characterrace)
        if crace in ["Orc", "Human", "Elf", "Halfling", "Mind Flayer", "Nord", "Half Elf", "Half Orc", "Dwarf"]:
            choosingrace = False
        else:
            print("Invalid race. Please try again.")

    # Prompt user for class and handle invalid input
    choosingclass = True
    while choosingclass:
        characterclass = input("Choose a class:\nRogue\nFighter\nWizard\nSorcerer\nMonk\nBarbarian\n")
        cclass = string.capwords(characterclass)
        if cclass in ["Rogue", "Fighter", "Wizard", "Sorcerer", "Monk", "Barbarian"]:
            choosingclass = False
        else:
            print("Invalid class. Please try again.")

    # Assign armor and weapons based on class
    if cclass == "Rogue":
        armorchoice = "Leather Armor"
    elif cclass == "Fighter":
        armor = input("Choose your armor.\nChain Mail\nLeather Armor\n")
        armorchoice = string.capwords(armor)
    else:
        armorchoice = "None"

    # Assign attribute bonuses based on race
    if crace == "Orc":
        strx += 2
        conx += 1
    elif crace == "Human":
        strx += 1
        dexx += 1
        conx += 1
        intx += 1
        wisx += 1
        chax += 1
    elif crace == "Elf":
        intx += 2
        chax += 1
    elif crace == "Halfling":
        dexx += 2
        wisx += 1
    elif crace == "Mind Flayer":
        intx += 2
        wisx += 1
    elif crace == "Nord":
        strx += 2
        conx += 1
    elif crace == "Half-elf":
        dexx += 2
        chax += 1
    elif crace == "Half-orc":
        strx += 2
        conx += 1
    elif crace == "Dwarf":
        conx += 2
        wisx += 1

    # Calculate hit points and armor class
    if cclass == "Rogue":
        hitpoints = 8 + conx
        if armorchoice == "Leather Armor":
            ac = 14 + dexx
        else:
            ac = 10 + dexx
    elif cclass == "Fighter":
        hitpoints = 10 + conx
        if armorchoice == "Chain Mail":
            ac = 16 + dexx
        else:
            ac = 12 + dexx
    elif cclass in ["Wizard", "Sorcerer"]:
        hitpoints = 6 + conx
        ac = 10 + dexx
    elif cclass == "Monk":
        hitpoints = 8 + conx
        ac = 10 + dexx
    elif cclass == "Barbarian":
        hitpoints = 12 + conx
        if armorchoice == "Chain Mail":
            ac = 16 + dexx
        elif armorchoice == "Leather Armor":
            ac = 12 + dexx
        else:
            ac = 10 + dexx

    # Print character summary
    print(f"Name: {cname}")
    print(f"Gender: {cgender}")
    print(f"Race: {crace}")
    print(f"Class: {cclass}")
    print(f"Armor: {armorchoice}")
    print(f"Hit Points: {hitpoints}")
    print(f"Armor Class: {ac}")

# Welcome screen
def welcome_screen():
  print("Welcome to the text-based adventure game!")
  print("Type 'start' to begin or 'quit' to quit")
  user_input = input()
  if user_input == 'start':
    start_game()
  elif user_input == 'quit':
    quit_game()
  else:
    print("Invalid input. Please try again.")
    welcome_screen()

# Start game
def start_game():
  print("You are about to embark on a grand adventure. Before we begin, let's create your character.")
  charactercreation()
  print("Your character has been created! Let's begin your journey.")
  map_screen()

# Map screen
def map_screen():
  print("You find yourself in a wide open field. You can see a forest to the north, a town to the east, a dungeon to the south, and a lake to the west.")
  print("Type 'north' to go to the forest, 'east' to go to the town, 'south' to go to the dungeon, or 'west' to go to the lake.")
  user_input = input()
  if user_input == 'north':
    forest()
  elif user_input == 'east':
    town()
  elif user_input == 'south':
    dungeon()
  elif user_input == 'west':
    lake()
  else:
    print("Invalid input. Please try again.")
    map_screen()

# Forest
def forest():
  print("You have entered the forest. You can see a path leading north, east, south, and west.")
  print("Type 'north' to go north, 'east' to go east, 'south' to go south, or 'west' to go west.")
  user_input = input()
  if user_input == 'north':
    north_forest()
  elif user_input == 'east':
    east_forest()
  elif user_input == 'south':
    south_forest()
  elif user_input == 'west':
    west_forest()
  else:
    print("Invalid input. Please try again.")
    forest()

# North forest
def north_forest():
  print("You have reached the northern part of the forest. You can see a path leading east, south, and west.")
  print("Type 'east' to go east, 'south' to go south, or 'west' to go west.")
  user_input = input()
  if user_input == 'east':
    east_forest()
  elif user_input == 'south':
    south_forest()
  elif user_input == 'west':
    west_forest()
  else:
    print("Invalid input. Please try again.")
    north_forest()

# East forest
def east_forest():
  print("You have reached the eastern part of the forest. You can see a path leading north, south, and west.")
  print("Type 'north' to go north, 'south' to go south, or 'west' to go west.")
  user_input = input()
  if user_input == 'north':
    north_forest()
  elif user_input == 'south':
    south_forest()
  elif user_input == 'west':
    west_forest()
  else:
    print("Invalid input. Please try again.")
    east_forest()

# South forest
def south_forest():
  print("You have reached the southern part of the forest. You can see a path leading north, east, and west.")
  print("Type 'north' to go north, 'east' to go east, or 'west' to go west.")
  user_input = input()
  if user_input == 'north':
    north_forest()
  elif user_input == 'east':
    east_forest()
  elif user_input == 'west':
    west_forest()
  else:
    print("Invalid input. Please try again.")
    south_forest()

# West forest
def west_forest():
  print("You have reached the western part of the forest. You can see a path leading north, east, and south.")
  print("Type 'north' to go north, 'east' to go east, or 'south' to go south.")
  user_input = input()
  if user_input == 'north':
    north_forest()
  elif user_input == 'east':
    east_forest()
  elif user_input == 'south':
    south_forest()
  else:
    print("Invalid input. Please try again.")
    west_forest()

# Town
def town():
  print("You have arrived at the town. You can see a store to the north, a blacksmith to the east, a tavern to the south, and a stable to the west.")
  print("Type 'north' to go to the store, 'east' to go to the blacksmith, 'south' to go to the tavern, or 'west' to go to the stable.")
  user_input = input()
  if user_input == 'north':
    store()
  elif user_input == 'east':
    blacksmith()
  elif user_input == 'south':
    tavern()
  elif user_input == 'west':
    stable()
  else:
    print("Invalid input. Please try again.")
    town()

# Store
def store():
  print("You have entered the store. You can buy items, check your inventory, or exit the store.")
  print("Type 'buy' to buy items, 'inventory' to check your inventory, or 'exit' to exit the store.")
  user_input = input()
  if user_input == 'buy':
    buy_items()
  elif user_input == 'inventory':
    check_inventory()
  elif user_input == 'exit':
    town()
  else:
    print("Invalid input. Please try again.")
    store()

# Buy items
def buy_items():
  print("You can buy a sword, armor, a horse, or food.")
  print("Type 'sword' to buy a sword, 'armor' to buy armor, 'horse' to buy a horse, or 'food' to buy food.")
  user_input = input()
  if user_input == 'sword':
    buy_sword()
  elif user_input == 'armor':
    buy_armor()
  elif user_input == 'horse':
    buy_horse()
  elif user_input == 'food':
    buy_food()
  else:
    print("Invalid input. Please try again.")
    buy_items()

# Buy sword
def buy_sword():
  print("You have bought a sword. You can equip it or put it in your inventory.")
  print("Type 'equip' to equip the sword or 'inventory' to put it in your inventory.")
  user_input = input()
  if user_input == 'equip':
    equip_sword()
  elif user_input == 'inventory':
    put_in_inventory()
  else:
    print("Invalid input. Please try again.")
    buy_sword()

# Equip sword
def equip_sword():
  print("You have equipped the sword. Your attack has increased.")
  store()

# Put in inventory
def put_in_inventory():
  print("You have put the sword in your inventory.")
  store()

# Buy armor
def buy_armor():
  print("You have bought armor. You can equip it or put it in your inventory.")
  print("Type 'equip' to equip the armor or 'inventory' to put it in your inventory.")
  user_input = input()
  if user_input == 'equip':
    equip_armor()
  elif user_input == 'inventory':
    put_in_inventory()
  else:
    print("Invalid input. Please try again.")
    buy_armor()

# Equip armor
def equip_armor():
  print("You have equipped the armor. Your armor class has increased.")
  store()

# Put in inventory
def put_in_inventory():
  print("You have put the armor in your inventory.")
  store()

# Buy horse
def buy_horse():
  print("You have bought a horse. You can mount it or put it in your inventory.")
  print("Type 'mount' to mount the horse or 'inventory' to put it in your inventory.")
  user_input = input()
  if user_input == 'mount':
    mount_horse()
  elif user_input == 'inventory':
    put_in_inventory()
  else:
    print("Invalid input. Please try again.")
    buy_horse()

# Mount horse
def mount_horse():
  print("You have mounted the horse. Your speed has increased.")
  store()

# Put in inventory
def put_in_inventory():
  print("You have put the horse in your inventory.")
  store()

# Buy food
def buy_food():
  print("You have bought food. You can eat it or put it in your inventory.")
  print("Type 'eat' to eat the food or 'inventory' to put it in your inventory.")
  user_input = input()
  if user_input == 'eat':
    eat_food()
  elif user_input == 'inventory':
    put_in_inventory()
  else:
    print("Invalid input. Please try again.")
    buy_food()

# Eat food
def eat_food():
  print("You have eaten the food. Your health has increased.")
  store()

# Put in inventory
def put_in_inventory():
  print("You have put the food in your inventory.")
  store()

# Blacksmith
def blacksmith():
  print("You have entered the blacksmith. You can buy weapons, repair weapons, or exit the blacksmith.")
  print("Type 'buy' to buy weapons, 'repair' to repair weapons, or 'exit' to exit the blacksmith.")
  user_input = input()
  if user_input == 'buy':
    buy_weapons()
  elif user_input == 'repair':
    repair_weapons()
  elif user_input == 'exit':
    town()
  else:
    print("Invalid input. Please try again.")
    blacksmith()

# Buy weapons
def buy_weapons():
  print("You can buy a sword, a bow, or a spear.")
  print("Type 'sword' to buy a sword, 'bow' to buy a bow, or 'spear' to buy a spear.")
  user_input = input()
  if user_input == 'sword':
    buy_sword()
  elif user_input == 'bow':
    buy_bow()
  elif user_input == 'spear':
    buy_spear()
  else:
    print("Invalid input. Please try again.")
    buy_weapons()

# Buy sword
def buy_sword():
  print("You have bought a sword. You can equip it or put it in your inventory.")
  print("Type 'equip' to equip the sword or 'inventory' to put it in your inventory.")
  user_input = input()
  if user_input == 'equip':
    equip_sword()
  elif user_input == 'inventory':
    put_in_inventory()
  else:
    print("Invalid input. Please try again.")
    buy_sword()

# Buy bow
def buy_bow():
  print("You have bought a bow. You can equip it or put it in your inventory.")
  print("Type 'equip' to equip the bow or 'inventory' to put it in your inventory.")
  user_input = input()
  if user_input == 'equip':
    equip_bow()
  elif user_input == 'inventory':
    put_in_inventory()
  else:
    print("Invalid input. Please try again.")
    buy_bow()

# Equip bow
def equip_bow():
  print("You have equipped the bow. Your ranged attack has increased.")
  blacksmith()

# Put in inventory
def put_in_inventory():
  print("You have put the bow in your inventory.")
  blacksmith()

# Buy spear
def buy_spear():
  print("You have bought a spear. You can equip it or put it in your inventory.")
  print("Type 'equip' to equip the spear or 'inventory' to put it in your inventory.")
  user_input = input()
  if user_input == 'equip':
    equip_spear()
  elif user_input == 'inventory':
    put_in_inventory()
  else:
    print("Invalid input. Please try again.")
    buy_spear()

# Equip spear
def equip_spear():
  print("You have equipped the spear. Your melee attack has increased.")
  blacksmith()

# Put in inventory
def put_in_inventory():
  print("You have put the spear in your inventory.")
  blacksmith()

# Repair weapons
def repair_weapons():
  print("You can repair your sword, bow, or spear.")
  print("Type 'sword' to repair your sword, 'bow' to repair your bow, or 'spear' to repair your spear.")
  user_input = input()
  if user_input == 'sword':
    repair_sword()
  elif user_input == 'bow':
    repair_bow()
  elif user_input == 'spear':
    repair_spear()
  else:
    print("Invalid input. Please try again.")
    repair_weapons()

# Repair sword
def repair_sword():
  print("You have repaired your sword. Your attack has been restored.")
  blacksmith()

# Repair bow
def repair_bow():
  print("You have repaired your bow. Your ranged attack has been restored.")
  blacksmith()

# Repair spear
def repair_spear():
  print("You have repaired your spear. Your melee attack has been restored.")
  blacksmith()

# Tavern
def tavern():
  print("You have entered the tavern. You can buy food, check your player card, or exit the tavern.")
  print("Type 'buy' to buy food, 'player' to check your player card, or 'exit' to exit the tavern.")
  user_input = input()
  if user_input == 'buy':
    buy_food()
  elif user_input == 'player':
    check_player_card()
  elif user_input == 'exit':
    town()
  else:
    print("Invalid input. Please try again.")
    tavern()

# Check player card
def check_player_card():
  print("You can see your stats and inventory.")
  print("Type 'stats' to check your stats or 'inventory' to check your inventory.")
  user_input = input()
  if user_input == 'stats':
    check_stats()
  elif user_input == 'inventory':
    check_inventory()
  else:
    print("Invalid input. Please try again.")
    check_player_card()

# Check stats
def check_stats():
  print("You can see your health, attack, armor class, and speed.")
  tavern()

# Check inventory
def check_inventory():
  print("You can see your items and weapons.")
  tavern()
# Stable
def stable():
  print("You have entered the stable. You can buy a horse, feed a horse, or exit the stable.")
  print("Type 'buy' to buy a horse, 'feed' to feed a horse, or 'exit' to exit the stable.")
  user_input = input()
  if user_input == 'buy':
    buy_horse()
  elif user_input == 'feed':
    feed_horse()
  elif user_input == 'exit':
    town()
  else:
    print("Invalid input. Please try again.")
    stable()

# Feed horse
def feed_horse():
  print("You have fed your horse. Your horse is now fully healed.")
  stable()

# Start game
start_game()
