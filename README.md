# 🏥 Healthcare Backend API

A scalable backend system for managing healthcare records — including patients, doctors, and their mappings — built using Django, Django REST Framework, and PostgreSQL with secure JWT authentication.

---

## 🚀 Features

* 🔐 JWT Authentication (Register & Login)
* 👤 Patient Management (CRUD operations)
* 👨‍⚕️ Doctor Management (CRUD operations)
* 🔗 Patient-Doctor Mapping
* 🛡 Secure endpoints with authentication & permissions
* ✅ Input validation & error handling
* ⚙️ Environment-based configuration

---

## 🛠 Tech Stack

* **Python 3.10+**
* **Django 4.2**
* **Django REST Framework 3.14**
* **PostgreSQL**
* **djangorestframework-simplejwt (JWT Auth)**
* **python-dotenv**

---

## 📁 Project Structure

```
healthcare_backend/
├── healthcare_backend/     # Core Django project (settings, urls, wsgi)
├── authentication/         # Register & Login APIs
├── patients/               # Patient CRUD APIs
├── doctors/                # Doctor CRUD APIs
├── mappings/               # Patient-Doctor mapping APIs
├── manage.py
├── requirements.txt
└── .env.example
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/healthcare-backend.git
cd healthcare-backend
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env`:

```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Create PostgreSQL database

```sql
CREATE DATABASE healthcare_db;
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Run server

```bash
python manage.py runserver 8001
```

👉 API will run at:
**http://127.0.0.1:8001/**

---

## 🔐 Authentication

All protected endpoints require:

```
Authorization: Bearer <access_token>
```

---

## 🧪 Quick Test Flow

1. Register a user
2. Login to get JWT token
3. Add token in Authorization header (Bearer Token)
4. Test all protected APIs

---

## 🔑 Authentication APIs

| Method | Endpoint              | Description            |
| ------ | --------------------- | ---------------------- |
| POST   | `/api/auth/register/` | Register a new user    |
| POST   | `/api/auth/login/`    | Login & get JWT tokens |

### Register Request

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "StrongPass123",
  "password2": "StrongPass123"
}
```

### Login Request

```json
{
  "username": "john@example.com",
  "password": "StrongPass123"
}
```

### Login Response

```json
{
  "message": "Login successful.",
  "access": "<JWT access token>",
  "refresh": "<JWT refresh token>"
}
```

---

## 👤 Patient APIs

| Method | Endpoint              | Description                                  |
| ------ | --------------------- | -------------------------------------------- |
| POST   | `/api/patients/`      | Add a new patient                            |
| GET    | `/api/patients/`      | Get all patients (created by logged-in user) |
| GET    | `/api/patients/<id>/` | Get specific patient                         |
| PUT    | `/api/patients/<id>/` | Update patient                               |
| DELETE | `/api/patients/<id>/` | Delete patient                               |

### Patient Request Example

```json
{
  "name": "Jane Smith",
  "date_of_birth": "1990-05-15",
  "gender": "F",
  "email": "jane@example.com",
  "phone": "9876543210",
  "address": "Delhi, India",
  "medical_history": "Diabetes Type 2"
}
```

---

## 👨‍⚕️ Doctor APIs

| Method | Endpoint             | Description                  |
| ------ | -------------------- | ---------------------------- |
| POST   | `/api/doctors/`      | Add a new doctor             |
| GET    | `/api/doctors/`      | Get all doctors              |
| GET    | `/api/doctors/<id>/` | Get specific doctor          |
| PUT    | `/api/doctors/<id>/` | Update doctor (creator only) |
| DELETE | `/api/doctors/<id>/` | Delete doctor (creator only) |

### Doctor Request Example

```json
{
  "name": "Dr. Rajesh Kumar",
  "specialization": "Cardiology",
  "email": "dr.rajesh@hospital.com",
  "phone": "9876500001",
  "experience_years": 10,
  "qualification": "MBBS, MD",
  "available": true
}
```

---

## 🔗 Patient-Doctor Mapping APIs

| Method | Endpoint                      | Description                |
| ------ | ----------------------------- | -------------------------- |
| POST   | `/api/mappings/`              | Assign doctor to patient   |
| GET    | `/api/mappings/`              | Get all mappings           |
| GET    | `/api/mappings/<patient_id>/` | Get doctors for a patient  |
| DELETE | `/api/mappings/<id>/`         | Remove doctor from patient |

### Mapping Request Example

```json
{
  "patient": 1,
  "doctor": 2,
  "notes": "Primary care physician"
}
```

---

## ⚠️ Error Handling

| Code | Meaning                        |
| ---- | ------------------------------ |
| 200  | Success                        |
| 201  | Created                        |
| 400  | Bad Request / Validation Error |
| 401  | Unauthorized                   |
| 403  | Forbidden                      |
| 404  | Not Found                      |

---

## 📌 Key Notes

* Patients are **scoped to the authenticated user**
* Doctors are **visible to all users**, but editable only by creator
* Duplicate mappings are **prevented**
* JWT access tokens expire in **1 hour**
* Refresh tokens valid for **7 days**

---

## 📸 API Screenshots

*Add screenshots here (recommended for better evaluation):*

* Login success
* Patient CRUD
* Doctor CRUD
* Mapping APIs

---

## 👨‍💻 Author

**Vaibhav Pant**

---

## ⭐ Final Note

This project demonstrates a production-ready backend structure with authentication, secure APIs, and clean architecture suitable for real-world healthcare applications.
