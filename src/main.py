#!/usr/bin/env python3
from src.strength_checker import PasswordStrengthChecker

def main():
    checker = PasswordStrengthChecker()
    
    print("Password Strength Checker")
    print("=" * 30)
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ").strip()
        
        if password.lower() == 'quit':
            break
            
        if not password:
            print("Please enter a password.")
            continue
        
        result = checker.check_strength(password)
        
        print(f"\nPassword: {'*' * len(password)}")
        print(f"Strength: {result['strength']} (Score: {result['score']}/10)")
        print("\nFeedback:")
        for item in result['feedback']:
            print(f"  {item}")

if __name__ == "__main__":
    main()
