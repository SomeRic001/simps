# Smart Investment Management & Portfolio System (SIMPS)

![Django](https://img.shields.io/badge/Backend-Django-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?style=for-the-badge&logo=mysql)
![TailwindCSS](https://img.shields.io/badge/UI-TailwindCSS-38B2AC?style=for-the-badge&logo=tailwind-css)
![JavaScript](https://img.shields.io/badge/Frontend-JavaScript-F7DF1E?style=for-the-badge&logo=javascript)
![License](https://img.shields.io/badge/License-Academic-blue?style=for-the-badge)

---

## 📌 Overview

**Smart Investment Management & Portfolio System (SIMPS)** is a full-stack web application designed to integrate structured financial management with investment portfolio tracking.

The system enables users to:

- Securely register and authenticate
- Record monthly income and expenses
- Automatically calculate savings
- Explore global investment instruments
- Build and manage a personal portfolio

SIMPS emphasizes strong relational database design, SQL-based modeling, and real-world DBMS implementation.

---

## 🎯 Project Objective

- Develop a centralized financial tracking platform and make investment easy 

---

## 🏗️ System Architecture

```bash
Frontend (HTML, CSS, JS, Tailwind)
↓
Django Backend (Business Logic & APIs)
↓
PosgreSQL (Relational Database)

```
---

## 🚀 Core Features

### 🔐 Authentication & User Management
- Secure sign-up and login
- Password hashing
- User session management

### 📊 User Dashboard
- Income & expense tracking
- Automatic savings calculation
- Financial summary overview

### 🌍 Investment Exploration
- Browse global equities (stocks)
- Card-based investment interface

### 📈 Personal Portfolio
- Add selected investments
- Track allocated amounts
- Manage portfolio entries

### 📱 Responsive Design
- Tailwind CSS-based UI
- Desktop and mobile support

---

## 🗂 Database Design

### Main Tables

- `users`
- `income`
- `expenses`
- `savings`
- `global_equities`
- `personal_portfolio`

### Relationships

- Users → Income (1:N)
- Users → Expenses (1:N)
- Users → Savings (1:N)
- Users ↔ Global Equities (M:N via Personal Portfolio)

---

## 🛠 Tech Stack

### Backend
- Python
- Django
- PosgreSQL

### Frontend
- HTML
- CSS
- JavaScript
- Tailwind CSS

### Development Tools
- Git & GitHub
- VS Code
- Thunder Client
- LaTeX (Documentation)

---

## 📁 Project Structure
```bash

TO BE FILLED LATER
```


---

# ⚙️ Local Setup Guide

## 1️⃣ Clone Repository

```bash
git clone <xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>
cd simps
```

## 2️⃣ Backend Setup
```bash
cd backend/simps_project
python -m venv simps_venv
source simps_venv/bin/activate   # macOS/Linux
```
### OR
```bash
simps_venv\Scripts\activate      # Windows
```

Install dependencies:
```bash
pip install -r ../../requirements.txt
```

## 3️⃣ Configure Database (PosgreSQL)

Open:
```bash
backend/simps_project/simps_project/settings.py
```
Update the DATABASES configuration:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'simps_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Ensure MySQL server is running.

## 4️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 5️⃣ Populate Database
Run script:
```bash
python scripts/price_updater.py
```
## 6️⃣ Run Server
```bash
npm install
npm run dev
```
---

## 🧪 Running the Full System
1. Start PosgreSQL
2. Run Frontend server (which automatically runs the backend server)
3. Open browser and access the application
---

## 👨‍💻 Contributors
- Prayush Bikram Khadka
- Rhiki Ranjan Neupane
- Shaswat Sharma
  
---

## 🔮 Future Improvements
- Portfolio performance analytics
- Risk profiling engine
- Cloud deployment (AWS / GCP / Azure)

---
## 📄 License
Developed for academic purposes at IOE Thapathali Campus.

### ⭐ If you found this project interesting, consider giving it a star!

---
