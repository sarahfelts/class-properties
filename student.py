class Student():
    def __init__(self, first_name="", last_name="", age=0, cohort_number=0):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._cohort_number = cohort_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("That's not an age, goober.")
    
    @property
    def cohort_number(self):
        return self._cohort_number
    
    @cohort_number.setter
    def cohort_number(self, value):
        self._cohort_number = value
    
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in Cohort {self.cohort_number}."

sarah = Student()
sarah.first_name = "Sarah"
sarah.last_name = "Felts"
sarah.age = 31
sarah.cohort_number = 25

print(sarah)