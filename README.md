# 🛒 E-Commerce App — Backend API

A Python-based e-commerce backend API designed to provide the foundation for an online shopping platform. The project focuses on backend development, API design, database management, and organizing application logic into reusable modules.

## 📌 About the Project

The E-Commerce App is a backend development project built with Python. It is designed to handle the core operations of an online shopping application through a structured API.

The project follows a modular structure that separates authentication, database operations, models, schemas, routes, and business logic, making the codebase easier to maintain, test, and extend.

This project is part of my journey as a Backend Developer, where I continue to strengthen my skills in building practical applications and designing reliable APIs.

## 🛠️ Technologies Used

- **Python** — Core programming language.
- **FastAPI** — Building API endpoints.
- **PostgreSQL** — Relational database management.
- **Pydantic** — Data validation and schema management.
- **Psycopg2** — PostgreSQL database connectivity.
- **Git & GitHub** — Version control and source code management.

## ✨ Key Components

- **Authentication:** A dedicated module for authentication-related functionality.
- **Database Management:** Database configuration and connectivity.
- **Models:** Organizing application data structures.
- **Schemas:** Validating and structuring API request and response data.
- **Routes:** Defining API endpoints.
- **Services:** Separating business logic from route handlers.
- **Testing:** A dedicated test file for checking application functionality.

## 📂 Project Structure

```text
e_commerce/
│
├── e_commerce/
├── venv/
├── auth.py
├── config.py
├── database.py
├── main.py
├── models.py
├── routes.py
├── schema.py
├── services.py
├── test.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Navigate into the project directory:

```bash
cd e_commerce
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file if required by the project and configure the necessary environment variables, such as your database connection settings and application secrets.

Keep sensitive credentials out of your source code and never commit your `.env` file to GitHub.

### 6. Set Up PostgreSQL

Ensure PostgreSQL is installed or that you have access to a PostgreSQL database. Configure the database connection according to your project's settings.

### 7. Run the Application

If `main.py` exposes a FastAPI application instance named `app`, run:

```bash
uvicorn main:app --reload
```

The API will typically be available at:

- **API Base URL:** http://127.0.0.1:8000
- **Interactive API Documentation:** http://127.0.0.1:8000/docs

## 🧪 Testing

Run your project's tests using the testing framework configured for the repository.

For example, if the tests use `pytest`:

```bash
python -m pytest
```

## 🎯 Project Goals

- Strengthen my backend development skills using Python.
- Build and organize RESTful API endpoints.
- Understand database integration and data validation.
- Practice modular application architecture.
- Improve code quality, testing, and maintainability.
- Develop a strong foundation for building full-featured e-commerce applications.

## 🚧 Project Status

**In Development**

The project is being developed and improved as I continue learning and implementing backend development concepts.

## 👨‍💻 Author

**Backend Developer**

Passionate about building useful applications, designing APIs, working with databases, and continuously improving my software development skills.

## 📄 License

A license has not yet been specified for this project.
