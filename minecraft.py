from random import *
from math import *
from time import *

global templist
templist = []

def GMN(difficulty):
    difficulty = 10 ** difficulty
    tries = 0
    while True:
        computer = randint(1, difficulty)
        try:
            print("Choose a number, 1 to",difficulty,"\n")
            usernumber = int(input())
            tries += 1
        except ValueError:
            print('                ⠀⠀   ⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷\n⠀⠀⠀⢀⣠⣶⣾⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⠿⣷⣦⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿\n⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢀⣴⣿⣿⣿⡟⠁⠀⠀⠙⣻⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁\n⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⣠⣶⣿⣿⠏⠀⠙⠟⠀⠀⠀⠀⠑⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀\n⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡿⠋⣽⠋⠀⠀⢀⡀⠀⡀⠀⠀⠀⠀⠀⠈⢻⣿⣯⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀\n⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠⡞⠁⠀⠀⠀⣼⡟⠀⣿⣶⣶⣦⠀⠀⠀⠀⠙⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡟⠀⠈⠁⠀⢀⣶⡾⢿⣷⠀⢸⡟⠉⠙⣷⡀⠀⠀⠀⠹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠿⠛⠉⠀⢸⣿⠁⠀⠀⠀⢠⣾⠋⠀⢠⣿⠃⠸⣿⡀⠀⠘⣷⠀⠀⠀⠀⠹⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⣾⣇⣀⣤⣿⡿⢀⣠⣿⣿⣶⣴⣿⠀⠀⠀⠀⠀⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⠀⠀⠀⠀⢸⣿⠿⠿⣿⣿⣿⣿⣿⣿⣍⠉⠛⢷⣄⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡄⠀⠀⢰⡿⠋⠀⠸⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠙⠓⣤⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠚⠁⠀⠀⠀⠉⠛⠻⠟⠛⠉⠀⠀⠀⠀⠀⠀⠘⠻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣤⠀⠀⠀⠀⢀⣀⣀⣀⣠⣤⣤⣤⣴⣶⣶⣿⣿⣷⣶⣮⣿⡀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣏⣠⣶⣿⣿⡿⠟⠛⠉⠉⢉⡀⠄⠁⠉⢉⣉⡛⣿⢿⣷⣿⠇⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣵⣄⠀⠀⠀⠀⠀⠀⣀⣠⣴⣿⣿⡛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣯⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⡿⠋⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣻⠅⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⡿⠟⠋⠙⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⣟⣀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣦⡀⠀⠉⠀⣠⣴⣄⡀⠀⢸⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⣿⠂⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⠀⢠⣾⣿⣿⣿⣿⣄⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⢿⣦⡀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⡟⠀⢾⣿⣿⣿⣿⣿⣿⣾⢧⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⣽⠃⠀⠈⠁⠀⠀⠀⠀⠹⢿⣿⣿⡿⠟⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⡿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣽⡇⠀⠀⠀⠀⠀⠀⠀⠴⢦⣤⣀⠀⠀⠀⠀⣀⠀⠀⠩⠽⠿⠋⠁⠈⣿⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣽⡿⢶⣤⣄⣀⡀⠀⠀⠀⠀⠈⣽⣿⣿⡟⠛⠉⠁⠀⠀⠀⠀⣀⣤⣶⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⣾⣿⣿⣿⣿⠟⠷⠶⢶⣶⣿⠾⣿⣿⣤⣀⣤⣤⢶⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⠀⠀⢠⣿⣿⣿⣿⡟⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡁⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀\n⠀⢀⣾⠋⠀⣀⣤⣤⣤⣄⡀⠀⢸⣿⣿⣿⣿⣿⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⡷⠟⠋⠉⠉⠉⠛⠷⣮⡀⠀⠀⠀\n⠀⣾⣿⣿⡿⠛⠉⠉⠉⠉⠛⠷⣾⣿⣿⣿⣿⣿⠿⣿⣇⠀⠀⠀⠀⠀⠀⠀⣾⡿⠉⢿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⡀⠀\n⣸⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠿⠋⣠⣿⣿⣄⠀⠀⠀⠀⠀⢰⣿⣿⣤⣀⡙⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣧⡀\n⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣄⠈⠉⠈⢻⣿⡄⠀⠀⠀⠀⢸⡟⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇\n⠙⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣼⣿⡇⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⡇\n⠀⣼⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⢿⡿⠀⠀⠀⠀⠀⠀⠈⠻⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠏⠀⠀\n⠀⠘⠣⢟⣷⣤⣄⣀⠀⠀⠀⠀⢀⣀⣀⣤⣴⣾⣻⠗⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠳⠷⠶⠶⠶⠶⠿⠻⠟⠛⠁⠀⠀⠀\n⠀⠀⠀ ⠀⠁⠉⠉⠛⠛⠛⠛⠛⠛⠟⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀INVALID INPUT. TRY AGAIN.')
            continue
        while usernumber != computer:
            difference = abs(computer - usernumber)
            if usernumber > computer:
                if difference >= 0.25 * difficulty:
                    print("Way too high, guess again!")
                else:
                    print("Too high, guess again!")
            else:
                if difference >= 0.25 * difficulty:
                    print("Way too low, guess again!")
                else:
                    print("Too low, guess again!")

            try:
                print("Choose a number, 1 to",difficulty, "\n")
                usernumber = int(input())
                tries += 1
            except ValueError:
                print("Invalid input. Try again.")
                continue

        if usernumber == computer:
            print("You got it in",tries,"tries. \n(づ ￣ ³￣)づ")
            return tries

