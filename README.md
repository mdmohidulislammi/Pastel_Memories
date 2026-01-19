# 🌸 Pastel Memories

**Pastel Memories** is a simple, secure, and personal recollection web application where users can save, view, and manage their memories privately. Each memory is accessible only after login, ensuring privacy and a calm, distraction‑free experience.

## 🚀 Features

* 🔐 User authentication (Register / Login / Logout)
* 🧠 Create, read, update, and delete personal memories
* 🕒 Memories stored with date & time
* 🎨 Modern pastel UI with Tailwind CSS
* 👤 User dashboard (manage profile only)
* 🔒 Each user can see **only their own memories**
* 🌐 Ready for deployment (Render / Railway)

---

## 🛠 Tech Stack

* **Backend:** Django
* **Frontend:** HTML, Tailwind CSS
* **Database:** PostgreSQL / SQLite
* **Authentication:** Django Auth (+ Google OAuth optional)

---

## 📸 Memory Structure

Each memory contains:

* Title
* Body (text only)
* Date & Time

---

## 🧩 Installation (Local)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🌍 Deployment

Pastel Memories can be deployed for free using:

* Render
* Railway

(Production settings supported)

---

## 🔐 Privacy First

All memories are private by default. Users cannot access or view other users’ content.

---

## 📚 Use Case

* Personal journaling
* Daily thoughts & reflections
* Academic / portfolio Django project

---

## 👨‍💻 Author

Developed as a personal Django project for learning and academic purposes.

---

✨ *Capture moments softly. Remember them forever.*
