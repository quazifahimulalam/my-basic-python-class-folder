import datetime
import calendar

def print_menu():
    print("\nDate and callender utility")
    print("1. show todays date")
    print("2. calculate days between two dates")
    print("3. show callender for a month")
    print("4. show current time of dhaka")
    print("5. show weekdays")
    print("6. exit")
    
    
def show_today():
    today = datetime.today()
    print(f"todays date: {today}")
    
def days_between():
    d1 = input("enter first date (YYYY-MM-DD):")
    d2 = input("enter second date (YYYY-MM-DD):")
    try:
        date1 = datetime.datetime.strptime(d1,"%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(d2,"%Y-%m-%d").date()
        diff = abs((date2-date1).days)
        print(f"days between: {diff}")
    except ValueError:
        print("invalid date format")
        
def show_weekday():
    d = input("enter a date (YYYY-MM-DD):")
    try:
        date_obj = datetime.datetime.strptime(d,"%Y-%m-%d").date()
        print(f"{d} is a {date_obj.strftime('%A')}")
    except ValueError:
        print("invalid date format")
        
        
def show_month_calendar():
    try:
        year = int(input("enter year (e.g. 2024):"))
        month = int(input("enter month (1-12):"))
        print(calendar.month(year , month))
    except ValueError:
        print("invalid input")
        
def show_time():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours = 6)
    print(f"current time in dhaka : {now.strftime('%Y-%m-%d' '%H:%M:%S')}")
        
def main():
    while True:
        print_menu()
        choice = input("chose an option (1-6)")
        if choice == '1':
            show_today()
        elif choice == '2':
            days_between()
        elif choice == '3':
            show_month_calendar()
        elif choice == '4':
            show_time()
        elif choice == '5':
            show_weekday()
        elif choice == '6':
            print("goodbye")
            break
        else:
            print("invalid choice")
            
            
if __name__ == "__main__":
    main()