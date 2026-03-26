# Deployment Guide: Bot-to-Bot Healthcare Communication System

To share your project with the world (so your friends or professors can test it on their phones), you need to "deploy" it to a cloud server. For beginners, **Render.com** is the easiest free platform for hosting Python web applications.

Here is the step-by-step guide to deploying this project completely for free:

---

## 🛠️ Step 1: Prepare the Project for Production

Right now, the app runs on a "development server" which is not allowed on live websites. We need to tell the live server to use a production web server like `gunicorn` with `eventlet`.

1. Open your `requirements.txt` file and make sure these two lines are at the very bottom:
   ```text
   gunicorn==21.2.0
   eventlet==0.33.3
   ```

2. Create a new file in your project folder named exactly `Procfile` (no `.txt` extension!). 
3. Paste the following exact line inside the `Procfile`:
   ```text
   web: gunicorn --worker-class eventlet -w 1 app:app
   ```

---

## 🐙 Step 2: Upload to GitHub

Render.com pulls your code directly from GitHub, so you need to upload it there first.

1. Go to [GitHub.com](https://github.com/) and create a free account (if you don't have one).
2. Click the **+** icon in the top right and select **New repository**.
3. Name it `healthcare-chatbot` (or anything you like) and click **Create repository**.
4. Upload all your project files (`app.py`, `database.py`, `requirements.txt`, `Procfile`, and the `templates` and `static` folders) to this repository.
   *(Note: Do not upload the `__pycache__` or `.venv` folders).*

---

## ☁️ Step 3: Deploy on Render.com

1. Go to [Render.com](https://render.com/) and sign up using your GitHub account.
2. Click the **New** button and select **Web Service**.
3. Click **Build and deploy from a Git repository**.
4. Connect your GitHub account and select the `healthcare-chatbot` repository you just made.
5. Fill out the settings as follows:
   - **Name**: healthcare-bot-app
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt` (Render usually fills this in automatically)
   - **Start Command**: `gunicorn --worker-class eventlet -w 1 app:app`
   - **Instance Type**: Free
6. Scroll down and click **Create Web Service**.

## 🎉 Step 4: Wait and Test!
Render will now build your project. You will see a terminal window with logs updating. This process takes about 2-5 minutes. 

Once you see the text `Your service is live 🎉`, click the URL given at the top left of the screen (e.g., `https://healthcare-bot-app.onrender.com`). 

You can now share this URL! 
- Go to `[Your-URL]/` to view the Patient Chatbot.
- Go to `[Your-URL]/hospital` to view the Hospital Dashboard.
