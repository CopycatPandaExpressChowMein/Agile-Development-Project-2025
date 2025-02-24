import unittest
from security import check_access, encrypt_data, validate_request

class TestSecurity(unittest.TestCase):

    def test_check_access(self):
        """Testar rollbaserad åtkomstkontroll."""
        self.assertTrue(check_access("admin", "delete"))  # Admin ska ha "delete"-åtkomst
        self.assertFalse(check_access("user", "delete"))  # User ska INTE ha "delete"-åtkomst
        self.assertTrue(check_access("user", "read"))  # User ska kunna läsa
        self.assertFalse(check_access("guest", "write"))  # Gäst får ej skriva

    def test_encrypt_data(self):
        """Testar SHA-256-kryptering (Samma input ska ge samma hash)."""
        hash1 = encrypt_data("password123")
        hash2 = encrypt_data("password123")
        hash3 = encrypt_data("differentPassword")
        self.assertEqual(hash1, hash2)  # Samma lösenord ska ge samma hash
        self.assertNotEqual(hash1, hash3)  # Olika lösenord ska ge olika hash

    def test_validate_request(self):
        """Testar validering av webbförfrågningar."""
        self.assertTrue(validate_request("https://example.com/resource"))  # Tillåten domän
        self.assertFalse(validate_request("https://evil-site.com/malware"))  # Blockerad domän
        self.assertFalse(validate_request("https://not-example.com/resource"))  # Subdomän som inte matchar

    def test_encrypt_data_uniqueness(self):
        """Testar att olika lösenord skapar olika hashvärden."""
        hashes = {encrypt_data(f"password{i}") for i in range(100)}
        self.assertEqual(len(hashes), 100)  # 100 unika lösenord ska ge 100 olika hash

if __name__ == "__main__":
    unittest.main()
