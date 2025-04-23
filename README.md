# 📜 Flask Todo App

A full-featured Flask-based Todo application with:

- ✅ User registration & login
- 🌒 Light/Dark mode toggle
- ✍️ Task creation, completion, editing & deletion
- 🗕️ Calendar view (FullCalendar)
- 📧 Email reminders for due tasks
- 📄 Export to CSV
- 🔐 Secure config via `.env`

---

## 🚀 Features

| Feature             | Description                                      |
|---------------------|--------------------------------------------------|
| 👤 Authentication   | Register/login system using `werkzeug.security` |
| 🌗 Dark Mode Toggle | Session-based light/dark theme switching        |
| 📬 Email Reminders  | SMTP-based alerts for tasks due today           |
| 📄 Export Tasks     | CSV download of your todo list                  |
| ✨ Task Manager      | Add, complete, delete, edit tasks               |
| 🗕️ Calendar View    | View tasks visually by due date                 |

---

## 🧱 Tech Stack

- Python 3.10+
- Flask
- Bootstrap 5
- Jinja2 templating
- FullCalendar.js (calendar view)
- `python-dotenv` for config
- SMTP (for email reminders)

---

## 🔐 Environment Variables

Create a `.env` file in your project root with:

```env
FLASK_SECRET_KEY=your_secret
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_password
EMAIL_SMTP=smtp.example.com
EMAIL_PORT=587
```

✅ Be sure to add `.env` to your `.gitignore`

---

## 🚀 Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/todo-flask-app.git
cd todo-flask-app
pip install -r requirements.txt
flask run
```

---

## 📧 Sending Email Reminders

You can manually visit `/remind` or schedule a cron job:

```bash
curl https://your-deployed-app.com/remind
```

---

## 📦 Deploying

- Recommended: [Render](https://render.com)
- Set up environment variables from `.env`
- Use `gunicorn` as your start command:

```bash
web: gunicorn main:app
```

---

## 📄 License

MIT © [Your Name]
