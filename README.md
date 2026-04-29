# 📝 Blog-Post-FastAPI

A modern, lightweight blog application built with **FastAPI** and **Jinja2** templates. Display blog posts with an elegant web interface and access posts via a REST API.

![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-blue?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

- 🚀 **Fast & Modern**: Built with FastAPI for high performance
- 📄 **Dynamic Blog Posts**: Display blog posts with metadata (author, date, content)
- 🌐 **REST API**: Access blog posts programmatically via `/api/posts`
- 🎨 **Responsive Design**: Clean and elegant UI with Jinja2 templates
- 📱 **Static Assets**: Custom CSS styling for a professional look
- ⚡ **Easy to Use**: Simple and straightforward codebase

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Templating**: Jinja2
- **Frontend**: HTML & CSS
- **Language**: Python 3.8+

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/HaRsh-init/Blog-Post-FastApi.git
cd Blog-Post-FastApi
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install fastapi uvicorn python-multipart
```

---

## 🚀 Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

Then open your browser and navigate to:
- **Web Interface**: http://localhost:8000/
- **API Endpoint**: http://localhost:8000/api/posts

### Using Uvicorn Options
```bash
# Run on a specific port
uvicorn main:app --reload --port 8080

# Run on all interfaces
uvicorn main:app --reload --host 0.0.0.0
```

---

## 📚 API Endpoints

### Home Page
```
GET /
GET /posts
```
Returns the rendered HTML blog home page with all posts.

### Get All Posts (JSON)
```
GET /api/posts
```
Returns all blog posts in JSON format.

**Response:**
```json
[
  {
    "id": 1,
    "author": "Corey Schafer",
    "title": "FastAPI is Awesome",
    "content": "This framework is really easy to use and super fast.",
    "date_posted": "April 20, 2025"
  },
  {
    "id": 2,
    "author": "Jane Doe",
    "title": "Python is Great for Web Development",
    "content": "Python is a great language for web development, and FastAPI makes it even better.",
    "date_posted": "April 21, 2025"
  }
]
```

---

## 📂 Project Structure

```
Blog-Post-FastApi/
├── main.py              # Main FastAPI application
├── templates/           # HTML templates
│   ├── home.html       # Blog home page template
│   └── layout.html     # Base layout template
├── static/             # Static files
│   └── css/
│       └── main.css    # Main stylesheet
├── .gitignore          # Git ignore file
└── README.md           # This file
```

---

## 🎯 Usage Examples

### View All Posts
Open your browser and visit: `http://localhost:8000/`

### Get Posts via API (using curl)
```bash
curl http://localhost:8000/api/posts
```

### Get Posts via API (using Python)
```python
import requests

response = requests.get("http://localhost:8000/api/posts")
posts = response.json()
for post in posts:
    print(f"{post['title']} by {post['author']}")
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**HaRsh-init**  
GitHub: [@HaRsh-init](https://github.com/HaRsh-init)

---

## 🙏 Acknowledgments

- FastAPI documentation and community
- Inspired by modern web development practices
- Built with ❤️ for the Python community

---

## 📞 Support

If you have any questions or need help, feel free to open an issue on GitHub or reach out!

---

**⭐ If you find this project useful, please consider giving it a star!**