def word_jumble(difficulty):
    words = ["people", "should", "because", "through", "always", "without", "before", "another",
        "everyone", "everything", "together", "sometimes", "beautiful", "important", "something",
        "interesting", "wonderful", "everywhere", "afternoon", "tomorrow", "yesterday", "especially",
        "restaurant", "understand", "telephone", "exciting", "happiness", "knowledge", "language",
        "relationship", "university", "difficult", "chocolate", "ambitious", "adventure", "community",
        "celebrate", "attention", "experience", "imagination", "celebration", "discovery", "challenge",
        "passionate", "incredible", "mysterious", "fascinating", "curiosity", "independent", "extraordinary",
        "motivation", "appreciate", "grateful", "inspiration", "fantastic", "achievement", "communication",
        "wonderful", "knowledgeable", "opportunity", "development", "successful", "thoughtful",
        "understanding", "delicious", "comfortable", "entertainment", "spontaneous", "adventurous",
        "breathtaking", "organization", "efficiency", "satisfaction", "encourage", "integrity",
        "creativity", "relaxation", "curiosity", "enthusiasm", "congratulations", "information",
        "experience", "inspiration", "relationship", "encouragement", "excellent", "anything"]

    word = choice(words)
    jumbled_word = "".join(sample(word, len(word)))

    print("Guess the jumbled word:", jumbled_word)
    sleep(1)
    print("(You can guess 'hint' to get a \nhint, but it will cost you a try.)")

    guess = input("\nYour guess: ").lower()
    tries = 1
    num = 0

    while guess != word:
        if guess == "hint":
            num += difficulty
            hint = word[:num]
            print(f"These are the first {num} letters of your word: {hint}")
            tries += 1
        else:
            print("Oops! Incorrect guess. Try again.")
            tries += 1

        guess = input("Your guess: ")

    print("Congratulations! You guessed the correct word.")
    if tries >= 2:
        print("It took you,", str(tries) + "!")
    else:
        print("It only took you a single try!")

global inventory
inventory = []

global resources
resources = ['oak wood', 'oak planks', 'spruce wood',
    'spruce planks', 'birch wood', 'birch planks',
    'jungle wood', 'jungle planks', 'acacia wood',
    'acacia planks', 'dark oak wood', 'dark oak planks',
    'mangrove wood', 'mangrove planks', 'sticks', #forage resources

    'coal', 'iron ore', 'iron ingots', 'redstone dust',
    'gold ore', 'gold ingots', 'diamonds', 'netherite ore', 'lapis lazuli', 'emeralds',
    'nether quartz', 'obsidian', 'cobblestone', 'deepslate', 'dirt', #mine resources

    'sugar cane', 'cactus', 'wheat', 'carrots', 'potatoes',
    'cocoa beans', 'melon', 'pumpkins', #farm resources

    'leather', 'raw beef', 'raw porkchops', 'raw chicken',
    'feathers', 'eggs', #easy mob resources
    
    'bone', 'gunpowder', 'slimeball', 'ender pearl', 'string',
    'spider eyes', 'ghast tears', 'rotten flesh', 'magma cream',
    'blaze rod', 'blaze powder', 'ender eye','shulker shells'] #hard mob resources

global hunt_mobs
hunt_mobs = ['creeper', 'skeleton', 'zombie', 'spider', 'enderman',
    'witch', 'slime', 'ghast', 'blaze', 'magma cube',
    'cave spider', 'guardian', 'elder guardian', 'shulker',
    'wolf', 'pig', 'cow', 'sheep', 'chicken']

