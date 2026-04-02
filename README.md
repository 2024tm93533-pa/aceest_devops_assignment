# 🏋️ ACEest Fitness & Gym – DevOps CI/CD Implementation

## 📌 Project Overview

This project implements a complete DevOps pipeline for **ACEest Fitness & Gym**, focusing on automating the software delivery lifecycle using modern tools and practices.

The system is designed to ensure:

* Code integrity
* Automated testing
* Consistent deployment environments
* Faster and reliable delivery

---

## 🎯 Objective

The primary objective of this assignment is to demonstrate hands-on implementation of:

* Version Control using Git
* Containerization using Docker
* Continuous Integration using GitHub Actions
* Continuous Deployment using Jenkins

---

## 🏗️ Project Structure

```
aceest-devops-assignment/
├── app/                    # Flask application (core backend)
├── aceest_desktop/         # Legacy desktop application (unchanged)
├── dockerfile              # Docker configuration files
├── .github/workflows/      # CI pipeline (GitHub Actions)
├── Jenkinsfile             # CD pipeline (Jenkins)
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md
```

---

## 🧱 System Architecture

```
Developer → Git → GitHub → CI (GitHub Actions) → Docker → CD (Jenkins) → Running App
```

### Explanation:

1. Developer writes code locally
2. Code is committed and pushed to GitHub
3. CI pipeline is triggered automatically
4. Docker image is built
5. Jenkins deploys the application
6. Application becomes available to users

---

## ⚙️ Application Details

### 🔹 Flask Application

* Acts as the main backend system
* Provides API endpoints for:

  * Member management
  * Health checks
* Organized using modular architecture:

  * Routes
  * Services
  * Models

### 🔹 Legacy Desktop Application

* Stored in `aceest_desktop/`
* Contains multiple versioned `.py` files
* **Not executed in CI/CD pipeline**
* Maintained for reference and traceability

---

## 🔄 CI/CD Pipeline

### 🚀 Continuous Integration (CI)

Implemented using GitHub Actions:

* Installs dependencies
* Runs unit tests
* Builds Docker image

### 🚀 Continuous Deployment (CD)

Implemented using Jenkins:

* Pulls latest code/image
* Runs Docker container
* Deploys application

---

## 🐳 Docker Implementation

Docker is used to:

* Package the application
* Ensure environment consistency
* Enable easy deployment

### Build Docker Image

```
docker build -t aceest-app .
```

### Run Container

```
docker run -p 8000:8000 aceest-app
```

---

## ▶️ Running the Project Locally

### Step 1: Clone Repository

```
git clone <your-repo-url>
cd aceest-devops-assignment
```

### Step 2: Setup Environment

```
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
pip install -r requirements.txt
```

### Step 3: Run Flask App

```
python run.py
```

Access:

```
http://127.0.0.1:8000
```

---

## 🧪 Running Tests

```
pytest
```

---

## 🔁 Version Control Strategy

* All code changes are tracked using Git
* Each feature is committed separately
* Clear commit messages are used

### Example Commits:

* `feat: added Flask routes`
* `feat: implemented services layer`
* `ci: added GitHub Actions workflow`
* `feat: dockerized application`

---

## 🔐 Key DevOps Benefits Achieved

* ✅ Automated build and testing
* ✅ Consistent environments via Docker
* ✅ Faster deployment using CI/CD
* ✅ Clear version tracking using Git

---

## 🧠 Key Learnings

* Understanding of complete DevOps lifecycle
* Hands-on experience with CI/CD pipelines
* Containerization and deployment automation
* Separation of application logic and infrastructure

---

## 📌 Conclusion

This project successfully demonstrates the implementation of a modern DevOps pipeline.
The integration of Git, GitHub Actions, Docker, and Jenkins ensures a scalable, reliable, and automated software delivery process.

---

## 👨‍💻 Author

Student Name: Parmeet Singh
BITSID: 2024TM93533
Course: DevOps Assignment
Organization: ACEest Fitness & Gym

---
