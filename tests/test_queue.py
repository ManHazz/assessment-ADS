import sys
sys.path.append('..')

from src.queue import Queue


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


if __name__ == "__main__":
    result = test_queue()
    if result:
        print("\n✅ Test completed successfully")
    else:
        print("\n❌ Test failed")
