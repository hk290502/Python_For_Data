class Envitia():
    def __init__(self, speciality, location, salary):
        self.speciality = speciality
        self.location = location
        self.__salary = salary  # private attribute

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = value

    def __str__(self):
        return f"My speciality is {self.speciality} at {self.location}."

class Engineer(Envitia):
    def salary_band(self):
        if self.salary == 120000:
            return "Above Average for an Engineer at Envitia."
        else:
            return "Below Average for an Engineer at Envitia."

    def __str__(self):
        return f"My speciality is {self.speciality} within the Engineering Dept at {self.location}."

class Consultant(Envitia):
    def salary_band(self):
        if self.salary == 100000:
            return "They Earn Above Average for a Consultant at Envitia."
        else:
            return "They Earn Below Average for a Consultant at Envitia."

    def __str__(self):
        return f"My speciality is {self.speciality} within the Consulting Dept at {self.location}."


c = Consultant("Platforming", "Mayfair", 100000)
e = Engineer("C++", "Camden", 85000)
t = Envitia("AI Engineering", "Green Park", 160000)

print(c)
print(c.salary_band())
print(f"Consultant salary: {c.salary}")

print(e)
print(e.salary_band())
print(f"Engineer salary: {e.salary}")

print(t)
print(f"Base salary: {t.salary}")

# Demonstrating the setter
print("\n-- Salary update --")
c.salary = 110000
print(f"Updated consultant salary: {c.salary}")
print(c.salary_band())