global helpful_mobs
helpful_mobs = ['horse', 'villager', 'iron golem', 'striders',
    'dolphin', 'fox', 'dog', 'cat']
    
global companions
companions = []

global complex_items
complex_items = ['furnace', 'bed', 'enchanting table', 'anvil',
    'brewing stand', 'chest', 'ender chest','bookshelf']

global tool_values
tool_values = {
    'wooden sword': 1,
    'wooden pickaxe': 1,
    'wooden axe': 1,
    'wooden shovel': 1,
    'stone sword': 2,
    'stone pickaxe': 2,
    'stone axe': 2,
    'stone shovel': 2,
    'iron sword': 3,
    'iron pickaxe': 3,
    'iron axe': 3,
    'iron shovel': 3,
    'diamond sword': 4,
    'diamond pickaxe': 4,
    'diamond axe': 4,
    'diamond shovel': 4,
    'netherite sword': 5,
    'netherite pickaxe': 5,
    'netherite axe': 5,
    'netherite shovel': 5
}

global tier
tier = ["wooden", "stone", "iron", "diamond", "netherite"]

global armor_values
armor_values = {
    'leather helmet': 1,
    'leather chestplate': 3,
    'leather leggings': 2,
    'leather boots': 1,
    'iron helmet': 2,
    'iron chestplate': 6,
    'iron leggings': 5,
    'iron boots': 2,
    'diamond helmet': 3,
    'diamond chestplate': 8,
    'diamond leggings': 6,
    'diamond boots': 3,
    'netherite helmet': 3.5,
    'netherite chestplate': 8.5,
    'netherite leggings': 6.5,
    'netherite boots': 4.5
}

global enchantment_list
enchantment_list = []

global enchantments_applied
enchantments_applied = [None, None, None, None, #Armor
    None, None, None, None] #sword, pickaxe, axe, shovel

global dimensions
dimensions = ['overworld', 'nether', 'the end']

global biomes
biomes = [
    [['plains', 'forest', 'jungle', 'swamp', 'mangrove swamp', 'taiga',
      'savanna', 'dark oak forest', 'bamboo jungle', 'birch forest'],  # forage
     ['ocean', 'beach', 'river'],  # water
     ['mushroom fields', 'desert', 'mesa'],  # random
     ['lush cave', 'cave', 'deep cave']],  # mine
    [['crimson forest', 'warped forest'], # nether forage
     ['nether wastes', 'soul sand valley', 'basalt deltas']], # random nether
    ["The End", "End Islands", "End Midlands"] # the end
]

global wood_possibleItems
wood_possibleItems = {
    'plains': 'oak wood',
    'forest': 'oak wood',
    'jungle': 'jungle wood',
    'swamp': 'oak wood',
    'mangrove swamp': 'mangrove wood',
    'taiga': 'spruce wood',
    'savanna': 'acacia wood',
    'dark oak forest': 'dark oak wood',
    'bamboo jungle': 'jungle wood',
    'birch forest': 'birch wood'
}

global structures
structures = ['village', 'mineshaft', 'igloo',
    'desert temple', 'jungle temple', 'witch hut',
    'ruined portal', 'shipwreck', 'buried treasure',
    'dungeon', 'nether fossil', 'ocean ruins',
    'underwater ruins', 'pillager outpost',
    'bastion remnant', 'stronghold',
    'woodland mansion', 'ocean monument',
    'end gateway', 'end portal', 'nether fortress',
    'ruined portal']

global items
items = []
items.extend(resources)
items.extend(complex_items)

def dnt():
    global action
    global night

    action += 1

    if action == 24:
        night = True
        print("The night has begun.")
    elif action == 48:
        night = False
        action = 0
        print("The day has begun.")

    return night

action = 0
night = False

for item in tool_values:
    items.append(item)

for item in armor_values:
    items.append(item)

for i in range(len(resources)):
    inventory.append(0)

for i in range(len(items) - len(resources)):
    inventory.append(False)

def add(item,amount = None):
    if amount == None:
        inventory[items.index(item)] = True
    else:
        inventory[items.index(item)] += amount

def drop(item,amount = None):
    if amount == None:
        inventory[items.index(item)] = False
    else:
        inventory[items.index(item)] -= amount

