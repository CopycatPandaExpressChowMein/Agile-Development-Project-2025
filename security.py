import hashlib
import hmac
import os
import json
#import requests

# 🎭 Rollbaserat åtkomstkontrollsystem (RBAC)
ROLE_PERMISSIONS = {
    "admin": ["read", "write", "delete"],  # Administratör har fullständig åtkomst
    "user": ["read", "write"],  # Vanlig användare kan läsa och skriva
    "guest": ["read"]  # Gästanvändare kan endast läsa
}

# 🔐 Funktion för att kontrollera behörighet baserat på roll och åtgärd
def check_access(role, action):
    """Kontrollerar om en roll har behörighet att utföra en viss åtgärd."""
    return action in ROLE_PERMISSIONS.get(role, [])

# 🔒 Enkel kryptering med SHA-256 (för lösenord eller känslig data)
def encrypt_data(data):
    """Krypterar data med SHA-256 hashing (envägskryptering)."""
    return hashlib.sha256(data.encode()).hexdigest()

# 🌐 Skydd mot Server-Side Request Forgery (SSRF)
ALLOWED_DOMAINS = ["example.com", "trusted-api.com"]  # Lista över betrodda domäner

# 🌍 Funktion för att validera externa förfrågningar
def validate_request(url):
    """Tillåter endast förfrågningar till betrodda domäner."""
    domain = url.split("/")[2]  # Extraherar domänen från URL:en
    return domain in ALLOWED_DOMAINS
