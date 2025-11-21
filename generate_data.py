import json
import os
import random

def generate_json():
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # ==========================================
    # 1. MANUAL ENTRY (Add specific items here)
    # ==========================================
    # You can add items here that you definitely want in the list.
    items = [
        {"id": 1, "category": "Personal", "name": "Raziq's Matrix Card", "location": "Exam Hall"},
        {"id": 2, "category": "Electronics", "name": "Lecturer's iPad", "location": "Staff Room"},
    ]
    
    current_id_start = 3 # Start random IDs after the manual ones

    # ==========================================
    # 2. RANDOM GENERATOR (For the remaining items)
    # ==========================================
    print("Generating random lost items...")
    
    colors = ["Red", "Blue", "Black", "Green", "Yellow", "White", "Silver", "Gold", "Purple"]
    objects = ["Wallet", "Umbrella", "Water Bottle", "Keys", "Notebook", "Jacket", "Phone Case", "Calculator", "Bag"]
    locations = ["Library", "Cafeteria", "Main Hall", "Gym", "Student Center", "Lab 1", "Mosque", "Parking Lot A"]
    categories = {
        "Wallet": "Personal", "Umbrella": "Accessories", "Water Bottle": "Personal", 
        "Keys": "Security", "Notebook": "Stationery", "Jacket": "Clothing", 
        "Phone Case": "Electronics", "Calculator": "Electronics", "Bag": "Accessories"
    }

    # Generate up to 1000 items
    total_items_needed = 1000
    
    for i in range(current_id_start, total_items_needed + 1):
        # Pick random attributes
        obj = random.choice(objects)
        color = random.choice(colors)
        loc = random.choice(locations)
        
        # Create the item record
        item = {
            "id": i,
            "category": categories[obj],
            "name": f"{color} {obj}",  # Example: "Blue Wallet"
            "location": loc
        }
        items.append(item)

    # ==========================================
    # 3. SAVE TO FILE
    # ==========================================
    with open('data/items.json', 'w') as f:
        json.dump(items, f, indent=4)
    
    print(f"Success! Generated {len(items)} items in 'data/items.json'.")
    print("Sample:", items[:3]) # Show first 3 items as proof

if __name__ == "__main__":
    generate_json()