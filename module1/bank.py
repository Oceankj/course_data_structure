from .account import Account


class UserNode:
    def __init__(self, id: int | None = None, account: Account | None = None):
        self.account = account
        self.id = id
        self.next: UserNode | None = None
        self.prev: UserNode | None = None


class Bank:
    def __init__(self) -> None:
        self.head: UserNode = UserNode()
        self.tail: UserNode = UserNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size: int = 0

    def __get_node(self, id: int) -> UserNode:
        curr = self.head
        while curr.id != id and curr.next is not None:
            curr = curr.next
        if curr is self.tail:
            raise ValueError("user didn't exist")
        return curr

    def __delete_node(self, node: UserNode) -> None:
        if node.prev is None or node.next is None:
            raise ValueError("node is not properly linked")
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.size -= 1

    def __add_after(self, node: UserNode, new_node: UserNode) -> None:
        if node.next is None:
            raise ValueError("node is not properly linked")
        node.next.prev = new_node
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
        self.size += 1

    def get_user_account(self, user_id: int) -> Account:
        user_node = self.__get_node(user_id)
        if user_node is None or user_node.account is None:
            raise ValueError("invalid id")
        return user_node.account

    def add_user(
        self, name: str, address: str, ssn: str, initial_deposit: float
    ) -> int:
        last_id = -1
        curr_node = self.head
        while (
            curr_node is not None
            and curr_node.next is not None
            and curr_node.next.id is not None
            and last_id == curr_node.next.id - 1
        ):
            last_id = curr_node.next.id
            curr_node = curr_node.next

        new_id = last_id + 1
        new_user_node = UserNode(
            new_id, Account(name, address, ssn, initial_deposit)
        )
        # Insert before tail (at the end)
        self.__add_after(curr_node, new_user_node)
        return new_id

    def delete_user(self, id: int) -> bool:
        try:
            user_node = self.__get_node(id)
            self.__delete_node(user_node)
        except ValueError:
            return False
        else:
            return True

    def payUserToUser(self, payer_ID: int, payee_ID: int, amount: int) -> bool:
        if amount == 0:
            return False

        try:
            payer_node = self.__get_node(payer_ID)
            if (
                payer_node.account is not None
                and payer_node.account.balance < amount
            ):
                return False

            payee_node = self.__get_node(payee_ID)
            if payer_node.account is None or payee_node.account is None:
                return False

        except ValueError:
            return False

        payer_node.account.balance -= amount
        payee_node.account.balance += amount
        return True

    def get_median_id(self) -> int:
        if self.size == 0:
            raise ValueError("Don't have any user.")

        median_count = self.size // 2

        if self.head.next is None:
            raise ValueError("Invalid list structure")
        curr: UserNode = self.head.next

        while median_count > 0:
            if curr.next is None:
                raise ValueError("Invalid list structure")
            curr = curr.next
            median_count -= 1

        if curr.id is None:
            raise ValueError("Invalid node")
        return curr.id

    def __is_same_user(self, node1: UserNode, node2: UserNode) -> bool:
        if node1.account is None or node2.account is None:
            raise ValueError("invalid nodes")
        return (
            node1.account.name == node2.account.name
            and node1.account.address == node2.account.address
            and node1.account.ssn == node2.account.ssn
        )

    def merge_accounts(self, id1: int, id2: int) -> bool:
        if id1 > id2:
            id1, id2 = id2, id1
        try:
            node1 = self.__get_node(id1)
            node2 = self.__get_node(id2)
        except ValueError:
            return False

        if not (self.__is_same_user(node1, node2)):
            return False

        if node1.account is None or node2.account is None:
            raise ValueError("invalid nodes")

        node1.account.balance += node2.account.balance
        self.__delete_node(node2)
        return True

    @staticmethod
    def merge_banks(bank1: "Bank", bank2: "Bank") -> "Bank":
        new_bank = Bank()
        new_curr = new_bank.head

        curr1 = bank1.head.next
        curr2 = bank2.head.next

        def append_from(node: "UserNode") -> None:
            if node.account is None:
                raise ValueError("Invalid node: account is None")
            new_bank.add_user(
                node.account.name,
                node.account.address,
                node.account.ssn,
                node.account.balance,
            )

        while curr1 is not None and curr2 is not None:
            if curr1.id is None or curr2.id is None:
                break

            if curr1.id < curr2.id:
                append_from(curr1)
                if new_curr.next is None:
                    raise ValueError("new_curr.next is None")
                new_curr = new_curr.next
                curr1 = curr1.next
            elif (
                curr2.id is not None
                and curr1.id is not None
                and curr2.id > curr1.id
            ):
                append_from(curr2)
                if new_curr.next is None:
                    raise ValueError("new_curr.next is None")
                new_curr = new_curr.next
                curr2 = curr2.next
            else:
                append_from(curr1)
                if curr2.account is None:
                    raise ValueError("curr2.account is None")
                bank1.add_user(
                    curr2.account.name,
                    curr2.account.address,
                    curr2.account.ssn,
                    curr2.account.balance,
                )
                curr1 = curr1.next
                curr2 = curr2.next

        while curr1 is not None and curr1.next is not None:
            append_from(curr1)
            curr1 = curr1.next

        while curr2 is not None and curr2.next is not None:
            if curr2.account is None:
                raise ValueError("curr2.account is None")
            append_from(curr2)
            curr2 = curr2.next

        return new_bank
