# create a MoringaEmployee class that has the following instance attributes
""" 
first_name
last_name
email (generate using the first and last name, make it lower case, format (@moringaschool.com))
salary
gender
dob
age (should be derived from the year of birth)
employment_date
"""

# create the following instance methods:
""" 
instance method that returns the current years of employment at moringa -> 2022 -> 2025 -> 3 years
instance method that returns the full name of the employee
instance met
instance method that returns the following message depending on the age of the employee
    - Above 25 yrs -> It's about time to consider marriage
    - Above 30 yrs -> It's about time to think about having Kids
    - Above 40 yrs -> It's time to consider retiring
    - Above 50 yrs -> Need to call it quits Old timer and retire
"""

from datetime import datetime

class MoringaEmployee:
    def __init__(self, first_name, last_name, salary, gender, dob, employment_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name.lower()}.{last_name.lower()}@moringaschool.com"
        self.salary = salary
        self.gender = gender
        self.dob = dob  # Format: 'YYYY-MM-DD'
        self.age = self.calculate_age()
        self.employment_date = employment_date  # Format: 'YYYY-MM-DD'

    def calculate_age(self):
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    def get_years_of_employment(self):
        employment = datetime.strptime(self.employment_date, "%Y-%m-%d")
        today = datetime.today()
        return today.year - employment.year - ((today.month, today.day) < (employment.month, employment.day))

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def life_advice(self):
        if self.age > 50:
            return "Need to call it quits Old timer and retire"
        elif self.age > 40:
            return "It's time to consider retiring"
        elif self.age > 30:
            return "It's about time to think about having Kids"
        elif self.age > 25:
            return "It's about time to consider marriage"
        else:
            return "Live your life and build your career!"

    def __str__(self):
        return (
            f"Name: {self.get_full_name()}\n"
            f"Email: {self.email}\n"
            f"Gender: {self.gender}\n"
            f"Age: {self.age}\n"
            f"Salary: {self.salary}\n"
            f"Employment Date: {self.employment_date}\n"
            f"Years of Employment: {self.get_years_of_employment()}\n"
            f"Advice: {self.life_advice()}"
        )
employee = MoringaEmployee(
    first_name="John",
    last_name="Smith",
    salary=85000,
    gender="Male",
    dob="1980-04-22",
    employment_date="2019-05-01"
)

print(employee)
#output = Name: John Smith, Email: john.smith@moringaschool.com, Gender: Male, Age: 45, Salary: 85000, Employment Date: 2019-05-01, Years of Employment: 6, Advice: It's time to consider retiring
