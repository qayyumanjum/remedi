from django.db import models

class Qualification(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_products():
        return Qualification.objects.all()
    
    
class Specialization(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_products():
        return Specialization.objects.all()
    
    
class Gender(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_products():
        return Gender.objects.all()


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Ensure this length is sufficient
    cnic = models.CharField(max_length=20)
    qualification = models.ForeignKey("Qualification", on_delete=models.CASCADE, default=1)
    specialization = models.ForeignKey("Specialization", on_delete=models.CASCADE, default=1)
    gender = models.ForeignKey("Gender", on_delete=models.CASCADE, default=1)

    
    
    
    def register(self):
        self.save()
    
    
    @staticmethod
    def get_Doctor_by_email(email):
        try:
            return Doctor.objects.get(email = email) 
        except:
            return False 
        
        
    def isExists(self):
        if Doctor.objects.filter(email = self.email):
            return True
        
        return False
    
    
class patient(models.Model):
    Name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    Gender = models.ForeignKey("Gender", on_delete=models.CASCADE, default=1)
    
    
    
    def register(self):
        self.save()
    
    
    @staticmethod
    def get_patient_by_email(email):
        try:
            return patient.objects.get(email = email) 
        except:
            return False 
        
        
    def isExists(self):
        if patient.objects.filter(email = self.email):
            return True
        
        return False