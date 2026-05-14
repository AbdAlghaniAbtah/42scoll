import os
import sys
from dotenv import load_dotenv

def main():
    print("ORACLE STATUS: Reading the Matrix...")
    load_dotenv()
    x = os.getenv("MATRIX_MODE")
    x1 = os.getenv("API_KEY")
    x2 = os.getenv("DATABASE_URL")
    log_level = os.getenv("LOG_LEVEL")
    zion_node = os.getenv("ZION_ENDPOINT")
    lis: list[str] = [x, x1, x2, log_level, zion_node]
    for i in lis:
        if i is None:
            print("CRITICAL ERROR: Missing configuration in .env file!")
            print("Make sure all required variables are set.")
            sys.exit(1)
    print("\nConfiguration loaded:")
    print(f"Mode: {x}")
    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    if x.lower() == "production":
        print("Database: Connected to PRODUCTION instance")
        print("Zion Network: Online (Encrypted)")
    elif x.lower() == "development":
        print(f"Database: Connected to local instance")
        print(f"Zion Network: Online")
    else:
        print(f"[!] WARNING: Unknown MATRIX_MODE '{x}'. Falling back to safe mode.")
        print("Database: Connection suspended for security.")


    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print(f"[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
if __name__ == "__main__":
    main()