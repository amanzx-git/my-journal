# 📖 My Journal

Welcome to **My Journal**, a personal journaling web application built from scratch while learning the Django framework! This project serves as a private, secure digital space to document thoughts, track daily habits, and log memories.

## 🚀 Features (Under Development)
* **User Authentication:** Secure signup, login, and logout functionality to keep your journal private.
* **Daily Entries:** Full CRUD functionality (Create, Read, Update, Delete) for writing and managing journal posts.
* **Rich Text Editing:** Format your posts cleanly with structured text.
* **Categorization/Tags:** Organize journal entries by mood, tags, or topics (e.g., Ideas, Daily, Travel).
* **Responsive Design:** Clean, minimalist frontend that looks great on both desktop and mobile devices.

---

## 🛠️ Tech Stack
* **Backend Framework:** Django (Python)
* **Database:** SQLite3 (Default development database)
* **Frontend:** HTML5, CSS3, Django Templates

---

## 📦 Getting Started & Installation

Follow these steps to get a local copy of this Django project up and running on your machine:

### 1. Prerequisites
Make sure you have **Python 3.x** installed. You can check by running:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com
cd my-journal
```

### 3. Set Up a Virtual Environment (Recommended)
Create and activate a virtual environment to manage your dependencies cleanly:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Django
Install the framework inside your virtual environment:
```bash
pip install django
```

### 5. Run Database Migrations
Apply the initial Django migrations to configure your SQLite database:
```bash
python manage.py migrate
```

### 6. Start the Local Server
```bash
python manage.py runserver
```
Open your web browser and navigate to `http://127.0.0` to view the application!

---

## 📂 Project Structure
* `my_site/` - The core configuration directory of the Django project.
* `blogs/` - The main application handling the journal entries and logic.
* `templates/` - Global HTML template layouts.
* `static/` - CSS files, images, and Javascript assets.
* `manage.py` - Django's command-line utility for administrative tasks.

---

## 💡 About This Project
This application is being built as a hands-on learning tool to master core web development concepts, including Django's MVT (Model-View-Template) architecture, working with databases, handling user data, and routing. 

