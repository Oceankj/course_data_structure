import pytest
from ..bank import Bank, UserNode
from ..account import Account


class TestBank:
    """Test cases for the Bank class"""

    def test_bank_initialization(self):
        """Test that Bank initializes correctly with empty linked list"""
        bank = Bank()
        assert bank.size == 0
        assert bank.head.next == bank.tail
        assert bank.tail.prev == bank.head
        assert bank.head.prev is None
        assert bank.tail.next is None

    def test_user_node_creation(self):
        """Test UserNode creation with and without parameters"""
        # Test with parameters
        account = Account("Test User", "Test Address", "123-45-6789", 100.0)
        node = UserNode(5, account)
        assert node.id == 5
        assert node.account == account
        assert node.next is None
        assert node.prev is None

        # Test without parameters
        empty_node = UserNode()
        assert empty_node.id is None
        assert empty_node.account is None
        assert empty_node.next is None
        assert empty_node.prev is None


class TestTask1:
    def test_linked_list_structure(self):
        """Test that the linked list maintains proper structure"""
        bank = Bank()
        bank.add_user("User1", "Address1", "111-11-1111", 100.0)
        bank.add_user("User2", "Address2", "222-22-2222", 200.0)
        bank.add_user("User3", "Address3", "333-33-3333", 300.0)

        current = bank.head
        user_ids = []
        while current.next != bank.tail:
            current = current.next
            user_ids.append(current.id)

        assert user_ids == [0, 1, 2]


class TestTask2:
    def test_add_user_basic(self):
        """Test adding a single user to the bank"""
        bank = Bank()
        bank.add_user("John Doe", "123 Main St", "123-45-6789", 1000.0)

        # Check that size increased
        assert bank.size == 1

        # Check that user was added after head
        first_user = bank.head.next
        assert first_user != bank.tail
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
        assert bank.size == 1
        assert bank.head.next.id == 0

        # Add second user
        bank.add_user("Bob", "456 Pine St", "222-22-2222", 750.0)
        assert bank.size == 2

        # Check that users are in the correct order
        first_user = bank.head.next
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
        assert bank.size == 3

        # Delete middle user
        is_success = bank.delete_user(id1)
        assert is_success is True
        assert bank.size == 2
        # Check that id1 is no longer in the list
        ids = []
        current = bank.head.next
        while current != bank.tail:
            ids.append(current.id)
            current = current.next
        assert ids == [0, 2]

        # Delete head user
        is_success = bank.delete_user(id0)
        assert is_success is True
        assert bank.size == 1
        ids = []
        current = bank.head.next
        while current != bank.tail:
            ids.append(current.id)
            current = current.next
        assert ids == [2]

        # Delete last user
        is_success = bank.delete_user(id2)
        assert is_success is True
        assert bank.size == 0
        # List should be empty (head.next is tail)
        assert bank.head.next == bank.tail
        assert bank.tail.prev == bank.head

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

        payer_node = bank.head.next
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
        assert bank.size == 2

        is_success = bank.merge_accounts(id1, id2)
        assert is_success is True
        assert bank.size == 1

        account = bank.get_user_account(min(id1, id2))
        assert account.balance == 300.0

    def test_merge_accounts_different_users(self):
        """Test merging two accounts with different user info fails"""
        bank = Bank()
        id1 = bank.add_user("Alice", "Addr1", "111-11-1111", 100.0)
        id2 = bank.add_user("Bob", "Addr2", "222-22-2222", 200.0)
        assert bank.size == 2

        is_success = bank.merge_accounts(id1, id2)
        assert is_success is False
        assert bank.size == 2

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
        assert merged_bank.size == 4

        ids = []
        curr = merged_bank.head.next
        while curr is not None and curr != merged_bank.tail:
            ids.append(curr.id)
            curr = curr.next
        assert sorted(ids) == [0, 1, 2, 3]

        # Check that all user data is present
        names = []
        curr = merged_bank.head.next
        while curr is not None and curr != merged_bank.tail:
            if curr.account is not None:
                names.append(curr.account.name)
            curr = curr.next
        assert names == ["Alice", "Bob", "Charlie", "Diana"]

        # Check balances
        balances = []
        curr = merged_bank.head.next
        while curr is not None and curr != merged_bank.tail:
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
        assert merged_bank.size == 1
        account = merged_bank.get_user_account(0)
        assert account.name == "Eve"
        assert account.balance == 500.0

    def test_merge_banks_both_empty(self):
        """Test merging two empty banks results in empty bank"""
        bank1 = Bank()
        bank2 = Bank()
        merged_bank = Bank.merge_banks(bank1, bank2)
        assert merged_bank.size == 0
        with pytest.raises(ValueError):
            merged_bank.get_median_id()
