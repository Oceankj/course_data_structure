import pytest
from ..bank import Bank


class TestTask1:
    def test_linked_list_structure(self):
        """Test that the linked list maintains proper structure"""
        bank = Bank()
        bank.add_user("User1", "Address1", "111-11-1111", 100.0)
        bank.add_user("User2", "Address2", "222-22-2222", 200.0)
        bank.add_user("User3", "Address3", "333-33-3333", 300.0)

        current = bank.list.head
        user_ids = []
        while current.next != bank.list.tail:
            current = current.next
            user_ids.append(current.id)

        assert user_ids == [0, 1, 2]


class TestTask2:
    def test_add_user_basic(self):
        """Test adding a single user to the bank"""
        bank = Bank()
        bank.add_user("John Doe", "123 Main St", "123-45-6789", 1000.0)

        # Check that size increased
        assert bank.list.size == 1

        # Check that user was added after head
        first_user = bank.list.head.next
        assert first_user != bank.list.tail
        assert first_user.id == 0
        assert first_user.account.name == "John Doe"
        assert first_user.account.address == "123 Main St"
        assert first_user.account.ssn == "123-45-6789"
        assert first_user.account.balance == 1000.0

    def test_add_multiple_users(self):
        """Test adding multiple users to the bank"""
        bank = Bank()

        # Add first user
        bank.add_user("Alice", "123 Oak St", "111-11-1111", 500.0)
        assert bank.list.size == 1
        assert bank.list.head.next.id == 0

        # Add second user
        bank.add_user("Bob", "456 Pine St", "222-22-2222", 750.0)
        assert bank.list.size == 2

        # Check that users are in the correct order
        first_user = bank.list.head.next
        second_user = first_user.next
        assert first_user.id == 0
        assert second_user.id == 1
        assert first_user.account.name == "Alice"
        assert second_user.account.name == "Bob"


class TestTask3:
    def test_delete_user(self):
        """Test deleting users from the bank"""
        bank = Bank()
        # Add three users
        id0 = bank.add_user("User0", "Addr0", "000-00-0000", 100.0)
        id1 = bank.add_user("User1", "Addr1", "111-11-1111", 200.0)
        id2 = bank.add_user("User2", "Addr2", "222-22-2222", 300.0)
        assert bank.list.size == 3

        # Delete middle user
        is_success = bank.delete_user(id1)
        assert is_success is True
        assert bank.list.size == 2
        # Check that id1 is no longer in the list
        ids = []
        current = bank.list.head.next
        while current != bank.list.tail:
            ids.append(current.id)
            current = current.next
        assert ids == [0, 2]

        # Delete head user
        is_success = bank.delete_user(id0)
        assert is_success is True
        assert bank.list.size == 1
        ids = []
        current = bank.list.head.next
        while current != bank.list.tail:
            ids.append(current.id)
            current = current.next
        assert ids == [2]

        # Delete last user
        is_success = bank.delete_user(id2)
        assert is_success is True
        assert bank.list.size == 0
        # List should be empty (head.next is tail)
        assert bank.list.head.next == bank.list.tail
        assert bank.list.tail.prev == bank.list.head

        # Try deleting a non-existent user
        is_success = bank.delete_user(999)
        assert is_success is False

    def test_id_reusablity(self):
        """Test that user IDs are reused after deletion"""
        bank = Bank()
        # Add three users
        id0 = bank.add_user("User0", "Addr0", "000-00-0000", 100.0)
        id1 = bank.add_user("User1", "Addr1", "111-11-1111", 200.0)
        id2 = bank.add_user("User2", "Addr2", "222-22-2222", 300.0)

        assert id0 == 0
        assert id1 == 1
        assert id2 == 2

        bank.delete_user(id1)

        new_user_id = bank.add_user("User1", "Addr1", "111-11-1111", 200.0)
        assert new_user_id == id1


