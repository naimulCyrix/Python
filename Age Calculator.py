from datetime import datetime

def calculate_age(birthdate):
    # Assuming the input format is "YYYY-MM-DD"
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the difference in years, months, and days
    age_years = current_date.year - birthdate.year
    age_months = current_date.month - birthdate.month
    age_days = current_date.day - birthdate.day
    
    # Adjust for negative values in months and days
    if age_days < 0:
        # Borrow a month
        age_months -= 1
        # Calculate the correct number of days
        age_days += 30  # Assuming a month is 30 days
    
    if age_months < 0:
        # Borrow a year
        age_years -= 1
        # Calculate the correct number of months
        age_months += 12
    
    return age_years, age_months, age_days

# Example usage:
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
age = calculate_age(birthdate_input)
print(f"Your age is {age[0]} years, {age[1]} months, and {age[2]} days.")
