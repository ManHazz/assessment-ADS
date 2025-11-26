#The Lost & Found Data Structures Test System
#Goal: Verify that every data structure functions properly prior to deployment.
#The following operations are tested in this file:
#Linked List, Binary Search Tree, Stack, and Queue.

import sys
sys.path.append('.')

from src.linked_list import LinkedList
from src.bst import BinarySearchTree
from src.stack import Stack
from src.queue import Queue


def test_linked_list():
    print("\n" + "="*60)
    print("TEST 1: LINKED LIST")
    print("="*60)
    
    ll = LinkedList()
    test_passed = True
    
    print("\n[Test 1.1] Inserting items...")
    test_items = [
        {"id": 100, "name": "Red Umbrella", "category": "Personal"},
        {"id": 200, "name": "Blue Wallet", "category": "Personal"},
        {"id": 300, "name": "Laptop", "category": "Electronics"}
    ]
    
    for item in test_items:
        ll.insert(item)
    
    print("✓ Inserted 3 items")
    
    print("\n[Test 1.2] Searching for existing item (ID: 200)...")
    result, steps = ll.linear_search(200)
    
    if result and result['id'] == 200:
        print(f"✓ Found item: {result['name']} (Steps: {steps})")
    else:
        print("✗ FAILED: Could not find item with ID 200")
        test_passed = False
    
    print("\n[Test 1.3] Searching for non-existing item (ID: 999)...")
    result, steps = ll.linear_search(999)
    
    if result is None:
        print(f"✓ Correctly returned None (Steps: {steps})")
    else:
        print("✗ FAILED: Should return None for missing item")
        test_passed = False
    
    print("\n[Test 1.4] Verifying insertion order...")
    current = ll.head
    expected_order = [300, 200, 100]
    actual_order = []
    
    while current:
        actual_order.append(current.data['id'])
        current = current.next
    
    if actual_order == expected_order:
        print(f"✓ Correct order: {actual_order}")
    else:
        print(f"✗ FAILED: Expected {expected_order}, got {actual_order}")
        test_passed = False
    
    if test_passed:
        print("\n✅ LINKED LIST: ALL TESTS PASSED")
    else:
        print("\n❌ LINKED LIST: SOME TESTS FAILED")
    
    return test_passed


def test_binary_search_tree():
    print("\n" + "="*60)
    print("TEST 2: BINARY SEARCH TREE")
    print("="*60)
    
    bst = BinarySearchTree()
    test_passed = True
    
    print("\n[Test 2.1] Inserting items...")
    test_items = [
        {"id": 50, "name": "Notebook", "category": "Stationery"},
        {"id": 30, "name": "Pen", "category": "Stationery"},
        {"id": 70, "name": "Keys", "category": "Personal"},
        {"id": 20, "name": "Eraser", "category": "Stationery"},
        {"id": 40, "name": "Ruler", "category": "Stationery"},
        {"id": 60, "name": "Phone", "category": "Electronics"},
        {"id": 80, "name": "Watch", "category": "Accessories"}
    ]
    
    for item in test_items:
        bst.insert(item)
    
    print("✓ Inserted 7 items")
    
    print("\n[Test 2.2] Searching for existing items...")
    test_ids = [50, 20, 80, 40]
    
    for test_id in test_ids:
        result, steps = bst.search(test_id)
        if result and result['id'] == test_id:
            print(f"  ✓ Found ID {test_id} in {steps} steps")
        else:
            print(f"  ✗ FAILED: Could not find ID {test_id}")
            test_passed = False
    
    print("\n[Test 2.3] Searching for non-existing item (ID: 999)...")
    result, steps = bst.search(999)
    
    if result is None:
        print(f"✓ Correctly returned None (Steps: {steps})")
    else:
        print("✗ FAILED: Should return None for missing item")
        test_passed = False
    
    print("\n[Test 2.4] Verifying efficiency...")
    result, steps = bst.search(20)
    
    if steps <= 4:
        print(f"✓ BST efficiency confirmed: {steps} steps for 7 items")
    else:
        print(f"⚠ Warning: BST took {steps} steps (might be unbalanced)")
    
    if test_passed:
        print("\n✅ BINARY SEARCH TREE: ALL TESTS PASSED")
    else:
        print("\n❌ BINARY SEARCH TREE: SOME TESTS FAILED")
    
    return test_passed


