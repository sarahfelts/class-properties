class Patient:
    def __init__(self, ssn, dob, insurance_num, first_name, last_name, address):
        self._ssn = ssn
        self._dob = dob
        self._insurance_num = insurance_num
        self._first_name = first_name
        self._last_name = last_name
        self._address = address
    
    @property
    def ssn(self):
        return self._ssn
    
    @property
    def dob(self):
        return self._dob
    
    @property
    def insurance_num(self):
        return self._insurance_num

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address
    
    @property
    def first_name(self):
        pass

    @property
    def last_name(self):
        pass

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
# cashew.ssn = "838-31-2256"

# Neither should this
# cashew.dob = "01-30-90"

# But printing either of them should work
print(cashew.ssn)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"