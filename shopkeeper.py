# Should learn about dictionaries soon so i can make prices to each item.

print("Greetings traveller! I am the shopkeeper.")
purchaseable_items = ["stick", "sword", "bread"]
inventory_items = ["stick", "shield"]
player_speech = ["Where am I?", "Where actually am I?", "Huh?", "Sure!", "...", "Who is \"him\"", "Oh no", "How do I survive then?", "Well thanks for that, I shall be heading towards him.", "Well thanks, see ya.", "Bye", "Goodbye =)"]
npc_speech = ["Well you are clearly in my shop!", "Oh, you are in the middle of nowhere with no hope of leaving this place and the world is going to combust within an hour.", "Well you can actually survive if you go talk to him.", "Oh... he? I have forgotten where he lives. All I remember is that he used to live in the North direction.", "Goodbye!", "Huh?", "What?"]

def buy():
    item_selection = input(f"\n\nShopkeeper: Oh heres what all I sell: \n[1] {purchaseable_items[0]} \n[2] {purchaseable_items[1]}, \n[3] {purchaseable_items[2]} \nTIP: You can select an item by typing the number corresponding to the item. \n> ")
    if item_selection.lower() in purchaseable_items:
        print(f"\n\nShopkeeper: Thanks for purchasing {item_selection} for free!")
    else:
        print("\n\nShopkeeper: Sorry, I don't sell that.")
    gameloop()

def sell():
    item_selection = input(f"\n\nShopkeeper: Oh you want to sell something? Lets see: \n[1] {inventory_items[0]} \n[2] {inventory_items[1]} \nTIP: You can select an item by typing the number corresponding to the item. \n> ")
    if item_selection.lower() in inventory_items:
        print("\n\nShopkeeper: Hmm... let me see... Well I can take it for free HAH!")
    else:
        print("\n\nShopkeeper: You don't actually have that with you now do you?")
    gameloop()

# WORK IN PROGRESS
def talk(line):
    mem = None
    while line != "end": # 0 means end
        if line == "start":
            line = int(input(f"\n\nShopkeeper: What you wanna talk about? \n[1] {player_speech[0]} \n[2] {player_speech[4]} \nTIP: You can select an action by typing the number corresponding to the action.\n> "))
        elif line == 1 and mem == None: # reply to where am i?
            line = int(input(f"\n\nShopkeeper: {npc_speech[0]} \nReply with:\n[1] {player_speech[1]} \n[2] {player_speech[-2]} \nTIP: You can select an action by typing the number corresponding to the action.\n> "))
            mem = player_speech[0]
        elif line == 2 and mem == None: # reply to ...
            print(f"\n\nShopkeeper: {npc_speech[-1]}")
            line = "end"
        elif line == 1 and mem == player_speech[0]: # reply to where actually am i?
            line = int(input(f"\n\nShopkeeper: {npc_speech[1]} \nReply with:\n[1] {player_speech[7]} \n[2] {player_speech[6]} \nTIP: You can select an action by typing the number corresponding to the action. \n> "))
            mem = player_speech[1]
        elif line == 2 and mem == player_speech[0]: # reply to bye. 
            print(f"\n\nShopkeeper: {npc_speech[-3]}")
            line = "end"
            break
        elif line == 1 and mem == player_speech[1]: # reply to how do i survive then
            line = int(input(f"\n\nShopkeeper: {npc_speech[2]} \nReply with: \n[1] wip \n[2] wip \nTIP: You can select an action by typing the number corresponding to the action. \n> "))
            mem = player_speech[6]
        elif line == 2 and mem == player_speech[1]: # reply to oh no
            line = int(input(f"\n\nShopkeeper: Welll... dont worry everything will be fine. Its just you have to stay positive. (really hope that nothing happens idk what will happen soon.)\nReply with: \n[1] {player_speech[-1]} \nTIP: You can select an action by typing the number corresponding to the action. \n> "))
            mem = player_speech[-1]
        else:
            line = "end"
            print("\n\nShopkeeper: Uhhh... you know you are supposed to type one of the corresponding numbers right? Lets try again.")
    else:
        return gameloop()
# WORK IN PROGRESS

def gameloop():
    selection = int(input("Shopkeeper: Anything else? \nTIP: You can choose your action by selectiong the corresponding digit: \n[1] Buy \n[2] Sell \n[3] Talk \n[4] Leave \n> "))
    if selection == 1:
        print(buy())
    elif selection == 2:
        print(sell())
    elif selection == 3:
        talk("start")
    elif selection == 4:
        print(npc_speech[-3])
    else:
        print(npc_speech[-1] or npc_speech[-2])

selection = int(input("What brings you here? \n\nChoose your action by selectiong the corresponding digit: \n[1] Buy \n[2] Sell \n[3] Talk \n[4] Leave \n> "))
if selection == 1:
    print(buy())
elif selection == 2:
    print(sell())
elif selection == 3:
    talk("start") # -1 means start
elif selection == 4:
    print(npc_speech[-3])
else:
    print(npc_speech[-1] or npc_speech[-2])
