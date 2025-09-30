from .bank import Bank, UserNode

bank = Bank()
bank.add_user("Alice", "123 Oak St", "111-11-1111", 500.0)
bank.add_user("Bob", "456 Pine St", "222-22-2222", 750.0)

curr: UserNode | None = bank.head
while curr is not None:
    print(curr.id)
    curr = curr.next