def test_stack():
    print("\n" + "="*60)
    print("TEST 3: STACK (LIFO)")
    print("="*60)
    
    stack = Stack()
    test_passed = True
    
    print("\n[Test 3.1] Testing empty stack...")
    if stack.is_empty():
        print("✓ New stack is empty")
    else:
        print("✗ FAILED: New stack should be empty")
        test_passed = False
    
    print("\n[Test 3.2] Pushing students to stack...")
    students = ["Alice", "Bob", "Charlie"]
    
    for student in students:
        stack.push(student)
        print(f"  Pushed: {student}")
    
    print("\n[Test 3.3] Popping items (Last-In-First-Out)...")
    expected_order = ["Charlie", "Bob", "Alice"]
    actual_order = []
    
    while not stack.is_empty():
        student = stack.pop()
        actual_order.append(student)
        print(f"  Popped: {student}")
    
    if actual_order == expected_order:
        print("✓ Correct LIFO order")
    else:
        print(f"✗ FAILED: Expected {expected_order}, got {actual_order}")
        test_passed = False
    
    print("\n[Test 3.4] Attempting to pop from empty stack...")
    result = stack.pop()
    
    if result is None:
        print("✓ Correctly returned None")
    else:
        print("✗ FAILED: Should return None when empty")
        test_passed = False
    
    if test_passed:
        print("\n✅ STACK: ALL TESTS PASSED")
    else:
        print("\n❌ STACK: SOME TESTS FAILED")
    
    return test_passed


def test_queue():
    print("\n" + "="*60)
    print("TEST 4: QUEUE (FIFO)")
    print("="*60)
    
    queue = Queue()
    test_passed = True
    
    print("\n[Test 4.1] Testing empty queue...")
    if queue.is_empty():
        print("✓ New queue is empty")
    else:
        print("✗ FAILED: New queue should be empty")
        test_passed = False
    
    print("\n[Test 4.2] Enqueueing students to queue...")
    students = ["Alice", "Bob", "Charlie"]
    
    for student in students:
        queue.enqueue(student)
        print(f"  Enqueued: {student}")
    
    print("\n[Test 4.3] Dequeueing items (First-In-First-Out)...")
    expected_order = ["Alice", "Bob", "Charlie"]
    actual_order = []
    
    while not queue.is_empty():
        student = queue.dequeue()
        actual_order.append(student)
        print(f"  Dequeued: {student}")
    
    if actual_order == expected_order:
        print("✓ Correct FIFO order")
    else:
        print(f"✗ FAILED: Expected {expected_order}, got {actual_order}")
        test_passed = False
    
    print("\n[Test 4.4] Attempting to dequeue from empty queue...")
    result = queue.dequeue()
    
    if result is None:
        print("✓ Correctly returned None")
    else:
        print("✗ FAILED: Should return None when empty")
        test_passed = False
    
    if test_passed:
        print("\n✅ QUEUE: ALL TESTS PASSED")
    else:
        print("\n❌ QUEUE: SOME TESTS FAILED")
    
    return test_passed


def test_stack_vs_queue_fairness():
    print("\n" + "="*60)
    print("TEST 5: FAIRNESS COMPARISON")
    print("="*60)
    
    students = ["Student 1 (arrived first)", 
                "Student 2 (arrived second)", 
                "Student 3 (arrived third)"]
    
    print("\n[Baseline] Using Stack (LIFO - Unfair):")
    stack = Stack()
    for s in students:
        stack.push(s)
    
    print("  Processing order:")
    order = 1
    while not stack.is_empty():
        print(f"    {order}. {stack.pop()}")
        order += 1
    
    print("\n[Optimized] Using Queue (FIFO - Fair):")
    queue = Queue()
    for s in students:
        queue.enqueue(s)
    
    print("  Processing order:")
    order = 1
    while not queue.is_empty():
        print(f"    {order}. {queue.dequeue()}")
        order += 1
    
    print("\n✓ Fairness difference demonstrated")


def run_all_tests():
    print("\n" + "#"*60)
    print("#" + " "*58 + "#")
    print("#" + " "*15 + "LOST & FOUND SYSTEM TEST SUITE" + " "*13 + "#")
    print("#" + " "*58 + "#")
    print("#"*60)
    
    results = []
    
    results.append(("Linked List", test_linked_list()))
    results.append(("Binary Search Tree", test_binary_search_tree()))
    results.append(("Stack", test_stack()))
    results.append(("Queue", test_queue()))
    
    test_stack_vs_queue_fairness()
    
    print("\n" + "="*60)
    print(" "*20 + "TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name:<25} {status}")
    
    print("-"*60)
    print(f"Total: {passed}/{total} tests passed")
    print("="*60)
    
    if passed == total:
        print("\n🎉 ALL SYSTEMS OPERATIONAL! Ready for deployment.")
    else:
        print(f"\n⚠️  WARNING: {total - passed} system(s) failed validation.")
    
    print("\n")


if __name__ == "__main__":
    run_all_tests()
