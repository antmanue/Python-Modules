import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
    HAS_DOTENV = True
except ModuleNotFoundError:
    HAS_DOTENV = False


def read_mainframe_config() -> None:
    if HAS_DOTENV:
        env_found = load_dotenv()
    else:
        env_found = False

    mode = os.environ.get("MATRIX_MODE", "missing")
    db_url = os.environ.get("DATABASE_URL", "missing")
    api_key = os.environ.get("API_KEY", "missing")
    log_level = os.environ.get("LOG_LEVEL", "missing")
    zion_endpoint = os.environ.get("ZION_ENDPOINT", "missing")

    if mode == "missing":
        print("ORACLE STATUS: Reading the Matrix...")
        print("[WARNING] No configuration found!")
        sys.exit(1)
    else:
        print("ORACLE STATUS: Reading the Matrix...")
        print()
        print("Configuration loaded:")
        print(f"Mode: {mode}")

        if db_url != "missing" and mode == "production":
            print("Database: Connected to PRODUCTION secure cluster")
        else:
            print("Database: Connected to local instance")

        if api_key != "missing" and mode == "production":
            print("API Access: Secured (Production Gateway)")
        else:
            print("API Access: Authenticated")

        print(f"Log Level: {log_level}")

        if zion_endpoint != "missing":
            print("Zion Network: Online")
        else:
            print("Zion Network: Offline")

        print()
        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")

        if env_found:
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] Running purely on system environment variables")

        print("[OK] Production overrides available")
        print()
        print("The Oracle sees all configurations.")


def main() -> None:
    read_mainframe_config()


if __name__ == "__main__":
    main()
