from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Doctor, Gender, Qualification, Specialization, patient
from django.views import View

# Home View
class Home(View):
    def get(self, request):
        return render(request, 'index.html')


class Options(View):
    def get(self, request):
        return render(request, 'ChooseSignup.html')

# Patient Signup View
class PSignup(View):
    def get(self, request):
        # Get options for genders
        
        print("\n\nPage relaoded\n\n")
        genders = Gender.objects.all()
        return render(request, 'Psignup.html', {'genders': genders})
    
    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        gender_id = postData.get('gender')  # Assuming gender is passed as an ID
        
        error_message = None
        
        values = {
            "name": name,
            "phone": phone,
            "email": email,
            "password": password
        }
        
        # Create a new Patient instance
        patient_instance = patient(
            Name=name,
            phone=phone,
            email=email,
            password=password,
            Gender_id=gender_id  # Using Gender_id to reference the Gender model
        )
        
        error_message = self.validations(patient_instance)
        
        if not error_message:
            patient_instance.password = make_password(patient_instance.password)
            print("\n\nHashed Password:", patient_instance.password)
            patient_instance.register()
            print("\n\nPatient created:", patient_instance)
            return redirect('login')
        else:
            return render(request, 'Psignup.html', {'error': error_message, 'values': values, 'genders': Gender.objects.all()})

    def validations(self, patient_instance):
        # Form validations
        error_message = None
        if not patient_instance.Name:
            error_message = "Name is required!"
        elif len(patient_instance.Name) <= 2:
            error_message = "Name must be longer than or equal to 2 characters!"
        elif not patient_instance.phone:
            error_message = "Phone number is required!"
        elif len(patient_instance.phone) <= 10:
            error_message = "Phone number must be longer than or equal to 10 characters!"
        elif not patient_instance.email:
            error_message = "Email is required!"
        elif len(patient_instance.email) <= 5:
            error_message = "Email must be longer than or equal to 5 characters!"
        elif patient_instance.isExists():
            error_message = "This email already exists! Please try another one."
        elif not patient_instance.password:
            error_message = "Password is required!"
        elif len(patient_instance.password) <= 10:
            error_message = "Password should have at least 10 characters."
        
        return error_message

class DoctorSignup(View):
    def get(self, request):
        qualifications = Qualification.objects.all()
        specializations = Specialization.objects.all()
        genders = Gender.objects.all()
        
        return render(request, 'Dsignup.html', {
            'qualifications': qualifications,
            'specializations': specializations,
            'genders': genders
        })  
    
    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        cnic = postData.get('cnic')
        qualification_id = postData.get('qualification')
        specialization_id = postData.get('specialization')
        gender_id = postData.get('gender')
        
        error_message = None
        
        values = {
            "name": name,
            "phone": phone,
            "email": email,
            "password": password,
            "cnic": cnic
        }
        
        doctor_instance = Doctor(
            name=name,
            phone=phone,
            email=email,
            password=make_password(password),
            cnic=cnic,
            qualification_id=qualification_id,
            specialization_id=specialization_id,
            gender_id=gender_id
        )
        
        error_message = self.validations(doctor_instance)
        
        if not error_message:
            doctor_instance.register()
            return redirect('login')
        else:
            return render(request, 'Dsignup.html', {
                'error': error_message, 
                'values': values,
                'qualifications': Qualification.objects.all(),
                'specializations': Specialization.objects.all(),
                'genders': Gender.objects.all()
            })

    def validations(self, doctor_instance):
        error_message = None
        if not doctor_instance.name:
            error_message = "Name is required!"
        elif len(doctor_instance.name) <= 2:
            error_message = "Name must be longer than or equal to 2 characters!"
        elif not doctor_instance.phone:
            error_message = "Phone number is required!"
        elif len(doctor_instance.phone) <= 10:
            error_message = "Phone number must be longer than or equal to 10 characters!"
        elif not doctor_instance.email:
            error_message = "Email is required!"
        elif len(doctor_instance.email) <= 5:
            error_message = "Email must be longer than or equal to 5 characters!"
        elif doctor_instance.isExists():
            error_message = "This email already exists! Please try another one."
        elif not doctor_instance.password:
            error_message = "Password is required!"
        elif len(doctor_instance.password) <= 10:
            error_message = "Password should have at least 10 characters."
        elif not doctor_instance.cnic:
            error_message = "CNIC is required!"
        elif len(doctor_instance.cnic) <= 13:
            error_message = "CNIC should be exactly 13 characters."
        
        return error_message

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        
        # Check if the email belongs to a Doctor
        doctor = Doctor.get_Doctor_by_email(email)
        if doctor:
            user = doctor
        else:
            # Check if the email belongs to a Patient
            patient_instance = patient.get_patient_by_email(email)
            if patient_instance:
                user = patient_instance
            else:
                user = None
        
        if user:
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                return redirect('homepage')  # Ensure 'homepage' is the correct URL name for your home page
            else:
                error_message = "Invalid email or password"
        else:
            error_message = "Invalid Email or Password!"
        
        return render(request, 'login.html', {'error': error_message})

# Logout View
def logout(request):
    request.session.clear()
    return redirect('login')
