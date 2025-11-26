# ADS Assessment - Lost & Found System

## Authors
* **Muhammad Aiman bin Ahmad Hazimin** (22011708)
* **Dhesigan A/L Vengadajalapathy** (22009144)
* **Muhammad Raziq Bin Sufian** (24006626)
* **Hazieq Danial Bin Roshihan Annuar** (24006633)
* **Mohamed Ennaceur** (24004285)

---

## Project Overview
This project is a simulation of a university Lost-and-Found System. It addresses the real-world challenge of managing thousands of lost items and students waiting to claim them.

The system demonstrates a realistic workflow:
1.  **Public Search:** Students browse/search for their lost item using keywords (e.g., "Blue Wallet").
2.  **Admin Retrieval (Optimization Core):** Once the ID is identified, the system retrieves the full secure record. We compare a **Baseline (Linked List)** vs. an **Optimized (Binary Search Tree)** approach to measure the speed difference.
3.  **Claim Queue:** We compare an unfair **Stack (LIFO)** approach against a fair **Queue (FIFO)** approach for managing the waiting line.

## Prerequisites
* **Python 3.x**
* No external libraries required.

---

## Setup & Installation

### Step 1: Generate the Database
First, you must create the dataset. The generator script creates 1,000 realistic items (e.g., "Red Umbrella", "Silver Laptop") with unique IDs and locations.

1.  Open your terminal or command prompt.
2.  Navigate to the project folder.
3.  Run the generation script:
    ```bash
    python generate_data.py
    ```
    **Success:** You will see a message confirming `data/items.json` has been created.

---

## How to Run the System
To start the simulation, run the main program:
```bash
python main.py
```

### System Workflow (What to Expect)

#### Phase 1: User Search (Interaction)
*   **The system asks:** `>> What did you lose?`
*   **Action:** Type a keyword like `wallet`, `keys`, or `blue`.
*   **Result:** The system will display a table of matching items found in the database.

#### Phase 2: Item Selection & Retrieval (The Benchmark)
*   **Action:** Identify "your" item from the list and enter its ID.
*   **Process:** The system will now race to fetch that specific ID using two methods:
    *   **Baseline (Linked List):** Scans one by one (Slow).
    *   **Optimized (BST):** Uses binary search logic (Fast).
*   **Output:** A comparison of "Steps Taken" and "Time (ms)" for both methods.

#### Phase 3: Claim Queue (Fairness Test)
*   The system simulates 3 students arriving at the counter.
*   **Stack Test:** Shows the last student being served first (Unfair).
*   **Queue Test:** Shows the first student being served first (Fair).

---

## Testing

To verify every data structure, run the test suite:
```bash python test_system.py```

This will perform thorough testing on the following:
- Linked List operations
-Binary Search Tree Functions
-Stack (LIFO) behavior
-Queue (FIFO) behavior

---

## File Structure & Complexity

| File | Purpose | Complexity |
| :--- | :--- | :--- |
| `src/linked_list.py` | **Baseline storage.** Must scan nodes sequentially to find an ID. | O(n) |
| `src/bst.py` | **Optimized storage.** Uses a Binary Search Tree to divide search space by half. | O(log n) |
| `src/stack.py` | **Baseline processing.** Uses "Last-In, First-Out" logic (Unfair). | O(1) |
| `src/my_queue.py` | **Optimized processing.** Uses "First-In, First-Out" logic (Fair). | O(1) |
