# Map of rooms and directions
rooms = {
    "Operations Center": {"west": "Barracks", "north": "Medical Wing", "south": "Armory", "east": "Laboratory X"},
    "Barracks": {"east": "Operations Center",},
    "Medical Wing": {"south": "Operations Center", "east": "Mess Hall"},
    "Mess Hall": {"west": "Medical Wing"},
    "Private Washrooms": {"east": "Armory"},
    "Armory": {"west": "Private Washrooms", "north": "Operations Center", "east": "Mission Command"},
    "Mission Command": {"west": "Armory"},
    "Laboratory X": {"west": "Operations Center", "north": "Mutant X Room"},
    "Mutant X Room": {}  # No exits
}

# Items in rooms
room_items = {
    "Barracks": "Sample A",
    "Medical Wing": "Sample B",
    "Mess Hall": "Sample C",
    "Private Washrooms": "Sample D",
    "Armory": "Sample E",
    "Mission Command": "Sample F",
    "Laboratory X": "Syringe"
}

# Items needed to win
required_items = {
    "Sample A", "Sample B", "Sample C", "Sample D", "Sample E", "Sample F", "Syringe"
}

# Start state
current_room = "Operations Center"
inventory = []

input("Do you want to play Operation Ground Zero: Last Mission? (press Enter to continue...)")

print("\nThe world hangs in the balance.")
print("Your team fell, but you must carry on.")
print("Recover all 6 of the samples and the syringe before facing Mutant X.")
print("Good luck, soldier!\n")

# Game loop
while True:
    print(f"\nYou are in the {current_room}.")

    # Show item if present
    if current_room in room_items:
        item = room_items[current_room]
        print(f"You found {item} here.")

    print(f"Inventory: {inventory}")
    action = input("What do you want to do? (move/get/quit): ").lower()

    if action == "quit":
        print("You gave up. Game over.")
        break

    elif action == "move":
        direction = input("Which direction? (north/south/east/west): ").lower()

        if direction in rooms[current_room]:
            next_room = rooms[current_room][direction]

            # Check if entering the Mutant X room
            if next_room == "Mutant X Room":
                if set(inventory) >= required_items:
                    print("\nYou face Mutant X...")
                    print("You have all the samples and the syringe.")
                    print("You inject the cure and defeat Mutant X. The world is saved!")
                    break
                else:
                    print("\nYou face Mutant X...")
                    print("But you're not ready. You're missing required items.")
                    print("Mutant X tears you apart. GAME OVER.")
                    break
            else:
                current_room = next_room
                print(f"You moved to {current_room}.")
        else:
            print("You can't go that way.")

    elif action == "get":
        if current_room in room_items:
            item = room_items[current_room]
            if item not in inventory:
                inventory.append(item)
                print(f"You picked up {item}.")
                del room_items[current_room]  # Remove item from room
            else:
                print("You already have that item.")
        else:
            print("There's nothing here to pick up.")

    else:
        print("Invalid action. Please type move, get, or quit.")