def player_damage(damage, category = None):
    max_defense = 0
    armor_sets = {}

    if category == None:
        for item in inventory:
            if item in armor_values:
                defense_points = armor_values[item]
                armor_type = item.split()[1]  # Extract the armor type

                # Add defense points
                if armor_type in armor_sets:
                    armor_sets[armor_type]['defense'] = max(armor_sets[armor_type]['defense'], defense_points)
                else:
                    armor_sets[armor_type] = {'defense': defense_points}

        # Sum up the maximum defense points and toughness from all armor sets
        for armor_set in armor_sets.values():
            max_defense += armor_set['defense']

        true_damage = damage * (1 - (max_defense/25))

        return round(true_damage, 2)  # Round to 2 decimal places

def tool_power(action):
    action = action.lower()

    if action == 'mine':
        for item in items:
            if "pickaxe" in item and inventory[items.index(item)] == True:
                return tool_values[item]
        return 0

    elif action == 'forage':
        for item in items:
            if "axe" in item and "pickaxe" not in item and inventory[items.index(item)] == True:
                return tool_values[item]
        return 0.33

    elif action == 'dig':
        for item in items:
            if "shovel" in item and inventory[items.index(item)] == True:
                return tool_values[item]
        return 0.5

    elif action == 'hunt':
        for item in items:
            if "sword" in item and inventory[items.index(item)] == True:
                return tool_values[item] + 3
        return 0.25

def enchanting():
    pass

def menu_and_settings():
    pass

def biomeTypeFind():
    pass

def world_generation():
    
    dimension = dimensions[0]
    biomeType = randint(0, sum(isinstance(element, list) for element in biomes[0]) - 4) #keep this at 4 for overworld forest biomes only, otherwise put it to 1
    random = randint(0, len(biomes[0][biomeType]) - 1)
    biome = biomes[0][biomeType][random]
    biomeType += 1

    global world
    world = [biomeType, biome, dimension]
    
    hearts = 10
    hunger = 10
    levels = [0,0]

    global stats
    stats = [hearts, hunger]

    global xp
    xp = [levels]
    AskUser()

def manage_biome():
    pass

def manage_level(exp):
    if xp[0] <= 15:
        while exp >= 2 * xp[0] + 7:
            xp[0] += 1
            exp -= 2 * xp[0] + 7
    elif xp[0] >= 16 and xp[0] <= 30:
        while exp >= 5 * xp[0] - 38:
            xp[0] += 1
            exp -= 5 * xp[0] - 38
    elif xp[0] >= 31:
        while exp >= 9 * xp[0] - 158:
            xp[0] += 1
            exp -= 9 * xp[0] - 158

def manage_hearts(damage, event):
    hearts = stats[0]
    if event == "mob":
        hearts -= player_damage(damage)
    elif event in ("starvation","warden boom"):
        hearts -= damage
    else:
        hearts -= player_damage(damage, prot_only)
    if hearts <= 0:
        exit("You died...")

def manage_hunger(activity):
    pass

def manage_stats(category, amount, activity = None):
    pass

