import sys
sys.path.append('..')

from src.bst import BinarySearchTree


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


if __name__ == "__main__":
    result = test_binary_search_tree()
    if result:
        print("\n✅ Test completed successfully")
    else:
        print("\n❌ Test failed")
