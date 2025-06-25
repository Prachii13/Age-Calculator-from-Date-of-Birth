from datetime import datetime, date

def calculate_age(birth_date):
    today = date.today()
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    if age_days < 0:
        age_days += 30
        age_months -= 1

    if age_months < 0:
        age_months += 12
        age_years -= 1

    total_days = (today - birth_date).days

    return age_years, age_months, age_days, total_days

def main():
    print("📅 Age Calculator")
    dob_str = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(dob_str, "%Y-%m-%d").date()
        years, months, days, total = calculate_age(birth_date)
        print(f"\n🎉 You are {years} years, {months} months, and {days} days old.")
        print(f"📆 Total days lived: {total} days")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
