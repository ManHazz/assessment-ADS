import json
import os
import random

def generate_json():
    
    if not os.path.exists('data'):
        os.makedirs('data')

    
    # manual add items
    items = [
        {"id": 1, "category": "Personal", "name": "Raziq's Matrix Card", "location": "Exam Hall"},
        {"id": 2, "category": "Electronics", "name": "Lecturer's iPad", "location": "Staff Room"},
    ]
    
    current_id_start = 3 # Start random IDs after the manual ones

   
    # randomly generate lost item
    
    print("Generating random lost items...")
    
    colors = ["Red", "Blue", "Black", "Green", "Yellow", "White", "Silver", "Gold", "Purple"]
    objects = ["Wallet", "Umbrella", "Water Bottle", "Keys", "Notebook", "Jacket", "Phone Case", "Calculator", "Bag"]
    locations = ["Library", "Cafeteria", "Main Hall", "Gym", "Student Center", "Lab 1", "Mosque", "Parking Lot A"]
    categories = {
        "Wallet": "Personal", "Umbrella": "Accessories", "Water Bottle": "Personal", 
        "Keys": "Security", "Notebook": "Stationery", "Jacket": "Clothing", 
        "Phone Case": "Electronics", "Calculator": "Electronics", "Bag": "Accessories"
    }

    
    total_items_needed = 1000
    
    for i in range(current_id_start, total_items_needed + 1):
        # Pick random attributes
        obj = random.choice(objects)
        color = random.choice(colors)
        loc = random.choice(locations)
        
        
        item = {
            "id": i,
            "category": categories[obj],
            "name": f"{color} {obj}",  
            "location": loc
        }
        items.append(item)


    with open('data/items.json', 'w') as f:
        json.dump(items, f, indent=4)
    
    print(f"Success! Generated {len(items)} items in 'data/items.json'.")

if __name__ == "__main__":
    generate_json()