import sys
sys.path.append('.')

from tests.test_linked_list import test_linked_list
from tests.test_bst import test_binary_search_tree
from tests.test_stack import test_stack
from tests.test_queue import test_queue
from src.stack import Stack
from src.queue import Queue


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
