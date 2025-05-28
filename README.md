# 🧑‍💼 Job Portal API

A robust backend for a modern job portal application, built with Django and Django REST Framework. This API streamlines recruitment workflows by connecting recruiters and applicants through secure, efficient, and user-friendly endpoints.

---

## 🚀 Features

### For Applicants
- **Apply to Jobs:** Easily submit applications with resumes, cover letters, and portfolio links.
- **Track Applications:** Monitor the status of all your job applications in real time.
- **Receive Notifications:** Get instant updates about your application progress and recruiter feedback.

### For Recruiters
- **Post Jobs:** Create, publish, and manage job postings effortlessly.
- **Manage Applications:** Review applicants, update application statuses, and communicate with candidates.
- **Notifications:** Receive alerts when new applications are submitted to your job postings.

### Additional Features
- **Role-Based Access Control:** Enforces secure, role-specific access for applicants and recruiters.
- **Automated Notifications:** Utilizes Django signals to trigger timely notifications on relevant user actions.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default); easily configurable to PostgreSQL for production environments
- **Authentication:** Token-based authentication using Django REST Framework
- **Deployment:** Pre-configured for platforms like Heroku, Render, or Railway

---

## 📂 Project Structure

```
Job_portal/
├── job_portal/           # Project settings and configurations
├── jobs/                 # App handling job postings and applications
├── users/                # Custom user model and authentication
├── db.sqlite3            # SQLite database (development)
├── manage.py             # Django's command-line utility
```

---

## 📦 Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Ravi8043/Job_portal.git
    cd Job_portal
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

---

## 🔑 API Endpoints Overview

### Applicants

- `GET /applicant/dashboard/`  
  View your job applications.

- `POST /jobs/apply/`  
  Apply to a job posting.

### Recruiters

- `POST /jobs/create/`  
  Create a new job posting.

- `GET /recruiter/notifications/`  
  View notifications for recruiters.

- `PATCH /recruiter/jobapplication/<id>/status/`  
  Update the status of a job application.  
  _Note: Replace `<id>` with the actual application ID._

---

## 🧪 Testing the API

Use tools like [Postman](https://www.postman.com/) or `cURL` to interact with the API endpoints.  
**Authentication tokens** must be included in your requests for authorized access.

---

## 🚀 Deployment

1. **Choose a Platform:**  
   [Heroku](https://heroku.com), [Render](https://render.com), or [Railway](https://railway.app) are recommended.

2. **Configure Environment Variables:**
   - `SECRET_KEY`: Your Django secret key.
   - `DEBUG`: Set to `False` for production.
   - `ALLOWED_HOSTS`: Domains/IPs your app will serve.
   - Database settings: Switch from SQLite to PostgreSQL for production readiness.

3. **Collect Static Files:**
    ```bash
    python manage.py collectstatic
    ```

4. **Deploy:**  
   Follow the deployment instructions provided by your chosen platform.

---

## 🤝 Contributing

Contributions are welcome!  
If you'd like to propose enhancements or report bugs, please fork the repository and submit a pull request.  
For significant changes, open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ✉️ Contact

For questions or support, please open an issue or contact [Ravi8043](https://github.com/Ravi8043).
