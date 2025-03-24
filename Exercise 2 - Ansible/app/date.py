from datetime import datetime

def print_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    print(f"Today's date is: {current_date}")

if __name__ == "__main__":
    print_date()
