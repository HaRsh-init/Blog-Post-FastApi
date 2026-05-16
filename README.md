# 📝 Blog-Post-FastAPI

A modern, lightweight blog application built with **FastAPI** and **Jinja2** templates. Display blog posts with an elegant web interface and access posts via a REST API.

![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-blue?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

- 🚀 **Fast & Modern**: Built with FastAPI for high performance
- 👤 **User Management:** Create users, associate posts, and assign profile images
- 📄 **Dynamic Blog Posts**: Display all posts, or filter by user
- 🔄 **REST API**: Create, fetch, and manage users and posts programmatically
- 🧑‍💻 **View Individual Posts:** Dedicated page for each post, and user-specific post lists
- 🖼️ **User Profile Images:** Custom or default profile pictures per user
- 🗂️ **Media & Static Assets:** `/media` and `/static` routes for serving images and static content
- 🛑 **Custom Error Pages:** Graceful error handling for both API & web responses
- 🎨 **Responsive Design:** Clean, elegant UI with Jinja2 templates
- 📱 **Simple & Expandable Codebase**

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, SQLAlchemy
- **Templating**: Jinja2
- **Frontend**: HTML & CSS
- **Language**: Python 3.8+

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Steps

1. **Clone the repository**
    ```bash
    git clone https://github.com/HaRsh-init/Blog-Post-FastApi.git
    cd Blog-Post-FastApi
    ```

2. **Create a virtual environment (recommended)**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install fastapi uvicorn python-multipart sqlalchemy
    ```

---

## 🚀 Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

Then open your browser and navigate to:
- **Web Interface**: http://localhost:8000/
- **API Endpoints**: http://localhost:8000/api/posts, http://localhost:8000/api/users

---

## 📚 API Endpoints (Key)

- `GET /` or `/posts`: Home page listing all posts
- `GET /posts/{post_id}`: View an individual post
- `GET /users/{user_id}`: View a user's profile and their posts

### Users
- `POST /api/users`: Create a user (`{"username": ..., "email": ...}`)
- `GET /api/users/{user_id}`: Get a specific user profile
- `GET /api/users/{user_id}/posts`: Get all posts by a user

### Blog Posts
- `GET /api/posts`: Get all posts (JSON)
- `POST /api/posts`: Create a post (`{"title": ..., "content": ..., "user_id": ...}`)
- `GET /api/posts/{post_id}`: Get a single post by ID

---

## 🗂️ Project Structure

```
Blog-Post-FastApi/
├── main.py              # Main FastAPI application
├── database.py          # Database models & session
├── models.py            # ORM models: User & Post
├── schemas.py           # Pydantic schemas
├── templates/
│   ├── home.html       # Home page template
│   ├── post.html       # Individual post
│   ├── user_posts.html # Posts by user
│   ├── error.html      # Error responses
│   └── layout.html     # Base layout template
├── static/             # Static files (css, images)
├── media/              # Media files and uploads
├── .gitignore
└── README.md
```

---

## 🤝 Contributing, License, Author, Acknowledgments, Support
(Sections remain as before)

---

**⭐ If you find this project useful, please consider giving it a star!**
