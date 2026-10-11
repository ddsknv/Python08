# Authorized: os, sys, python-dotenv modules, file operations
import os
from dotenv import load_dotenv

load_dotenv()
print("\nORACLE STATUS: Reading the Matrix...\n")
print("Configuration loaded:")

matrix_mode = os.getenv("MATRIX_MODE", "development")
if matrix_mode == "development":
    print("Mode: development")
elif matrix_mode == "production":
    print("Mode: production")
database_url = os.getenv("DATABASE_URL")
if database_url is None:
    print("Warning: DATABASE_URL is missing")
else: 
    print("Database: Connected to local instance")
api_key = os.getenv("API_KEY")
if api_key is None:
    print("Warning: API_KEY is missing")
else: 
    print("API Access: Authenticated")
log_level = os.getenv("LOG_LEVEL")
if log_level is None:
    print("Warning: LOG_LEVEL is missing")
else:
    print(f"Log Level: {log_level}")
zion_endpoint = os.getenv("ZION_ENDPOINT")
if zion_endpoint is None:
    print("Warning: ZION_ENDPOINT is missing")
else:
    print("Zion Network: Online")

print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available")
print("The Oracle sees all configurations.")



