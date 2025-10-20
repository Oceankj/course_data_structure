import pytest
from ..account import Account


class TestAccount:
    def test_account_creation(self):
        """Test Account creation and properties"""
        account = Account("Jane Smith", "789 Elm St", "987-65-4321", 2500.0)
        assert account.name == "Jane Smith"
        assert account.address == "789 Elm St"
        assert account.ssn == "987-65-4321"
        assert account.balance == 2500.0

    def test_edge_cases(self):
        """Test edge cases for add_user method"""
        # Test adding user with negative initial deposit
        with pytest.raises(ValueError):
            Account("Negative Balance", "456 Test St", "111-11-1111", -100.0)
