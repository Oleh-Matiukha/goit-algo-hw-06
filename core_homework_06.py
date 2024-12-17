from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): # Class for storing contact name.
    def __init__(self, value):
        super().__init__(value)

class Phone(Field): # Class for storing phone numbers.
    def __init__(self, value):
        if len(value) == 10 and value.isdigit(): # Format validation (10 digits).
            super().__init__(value)
        else: raise ValueError 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone): # Method for adding.
        self.phones.append(Phone(phone))

    def find_phone(self, phone): # Method for finding Phone objects.
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def remove_phone(self, phone): # Method for removal.
        self.phones.remove(self.find_phone(phone))

    def edit_phone(self, old_phone, new_phone): # Method for editing.
        if self.find_phone(old_phone) and Phone(new_phone): # If the old_phone exists and the new_phone is valid.
            self.phones.remove(self.find_phone(old_phone))
            self.add_phone(new_phone)
        else:
            raise ValueError

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record): # Method that adds a record to "self.data".
        self.data[record.name.value] = record

    def find(self, name): # Method that finds a record by name.
        return self.data.get(name)
    
    def delete(self, name): # Method that deletes a record by name.
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