def craft():
    possibleItems = []
    while True:
        ans = input("What would you like to craft?\n(Say 'nothing' if you'd like to go back)\n")
        if ans.lower() in items:
            if type(inventory[items.index(ans)]) == False:
                if ans in tool_values:
                    tool_tier = ans.split()[0]
                    tool_type = ans.split()[1]
                    if tool_tier == "wooden":
                        print("You can use the following wood planks to craft the", str(ans)+":")
                        for item in items:

                            if 'planks' in item:
                                if "axe" in tool_type:
                                    wood_needed = 3
                                elif tool_type == "sword":
                                    wood_needed = 2
                                elif tool_type == "shovel":
                                    wood_needed = 1

                                if inventory[items.index(item)] >= wood_needed:
                                    print(item)
                        use = input("Which wood would you like to craft with?\n")
                    elif tool_tier == "stone":
                        use = "cobblestone"
                    elif tool_tier == "iron":
                        use = "iron ingots"

                    elif tool_tier == "diamond":
                        use = "diamonds"

                    if "axe" in tool_type:
                        if inventory[items.index(use)] >= 3 and inventory[items.index("sticks")] >= 2:
                            req = [3, 2]
                        else:
                            print("You do not have enough materials.")
                            AskUser()
                    if tool_type == "sword":
                        if inventory[items.index(use)] >= 2 and inventory[items.index("sticks")] >= 1:
                            req = [2, 1]
                        else:
                            print("You do not have enough materials.")
                            AskUser()
                    if tool_type == "shovel":
                        if inventory[items.index(use)] >= 1 and inventory[items.index("sticks")] >= 2:
                            req = [1, 2]
                        else:
                            print("You do not have enough materials.")
                            AskUser()
                            

                    drop(use, req[0])
                    drop("sticks", req[1])

                    add(ans)
                    print(str(ans),"has been added to your inventory.")

                    for i in range(tier.index(tool_tier)):
                        drop(str(tier[i]) + str(" ") + str(tool_type))

                    AskUser()



                        
            elif type(inventory[items.index(ans)]) == int:
                amount = int(input("How many would you like to craft?\n"))
                if "plank" in ans:
                    if amount % 4 != 0:
                        print("You can't craft planks in that package size. It has to be in bundles of 4.")
                        continue
                    else:
                        for item in items:
                            if 'wood' in item and ans.split()[0] in item.split()[0]:
                                if inventory[items.index(item)] >= amount / 4:
                                    wood = item
                                    if inventory[items.index(wood)] >= amount/4:
                                        add(ans, amount)
                                        drop(wood, amount / 4)
                                        print('You have successfully crafted',amount,str(ans)+'!')
                                        AskUser()
                                    else:
                                        print(f"You don't have enough {wood}")
                                else:
                                    print(f"You don't have enough {ans.split()[0]} wood as such can not craft those planks.")
                elif ans == "sticks":
                    if amount % 4 != 0:
                        print("You can't craft sticks in that package size. It has to be in bundles of 4.")
                        continue
                    else:
                        print("These are the items you can use to craft the sticks:\n")
                        if any(inventory[i] >= 0 for i in range(len(items)) if "planks" in items[i]):
                            for item in items:
                                if 'planks' in item:
                                    if inventory[items.index(item)] >= amount / 2:
                                        possibleItems.append(item)
                            for item in possibleItems:
                                print(item)
                        else:
                            print("You do not have the required resources.")

                        wood = input("Which item would you like to use?\n")
                        if wood in possibleItems:
                            add("sticks", amount)
                            drop(wood, amount/2)
                            AskUser()
                        else:
                            print("That is not one of the possible options.")


            elif inventory[items.index(ans)] == True:
                print("You already have this item.")
        elif ans == "nothing":
            print("Understood. \n")
            AskUser()
        else:
            print("This item does not exist.")
    AskUser()

def forage():
    while True:
        try:
            ans = int(input('How many blocks would you like to mine? '))
            if ans / tool_power('forage') >= 60:
                print("The more blocks you forage the longer it will take.\nThis will take about",round(ans / tool_power('forage'),1),"seconds.")
                user = input("Are you sure you would like to forage?\n")
                if user.lower() in ('yes', 'y'):
                    break
                elif user.lower() in ("no", "n"):
                    return
                else:
                    print("That input is invalid. Please try again.")
            elif ans / tool_power('forage') <= 60:
                print("Foraging...")
                break
        except:
            print("That input is invalid. Please try again.")
            
    wood_type = wood_possibleItems.get(world[1].lower())
        
    add(wood_type, ans)
    #sleep(ans / tool_power('forage'))
    print("You got",ans,wood_type)
    AskUser()

def hunt():
    pass


def mine():
    while True:
        try:
            ans = int(input('How many blocks would you like to mine?'))
            if ans / tool_power('mine') > 60:
                ans = input("The more you mine the longer it will take.\nThis will take over a minute.\nAre you sure you would like to mine?\n")
                if ans.lower() in ('yes','y'):
                    print("Mining...")
                    break
            print("Mining...")
            break
        except:
            print("That input is invalid. Please try again.")
    for i in range(ans):
        pass
    sleep(ans / tool_power('mine'))

def explore():
    pass

def explorePlains():
    pass

def exploreForest():
    pass

def exploreNether():
    pass

def exploreEnd():
    pass

def exploreSpace():
    pass

def exploreMoon():
    pass

def exploreOcean():
    pass

def exploreOuterEnd():
    pass

def float_to_int():
    for i in range(len(inventory)):
        if isinstance(inventory[i], float):
            inventory[i] = int(inventory[i]) 

