# Deployment Guide - FastAPI on Render

## Step 1: Push to GitHub

### 1a. Initialize Git (if not done)
```bash
cd c:\Users\devda\Documents\devdath APIs
git init
git add .
git commit -m "Initial commit: FastAPI project"
```

### 1b. Create a new GitHub repository
- Go to https://github.com/new
- Name it: `devdath-apis` (or your preferred name)
- Click "Create repository"

### 1c. Link and push your code
```bash
git remote add origin https://github.com/YOUR_USERNAME/devdath-apis.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy to Render

### 2a. Sign up on Render
- Go to https://render.com
- Sign up with GitHub (recommended)

### 2b. Create a Web Service
- Click "New +" → "Web Service"
- Connect GitHub and select your `devdath-apis` repo
- Choose the `main` branch

### 2c. Configure the Service
- **Name:** devdath-api (or your choice)
- **Environment:** Python 3
- **Build Command:**
  ```
  pip install -r requirements.txt
  ```
- **Start Command:**
  ```
  uvicorn app.main:app --host 0.0.0.0 --port 10000
  ```

### 2d. Add Environment Variables
Click "Advanced" and add these environment variables:
```
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./app.db
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=your-email@gmail.com
```

### 2e. Deploy
- Click "Create Web Service"
- Wait for build to complete (2-3 minutes)
- Your API URL will be: `https://devdath-api.onrender.com`

### 2f. Test Your API
Open: `https://devdath-api.onrender.com/docs`

---

## Quick Reference

**Your API will be live at:**
```
https://devdath-api.onrender.com
```

**Test endpoints:**
- Swagger UI: `https://devdath-api.onrender.com/docs`
- Register: `POST /register`
- Login: `POST /token`
- Get joke: `GET /external/joke`

---

Done! Your API is now live and ready to use! 🚀
