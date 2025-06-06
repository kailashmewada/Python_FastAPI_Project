
# 🚀 FastAPI Auth Service

A lightweight authentication API built using **FastAPI** and **MongoDB**, supporting:

- ✅ User Signup
- ✅ User Login
- ✅ Get User Details
- ✅ Forgot Password
- ✅ Reset Password
- ✅ JWT Token Authentication
- ✅ Auto-generated Swagger Docs

---

## 📁 Project Structure

```
FastAPI/
├── app/
│   ├── controllers/         # Business logic for routes
│   ├── core/                # Token & security utilities
│   ├── models/              # Request & response models
│   ├── routes/              # API route handlers
│   └── main.py              # Main FastAPI application
├── venv/                    # Virtual environment (optional)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Prerequisites

- Python 3.8+
- MongoDB (local or URI)
- Git (optional)

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/kailashmewada/Python_FastAPI_Project.gdait
cd fastapi-auth
```

### 2. Create & activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
# OR
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install fastapi uvicorn motor python-jose[cryptography] passlib[bcrypt] python-dotenv
```

Then freeze:

```bash
pip freeze > requirements.txt
```

---

## ▶️ Running the Server

```bash
uvicorn app.main:app --reload --port 5000
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📘 Swagger Docs

- Swagger UI → [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)
- Redoc UI → [http://127.0.0.1:5000/redoc](http://127.0.0.1:5000/redoc)

---

## 🔗 API Endpoints

| Method | Endpoint                        | Description                    |
|--------|----------------------------------|--------------------------------|
| POST   | `/api/v1/auth/signup`           | Register a new user           |
| POST   | `/api/v1/auth/login`            | User login                    |
| GET    | `/api/v1/auth/user/{username}`  | Get user details              |
| POST   | `/api/v1/auth/forget-password`  | Request password reset        |
| POST   | `/api/v1/auth/reset-password`   | Reset user password           |
| GET    | `/api/v1/auth/`                 | Health check endpoint         |

---

## 📥 Sample Payloads

### Signup

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "password": "securePass123"
}
```

### Login

```json
{
  "username": "john_doe",
  "password": "securePass123"
}
```

---

## 🧾 .env File Example

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb://localhost:27017
JWT_SECRET=your_jwt_secret
JWT_EXPIRY_MINUTES=30
```

---

## 🛠 Useful Commands

```bash
# Run server
uvicorn app.main:app --reload --port 5000

# Freeze installed packages
pip freeze > requirements.txt

# Deactivate virtual environment
deactivate
```

---

## 👨‍💻 Author

**Kailash Mewada**  
Backend Developer  
📧 kailashmewada485@gmail.com

---

## 📄 License

This project is licensed under the MIT License.
