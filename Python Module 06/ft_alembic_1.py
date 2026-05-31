from elements import create_water 

if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Using:")
    print("'from... import...' structure to access elements.py")
    
    resultado = create_water()
    print(f"Testing create_water: {resultado}")