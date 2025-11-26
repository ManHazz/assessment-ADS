import sys
sys.path.append('..')

from src.linked_list import LinkedList


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


if __name__ == "__main__":
    result = test_linked_list()
    if result:
        print("\n✅ Test completed successfully")
    else:
        print("\n❌ Test failed")
