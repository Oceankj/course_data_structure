# Bank Class Assignment

## Task Description

Consider a commercial bank, **Bank of Orange County**, where anyone can open bank accounts. To open a bank account, the following information is needed:

- **Name**
- **Address**
- **Social Security Number**
- **Initial deposit amount**

The bank assigns a **unique ID** whenever a user opens an account. The unique ID is incrementally assigned to new users, meaning if the last new user’s ID is `x`, the next user will have a unique ID of `x + 1`. If a user closes their account, the unique ID can be reclaimed and re-assigned to future new users.

---

**You are to write a class for the Bank of Orange County to complete the following tasks:**

> **Note:** Write sample test cases to validate your implementation for each task.

---

### Tasks

#### **Task 1**

- Model the list of users as a **linked list** where each account is a node in the list.
- Users must be **sorted by their ID** in the linked list.

#### **Task 2**

- Write a method/function `addUser(user)` that adds a new user.
- The new user should have a unique ID that is either:
  - 1 more than the last unique ID, **or**
  - Equal to the first freed-up unique ID (from a user closing their account), **whichever comes first**.

#### **Task 3**

- Write a method/function `deleteUser(ID)` that deletes an existing user.
- Free up the unique ID while deleting the user.
- This unique ID can be re-assigned to a future new user.

#### **Task 4**

- Write a method/function `payUserToUser(payer_ID, payee_ID, amount)` that lets the user with `payer_ID` pay the user with `payee_ID` by the specified amount.

#### **Task 5**

- Write a method/function `getMedianID()` that returns the **median** of all the account IDs (i.e., the middle node of the linked list).
- If the number of nodes is even, you can:
  - Return the average of the IDs of the middle two nodes (**return float**), **or**
  - Return the first middle node’s ID.

#### **Task 6**

- Write a method/function `mergeAccounts(ID1, ID2)` that merges two accounts into one.
- This function only merges two accounts if they are owned by the **same person** (same name, address, and SSN).
- While merging:
  - Sum the two balances,
  - Delete the account with the **biggest unique ID** of the two,
  - Keep the account with the **smallest unique ID** with the new balance.

#### **Task 7**

- Imagine another bank, **Bank of Los Angeles**, which uses the same class as the Bank of Orange County.
- These two banks have decided to merge into a new bank, **Bank of Southern California**.
- Write a method `mergeBanks(bankOfOrangeCounty, bankOfLosAngeles)` to merge the two linked lists into one.
- If both lists have a node with the same ID:
  - Create a new ID for one of the duplicates and add it to the new list.
  - While creating the new ID, you must maintain the incremental property.

---