class TestTask4:
    def test_pay_user_to_user_success(self):
        """Test successful payment from one user to another"""
        bank = Bank()
        payer_id = bank.add_user(
            "Payer", "Payer Address", "111-11-1111", 500.0
        )
        payee_id = bank.add_user(
            "Payee", "Payee Address", "222-22-2222", 100.0
        )

        is_success = bank.payUserToUser(payer_id, payee_id, 200)
        assert is_success is True

        # Check balances
        payer_account = bank.get_user_account(payer_id)
        payee_account = bank.get_user_account(payee_id)
        assert payer_account.balance == 300.0
        assert payee_account.balance == 300.0

    def test_pay_user_to_user_insufficient_funds(self):
        """Test payment fails if payer has insufficient funds"""
        bank = Bank()
        payer_id = bank.add_user(
            "Payer", "Payer Address", "111-11-1111", 100.0
        )
        payee_id = bank.add_user(
            "Payee", "Payee Address", "222-22-2222", 100.0
        )

        is_success = bank.payUserToUser(payer_id, payee_id, 200)
        assert is_success is False

        # Balances should remain unchanged
        payer_account = bank.get_user_account(payer_id)
        payee_account = bank.get_user_account(payee_id)
        assert payer_account.balance == 100.0
        assert payee_account.balance == 100.0

    def test_pay_user_to_user_invalid_ids(self):
        """Test payment fails if payer or payee does not exist"""
        bank = Bank()
        payer_id = bank.add_user(
            "Payer", "Payer Address", "111-11-1111", 500.0
        )
        payee_id = bank.add_user(
            "Payee", "Payee Address", "222-22-2222", 100.0
        )

        # Invalid payer
        is_success = bank.payUserToUser(999, payee_id, 50)
        assert is_success is False

        # Invalid payee
        is_success = bank.payUserToUser(payer_id, 888, 50)
        assert is_success is False

    def test_pay_user_to_user_zero_amount(self):
        """
        Test payment of zero amount is allowed and does not change balances
        """
        bank = Bank()
        payer_id = bank.add_user(
            "Payer", "Payer Address", "111-11-1111", 100.0
        )
        payee_id = bank.add_user(
            "Payee", "Payee Address", "222-22-2222", 200.0
        )

        is_success = bank.payUserToUser(payer_id, payee_id, 0)
        assert is_success is False

        payer_node = bank.list.head.next
        payee_node = payer_node.next
        assert payer_node.account.balance == 100.0
        assert payee_node.account.balance == 200.0


class TestTask5:
    def test_get_median_id_single_user(self):
        """Test get_median_id returns the only user's ID"""
        bank = Bank()
        user_id = bank.add_user("Alice", "123 Main St", "111-11-1111", 100.0)
        assert bank.get_median_id() == user_id

    def test_get_median_id_odd_number_of_users(self):
        """Test get_median_id returns the middle ID for odd number of users"""
        bank = Bank()
        for i in range(5):
            bank.add_user(f"User{i}", f"Addr{i}", f"SSN{i}", 100 + i)
        assert bank.get_median_id() == 2

    def test_get_median_id_even_number_of_users(self):
        """
        Test get_median_id returns the first middle ID for even number of users
        """
        bank = Bank()
        for i in range(4):
            bank.add_user(f"User{i}", f"Addr{i}", f"SSN{i}", 100 + i)
        assert bank.get_median_id() == 2

    def test_get_median_id_after_deletion(self):
        """Test get_median_id after deleting users"""
        bank = Bank()
        for i in range(5):
            bank.add_user(f"User{i}", f"Addr{i}", f"SSN{i}", 100 + i)

        bank.delete_user(2)

        assert bank.get_median_id() == 3

    def test_get_median_id_empty_bank(self):
        """Test get_median_id raises ValueError if no users"""
        bank = Bank()
        with pytest.raises(ValueError):
            bank.get_median_id()


class TestTask6:
    def test_merge_accounts_success(self):
        """Test merging two accounts with the same user info"""
        bank = Bank()
        id1 = bank.add_user("John Doe", "123 Main St", "111-11-1111", 100.0)
        id2 = bank.add_user("John Doe", "123 Main St", "111-11-1111", 200.0)
        assert bank.list.size == 2

        is_success = bank.merge_accounts(id1, id2)
        assert is_success is True
        assert bank.list.size == 1

        account = bank.get_user_account(min(id1, id2))
        assert account.balance == 300.0

    def test_merge_accounts_different_users(self):
        """Test merging two accounts with different user info fails"""
        bank = Bank()
        id1 = bank.add_user("Alice", "Addr1", "111-11-1111", 100.0)
        id2 = bank.add_user("Bob", "Addr2", "222-22-2222", 200.0)
        assert bank.list.size == 2

        is_success = bank.merge_accounts(id1, id2)
        assert is_success is False
        assert bank.list.size == 2

    def test_merge_accounts_invalid_id(self):
        """Test merging with an invalid id returns False"""
        bank = Bank()
        id1 = bank.add_user("Alice", "Addr1", "111-11-1111", 100.0)

        is_success = bank.merge_accounts(id1, 999)
        assert is_success is False


