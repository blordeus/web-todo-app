from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import json, os, csv
from datetime import datetime, date
import smtplib
from email.mime.text import MIMEText

load_dotenv()

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'supersecretkey')

USERS_FILE = 'users.json'
TASKS_FILE = 'tasks.json'

# --- User Utilities ---
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# --- Task Utilities ---
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# --- Email Reminder Logic ---
def send_email_reminder(to_email, subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = os.getenv('EMAIL_USER')
        msg['To'] = to_email

        with smtplib.SMTP(os.getenv('EMAIL_SMTP'), int(os.getenv('EMAIL_PORT'))) as server:
            server.starttls()
            server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/remind')
def remind():
    tasks = load_tasks()
    for user, user_tasks in tasks.items():
        due_today = [t for t in user_tasks if t.get('due_date') == date.today().isoformat() and not t['completed']]
        if due_today:
            task_list = '\n'.join([f"- {t['task']} ({t['priority']})" for t in due_today])
            message = f"You have the following tasks due today:\n\n{task_list}"
            send_email_reminder(f"{user}@example.com", "Tasks Due Today", message)
    flash("📧 Email reminders sent for today's due tasks.", "success")
    return redirect(url_for('index'))

@app.route('/toggle-theme')
def toggle_theme():
    current = session.get('theme', 'light')
    session['theme'] = 'dark' if current == 'light' else 'light'
    return redirect(request.referrer or url_for('index'))