def hasReq(activity):
    if activity == "mine":
        for item in items:
            if any(inventory[i] for i in range(len(items)) if "pickaxe" in items[i]):
                    if world[2] == "overworld":
                        if world[0] == 4:
                            print("You will be mining in a", biome)
                        elif world[0] == 2:
                            print("You are in the (water) biome", biome + ", and as such you can't dig down here.")
                        else:
                            print("You are in the (above ground) biome", biome, "and have to dig underground to mine.")
                            ans = input("Would you like to dig?\n")
                            if ans.lower() in ("yes", "y"):
                                print("Digging... This may take a while...")
                                sleep(25 / tool_power("dig"))
                                world[0] = 3
                                world[1] = biomes[world[0]][randint(0,(len(biomes[world[0]])) - 1)]
                                print("You are now in the biome:",world[1])
                                mine()
            else:
                print("You do not have a pickaxe.\n")
                AskUser()
    elif activity == "forage":
        if world[0] == 1:
            print("You will be foraging in the", world[1])
            forage()
        else:
            print("You're in the biome", world[1], + ", you can't forage here.")
            AskUser()
    elif activity == "craft":
        if any(inventory):
            craft()

def eat():
    AskUser()

def build():
    AskUser()

def check_inventory():
    if any(inventory):
        print(inventory)
        for i in range(len(items)):
            value = inventory[i]
            if value != 0 and value != False:
                if type(value) == int:
                    print(str(items[i])+":",value)
                else:
                    print("\nYou have a",str(items[inventory.index(value)])+"\n")
    else:
        print("\nYou have no items.\n")
    AskUser()

def AskUser():
    add("diamonds",2)
    float_to_int()
    biome = str(world[1])
    dimension = str(world[2])

    print("You're in", biome + ', ' + dimension + '.')

    while True:
        ans = input('\nWhat would you like to do?\n▷ Gather Resources\n▷ Explore\n▷ Craft \n▷ Settings\n▷ More\n\n\n').lower()
        if ans in ("mine", "forage", "hunt"):
            hasReq(ans)
        if ans.lower() in ("gather resources", "1", "gather"):
            while True:
                ans = input('\nWould you like to mine, forage, or hunt?\n').lower()
                try:
                    int(ans)
                    ans = ["mine","forage","hunt"][ans]
                    hasReq(ans)
                except:
                    if ans in ("mine", "forage", "hunt"):
                        hasReq(ans)
                else:
                    print("That's not a valid option.")

        elif ans in ["explore", "2"]:
            explore()
        elif ans in ['craft', "3"]:
            craft()
        
        elif ans.lower() == "more":
            while True:
                ans = (input("\n▷ Eat\n▷ Build\n▷ Check Inventory\n\n\n").lower()).replace(" ", "_")
                try:
                    ans = "eat" if ans == "1" else ans
                    ans = "build" if ans == "2" else ans
                    ans = "check_inventory" if ans in ["inventory", 3] else ans
                    
                    func = globals()[ans]
                    func()
                except:
                    print("That's not a valid input. Please try again.")
                    

        else:
            print("That's not an option.")

def welcome():
    print("Welcome! This is a game I made to replicate minecraft.")
    sleep(2)
    print("Note that there are many changes.")
    sleep(2.5)
    ans = input("Would you like to learn about the changes?\n")
    if ans.lower() in ("yes","y"):
        changes = ["1. Gold can not be used to craft tools.",
        "\n2. Gold can not be used to craft armor.",
        "\n3. Items do not have durability.",
        "\n4. Many utility items are set to either\n True or False values once acquiried.",
        "\n5. The inventory has practically infinite storage space for each item.",
        "\n6. Your building options are limited.",
        "\n7. Netherite armor has buffed protection\n capabilities due to the lack of durability incentives.",
        "\n8. Drops from tasks such as mining and mob farming are\n determined by a combination of luck and text-based minigames.",
        "\n9. Items of lower tiers are deleted once a higher tier\n item is acquired (e.g. when a stone pickaxe is\n acquired the lower tiered wooden pickaxe is deleted)",
        "\n10. Crafting tables are removed from the game and the crafting\n function is moved into the main selection of choices.",
        "\n11. Hoes don't exist."]
        for change in changes:
            print(change)
            sleep(1)
    sleep(0.05)

    while True:
        ans = input("Would you like to play?\n")
        if ans.lower() in ('yes','y'):
            print("Generating World...\n")
            sleep(0.75)
            break
        elif ans.lower() in ('no','n'):
            print("umm... ok... ")
            sleep(1)
            print("ykw i'll just give you a random game then\n")
            sleep(1)
            GMN(10 ** randint(1, 4)) if randint(1, 2) == 1 else word_jumble(randint(1, 3))
        else:
            print("that's not a yes or no...")
#welcome()
world_generation()