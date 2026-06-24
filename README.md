# Internal Status App DevOps

Python Flask internal status application built for DevOps learning.

## Routes

- `/` - Main status page
- `/health` - Health check endpoint

## Tech Stack

- Python
- Flask
- Git
- GitHub

## How to Run Locally

Activate virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the app:

```powershell
python app\main.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

## Project Goal

Deploy this Flask app on AWS EC2 inside a custom VPC and improve it step by step using real DevOps practices.