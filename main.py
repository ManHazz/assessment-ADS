import json
import time
import random
import sys

from src.linked_list import LinkedList
from src.stack import Stack
from src.bst import BinarySearchTree
from src.queue import Queue

sys.setrecursionlimit(3000)

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Please run generate_data.py first.")
        sys.exit(1)

def find_matches_by_description(items, keyword):
    
    matches = []
    keyword = keyword.lower()
    for item in items:
        
        if keyword in item['name'].lower() or keyword in item['category'].lower():
            matches.append(item)
    return matches

def main():
    print("=================================================")
    print("   CAMPUS LOST-AND-FOUND SYSTEM   ")
    print("=================================================")

    
    items_data = load_data('data/items.json')
    print(f"[System] Database loaded with {len(items_data)} items.")

    
    ll = LinkedList()
    bst = BinarySearchTree()

    
    for item in items_data:
        ll.insert(item)

    
    shuffled_data = items_data[:]
    random.shuffle(shuffled_data)
    for item in shuffled_data:
        bst.insert(item)

    print("[System] System Ready. Waiting for user input...\n")

    # user keyword search for losrt item
    while True:
        user_query = input(">> What did you lose? (e.g., 'blue wallet', 'keys'): ").strip()
        if not user_query:
            print("Please enter a description.")
            continue
            
        print(f"\n[Searching] Looking for items matching '{user_query}'...")
        
        
        matches = find_matches_by_description(items_data, user_query)

        if not matches:
            print("❌ No items found matching that description. Try again.")
            continue
        
        print(f"Found {len(matches)} possible matches:\n")
        print(f"{'ID':<6} | {'Item Name':<25} | {'Location':<15}")
        print("-" * 55)

        #display only first 10 matches
        for item in matches[:10]:
            print(f"{item['id']:<6} | {item['name']:<25} | {item['location']:<15}")
        
        if len(matches) > 10:
            print(f"... and {len(matches) - 10} more.")
            
        break 


    # user id selection
    print("\n-------------------------------------------------")
    print("Which one is yours? Enter the ID to claim it.")
    
    try:
        selected_id = int(input(">> Enter Item ID: "))
    except ValueError:
        print("Invalid ID entered. Exiting.")
        return

    print(f"\n[System] meaningful retrieval for Item ID #{selected_id}...")
    print("(Comparing Baseline vs. Optimized performance...)\n")

    # Benchmark 1 -linked list
    start_time = time.perf_counter()
    found_data, steps_ll = ll.linear_search(selected_id)
    end_time = time.perf_counter()
    time_ll = (end_time - start_time) * 1000 # ms

    print(f"1. Baseline Approach (Linked List):")
    if found_data:
        print(f"   - Status: RETRIEVED")
    else:
        print(f"   - Status: NOT FOUND")
    print(f"   - Steps taken: {steps_ll}")
    print(f"   - Time taken: {time_ll:.4f} ms")

    # Benchmark 2 - optimized (Binary Search Tree)
    start_time = time.perf_counter()
    found_data, steps_bst = bst.search(selected_id)
    end_time = time.perf_counter()
    time_bst = (end_time - start_time) * 1000 # ms

    print(f"\n2. Optimized Approach (AVL/BST):")
    if found_data:
        print(f"   - Status: RETRIEVED")
    else:
        print(f"   - Status: NOT FOUND")
    print(f"   - Steps taken: {steps_bst}")
    print(f"   - Time taken: {time_bst:.4f} ms")

    # Summary
    if steps_bst > 0:
        speedup = steps_ll / steps_bst
        print(f"\n>> EFFICIENCY RESULT: The Optimized System was {speedup:.1f}x faster.")
    
  
    # Queue process comparison
    print("\n-------------------------------------------------")
    print("[Claim Process] Processing the waiting line...")
    
    students = ["You (Arrived 1st)", "Student B (Arrived 2nd)", "Student C (Arrived 3rd)"]

    print("\n--- Scenario A: Stack (Unfair/LIFO) ---")
    stack = Stack()
    for student in students:
        stack.push(student)
        print(f"  -> {student} added to stack.")
    served_stack = stack.pop()
    print(f"Now serving: {served_stack} (Last person in!)")

    print("\n--- Scenario B: Queue (Fair/FIFO) ---")
    queue = Queue()
    for student in students:
        queue.enqueue(student)
        print(f"  -> {student} added to queue.")
    served_queue = queue.dequeue()
    print(f"Now serving: {served_queue} (First person in!)")

if __name__ == "__main__":
    main()