# FastAPI Backend Example

A minimal HTTP API created using `FastAPI` and `Uvicorn` for a school project.

## 🛠 Prerequisites

Make sure you have **Python 3.10+** installed. You can check this by running:
```powershell
python --version
```
*(If Python is not found, download it from [python.org](https://www.python.org/downloads/) and check ✅ **"Add Python to PATH"** during installation.)*

---

## 🚀 Setup Instructions

Follow these steps to set up the project locally:

### 1. Create a Virtual Environment (`venv`)
Run the following command in your terminal inside the project directory:
```powershell
python -m venv venv
```

### 2. Activate the Virtual Environment
- **On PowerShell**:
  ```powershell
  .\venv\Scripts\activate
  ```
  *(If you get a script execution policy error, run `Set-ExecutionPolicy Unrestricted -Scope Process` first)*

- **On Command Prompt (CMD)**:
  ```cmd
  venv\Scripts\activate
  ```

Once activated, you will see `(venv)` at the beginning of your command prompt lines.

### 3. Install Required Packages
With your environment activated, run:
```powershell
pip install -r requirements.txt
```

---

## ▶️ Running the Backend

Start the local development server using `uvicorn`:
```powershell
uvicorn main:app --reload
```

The API will now be accessible at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🔍 API Endpoints & Testing

You can use `curl` to test the API endpoints from your terminal:

### 1. Root Endpoint (`GET /`)
Returns a friendly greeting.
```powershell
curl http://127.0.0.1:8000/
```
**Expected Response:**
```json
{
  "message": "hello, world",
  "info": "Welcome to the modular FastAPI template!"
}
```

### 2. Healthcheck Endpoint (`GET /api/v1/healthcheck`)
Returns a successful health status.
```powershell
curl http://127.0.0.1:8000/api/v1/healthcheck
```
**Expected Response:**
```json
{
  "status": "ok",
  "message": "successful health status"
}
```