class TestTask7:
    def test_merge_banks(self):
        """Test merging two banks combines users in order of id"""
        bank1 = Bank()
        bank2 = Bank()

        # Add users to bank1: ids 0, 1
        bank1.add_user("Alice", "Addr1", "111-11-1111", 100.0)
        bank1.add_user("Bob", "Addr2", "222-22-2222", 200.0)

        # Add users to bank2: ids 0, 1
        bank2.add_user("Charlie", "Addr3", "333-33-3333", 300.0)
        bank2.add_user("Diana", "Addr4", "444-44-4444", 400.0)

        merged_bank = Bank.merge_banks(bank1, bank2)

        # The merged bank should have 4 users
        assert merged_bank.list.size == 4

        ids = []
        curr = merged_bank.list.head.next
        while curr is not None and curr != merged_bank.list.tail:
            ids.append(curr.id)
            curr = curr.next
        assert sorted(ids) == [0, 1, 2, 3]

        # Check that all user data is present
        names = []
        curr = merged_bank.list.head.next
        while curr is not None and curr != merged_bank.list.tail:
            if curr.account is not None:
                names.append(curr.account.name)
            curr = curr.next
        assert names == ["Alice", "Bob", "Charlie", "Diana"]

        # Check balances
        balances = []
        curr = merged_bank.list.head.next
        while curr is not None and curr != merged_bank.list.tail:
            if curr.account is not None:
                balances.append(curr.account.balance)
            curr = curr.next
        assert balances == [100.0, 200.0, 300.0, 400.0]

    def test_merge_banks_empty_and_nonempty(self):
        """Test merging an empty bank with a non-empty bank"""
        bank1 = Bank()
        bank2 = Bank()
        bank2.add_user("Eve", "Addr5", "555-55-5555", 500.0)

        merged_bank = Bank.merge_banks(bank1, bank2)
        assert merged_bank.list.size == 1
        account = merged_bank.get_user_account(0)
        assert account.name == "Eve"
        assert account.balance == 500.0

    def test_merge_banks_both_empty(self):
        """Test merging two empty banks results in empty bank"""
        bank1 = Bank()
        bank2 = Bank()
        merged_bank = Bank.merge_banks(bank1, bank2)
        assert merged_bank.list.size == 0
        with pytest.raises(ValueError):
            merged_bank.get_median_id()

    def test_merge_not_sequence_banks(self):
        bank1 = Bank()
        bank2 = Bank()

        bank1.add_user("Anna", "AddrA", "111-11-1111", 100.0)  # id 0
        delete_id_a = bank1.add_user(
            "Ben", "AddrB", "222-22-2222", 200.0
        )  # id 1
        bank1.add_user("Cara", "AddrC", "333-33-3333", 300.0)  # id 2
        delete_id_b = bank1.add_user(
            "Dan", "AddrD", "444-44-4444", 400.0
        )  # id 3

        # Delete Ben (id 1) and Dan (id 3) to create gaps
        bank1.delete_user(delete_id_a)
        bank1.delete_user(delete_id_b)
        # Now bank1 has users with ids 0 (Anna) and 2 (Cara)

        # Add users to bank2 with overlapping and new users
        bank2.add_user("Eli", "AddrE", "555-55-5555", 500.0)  # id 0
        bank2.add_user(
            "Anna", "AddrA", "111-11-1111", 150.0
        )  # id 1 (same as Anna in bank1, but different id)
        bank2.add_user(
            "Cara", "AddrC", "333-33-3333", 350.0
        )  # id 2 (same as Cara in bank1, same id)
        bank2.add_user("Fay", "AddrF", "666-66-6666", 600.0)  # id 3

        # Now, merge the banks
        merged_bank = Bank.merge_banks(bank1, bank2)

        # Collect all user ids and names in merged bank
        ids = []
        names = []
        balances = []
        curr = merged_bank.list.head.next
        while curr is not None and curr != merged_bank.list.tail:
            ids.append(curr.id)
            if curr.account is not None:
                names.append(curr.account.name)
                balances.append(curr.account.balance)
            curr = curr.next

        # There should be 5 users
        assert merged_bank.list.size == 6
        assert ids == [0, 1, 2, 3, 4, 5]

        # Check names and balances by id
        id_to_name = dict(zip(ids, names))
        id_to_balance = dict(zip(ids, balances))

        assert id_to_name[0] == "Anna"
        assert id_to_balance[0] == 100.0

        assert id_to_name[1] == "Anna"
        assert id_to_balance[1] == 150.0

        assert id_to_name[2] == "Cara"
        assert id_to_balance[2] == 300.0

        assert id_to_name[3] == "Fay"
        assert id_to_balance[3] == 600.0

        assert id_to_name[4] == "Eli"
        assert id_to_balance[4] == 500.0

        assert id_to_name[5] == "Cara"
        assert id_to_balance[5] == 350.0
