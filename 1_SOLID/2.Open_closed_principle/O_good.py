from abc import ABC, abstractmethod

class Invoice(ABC):
    def __init__(self,name: str):
        self.name = name
    
    @abstractmethod
    def save(self,):
        pass

class DBSave(Invoice):
    
    def save(self):
        print(f"Saved to DB: {self.name}")

class FileSave(Invoice):
    
    def save(self):
        print(f"Saved as File: {self.name}")

class CloudSave(Invoice): # This will throw an error since save() is not instantiated.
    
    def delete(self):
        print(f"deleted")


f = FileSave("Adhi")
d = DBSave("rahul")
c = CloudSave("Sample")

f.save()
d.save()
