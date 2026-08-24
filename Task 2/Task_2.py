
def main():
    total = 0          
    count = 0          

    print("=== Expense Tracker ===")
    print("Enter an expense amount, or type 'quit' to stop.\n")

    while True:                                  
        raw_input_value = input("Enter expense (or 'quit'): ").strip()

        if raw_input_value.lower() == "quit":                break

        try:
            expense = int(raw_input_value)         
        except ValueError:                         
            print("  Invalid input — please enter a whole number.\n")
            continue

        total += expense                            
        count += 1
        print(f"  Added {expense}. Running total: {total}\n")

    # Phase 3: Output
    print("\n=== Summary ===")
    print(f"Transactions logged: {count}")
    print(f"Total Spent: {total}")


if __name__ == "__main__":
    main()