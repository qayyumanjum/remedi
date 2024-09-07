# Remedic: Patient Management System

## Description
Remedic is a web-based platform designed to manage patient data, appointments, medical records, and billing in a secure and efficient manner.

## Features
- **Authentication**: Multi-factor authentication for admins and patients.
- **Data Encryption**: Secure encryption for sensitive information.
- **Appointment Booking**: Doctors and patients can manage appointments seamlessly.
- **Billing System**: Secure billing with integration to Stripe.

## Installation
### Clone the repository
```bash
git clone https://github.com/qayyumanjum/remedic.git
```
pip install -r requirements.txt

### Technology Stack
**Frontend**: 
- HTML, CSS, JavaScript, Bootstrap

**Backend**:
- Python (Django) 

**Database**:
- MySQL | RDBMS

**Authentication and Security**:
- Django Allauth / Flask-Security / Auth0
- PyCryptodome / bcrypt for data encryption

**Payment Gateway**:
- Stripe / Razorpay

**Cloud Services** (Optional):
- AWS (for hosting, AWS Key Management Service for encryption)
