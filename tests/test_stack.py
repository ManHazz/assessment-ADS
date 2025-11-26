import sys
sys.path.append('..')

from src.stack import Stack


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


if __name__ == "__main__":
    result = test_stack()
    if result:
        print("\n✅ Test completed successfully")
    else:
        print("\n❌ Test failed")
