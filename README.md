# 🏥 Healthcare Backend API

A scalable and production-ready backend system for managing healthcare records — including patients, doctors, and their mappings — built using **Django**, **Django REST Framework**, and **PostgreSQL** with secure **JWT authentication**.

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
* **djangorestframework-simplejwt**
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

## 🌐 Base URL

```
http://127.0.0.1:8001/
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/VAIBHAVPANT07/healthcare-backend-api.git
cd healthcare-backend-api
```

---

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=vaibhav
DB_PASSWORD=root
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Setup PostgreSQL Database

```bash
psql -U postgres
```

```sql
CREATE DATABASE healthcare_db;
\c healthcare_db
```

---

### 6. Run migrations

```bash
python manage.py migrate
```

---

### 7. Run server

```bash
python manage.py runserver 8001
```

👉 API will be available at:

```
http://127.0.0.1:8001/
```

---

## 🔐 Authentication

### ⚠️ Important Notes

* Register & Login APIs → ❌ No authentication required
* All other APIs → ✅ Require JWT token

---

### 🔑 Authentication Header

```
Authorization: Bearer <access_token>
```

---

## 🔄 API Usage Flow (Step-by-Step)

1. Register a user
2. Login to get JWT token
3. Copy the `access` token
4. Add it to Authorization header
5. Use it for all protected APIs

---

## 🔑 Authentication APIs

| Method | Endpoint              | Description        |
| ------ | --------------------- | ------------------ |
| POST   | `/api/auth/register/` | Register a user    |
| POST   | `/api/auth/login/`    | Login & get tokens |

---

### Register Request

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "StrongPass123",
  "password2": "StrongPass123"
}
```

---

### Login Request

```json
{
  "username": "john@example.com",
  "password": "StrongPass123"
}
```

---

### Login Response

```json
{
  "access": "<JWT access token>",
  "refresh": "<JWT refresh token>"
}
```

---

## 👤 Patient APIs

| Method | Endpoint              | Description       |
| ------ | --------------------- | ----------------- |
| POST   | `/api/patients/`      | Create patient    |
| GET    | `/api/patients/`      | Get all patients  |
| GET    | `/api/patients/<id>/` | Get patient by ID |
| PUT    | `/api/patients/<id>/` | Update patient    |
| DELETE | `/api/patients/<id>/` | Delete patient    |

---

### Example Request (POST)

```json
{
  "name": "Jane Smith",
  "date_of_birth": "1990-05-15",
  "gender": "F"
}
```

---

## 👨‍⚕️ Doctor APIs

| Method | Endpoint             | Description      |
| ------ | -------------------- | ---------------- |
| POST   | `/api/doctors/`      | Create doctor    |
| GET    | `/api/doctors/`      | Get all doctors  |
| GET    | `/api/doctors/<id>/` | Get doctor by ID |
| PUT    | `/api/doctors/<id>/` | Update doctor    |
| DELETE | `/api/doctors/<id>/` | Delete doctor    |

---

## 🔗 Mapping APIs

| Method | Endpoint                      | Description              |
| ------ | ----------------------------- | ------------------------ |
| POST   | `/api/mappings/`              | Assign doctor to patient |
| GET    | `/api/mappings/`              | Get all mappings         |
| GET    | `/api/mappings/<patient_id>/` | Get doctors for patient  |
| DELETE | `/api/mappings/<id>/`         | Remove mapping           |

---

## 🧪 Testing with Postman

* Use POST for Register & Login
* Use Bearer Token for protected APIs
* Do NOT send body in GET requests
* Add token in Authorization tab

---

## ⚠️ Common Errors

| Error            | Reason                     |
| ---------------- | -------------------------- |
| 401 Unauthorized | Missing or invalid token   |
| Database error   | Wrong `.env` configuration |
| 403 Forbidden    | Permission issue           |

---

## 📸 API Screenshots

*(Add screenshots here for better evaluation)*

* Register success
* Login response
* Patient creation
* Patient list

---

## 👨‍💻 Author

**Vaibhav Pant**

---

## ⭐ Final Note

This project demonstrates a **production-level backend system** with authentication, secure APIs, and scalable architecture — suitable for real-world healthcare applications.
