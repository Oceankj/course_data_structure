from ..bank import Bank, UserNode
from ..account import Account


class TestBank:
    """Test cases for the Bank class"""

    def test_bank_initialization(self):
        """Test that Bank initializes correctly with empty linked list"""
        bank = Bank()
        assert bank.list.size == 0
        assert bank.list.head.next == bank.list.tail
        assert bank.list.tail.prev == bank.list.head
        assert bank.list.head.prev is None
        assert bank.list.tail.next is None

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
