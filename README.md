# Todo List with FastAPI

This repository is a learning and testing project aimed at gaining a deeper understanding of **FastAPI** by building a simple Todo List application.

The project focuses on FastAPI fundamentals, best practices, and common backend patterns such as request validation, routing, dependency injection, and async APIs.

---

## 🚀 Features

* FastAPI-based RESTful API
* Todo CRUD operations (Create, Read, Update, Delete)
* Request & response validation with Pydantic
* Clean and simple project structure
* Designed for learning and experimentation

---

## 🛠 Requirements

* Python 3.9+
* pip

All required dependencies are listed in `requirements.txt`.

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Todo-list-with-fastapi.git
cd Todo-list-with-fastapi
```

2. (Optional but recommended) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> This command installs **all required packages** defined in `requirements.txt`.

---

## ▶️ Running the Project

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

* **API:** `http://127.0.0.1:8000`
* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## 📂 Project Structure (Example)

```
.
├── main.py
├── requirements.txt
├── routers/
├── models/
├── schemas/
└── README.md
```

---

## 🧪 Purpose of This Project

* Learn FastAPI deeply
* Practice async backend development
* Experiment with API design and architecture
* Prepare a foundation for larger FastAPI projects

---

## 🧩 Future Improvements

* Database integration (PostgreSQL / SQLite)
* Authentication & authorization
* Unit and integration tests
* Docker support
* Pagination and filtering

---

## 📜 License

This project is for educational purposes.
Feel free to fork, modify, and experiment.

---

If you want, I can also:

* Make it **more minimal**
* Make it **enterprise-style**
* Add **Docker**, **Alembic**, or **PostgreSQL** sections
* Rewrite it for **resume / portfolio quality**

Just tell me 👌
