def is_leap_year(year):
    """Check if the given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
    """Return the number of days in a given month of a year."""
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

def get_day_of_week(year, month, day):
    """Get day of week using corrected Zeller's congruence algorithm."""
    if month < 3:
        month += 12
        year -= 1
    
    k = year % 100
    j = year // 100
    
    h = (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    

    return (h + 6) % 7

def print_calendar(year):
    """Print the calendar for the entire year."""
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    
    print(f"\n{year:^50}")
    print("=" * 50)
    
    for month_num in range(1, 13):

        first_day = get_day_of_week(year, month_num, 1)
        

        print(f"\n{months[month_num-1]} {year}")
        print(" ".join(days))
        print("-" * 28)
        

        print("   " * first_day, end="")
        

        days_in_month = get_days_in_month(month_num, year)
        

        current_day = first_day
        for day in range(1, days_in_month + 1):
            print(f"{day:3}", end="")
            current_day = (current_day + 1) % 7
            if current_day == 0:
                print()  
        
        if current_day != 0:
            print()  
        print()

def main():
    try:
        year = int(input("Enter a year: "))
        if year < 1:
            print("Please enter a valid year (greater than 0)")
            return
        print_calendar(year)
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()
