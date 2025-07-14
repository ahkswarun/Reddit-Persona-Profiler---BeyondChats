# Reddit User Persona Generator 
AI-powered tool that generates detailed user personas from any public Reddit profile. It analyzes recent posts and comments with Google Gemini AI to extract interests, personality, and behavior, citing Reddit activity for transparency and verifiability.

## **Setup Instructions**

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator
```

### 2. **Install Required Packages**

Make sure you have Python 3.8+ installed.

```bash
pip install praw google-generativeai
```

### 3. **Get Your API Keys**

#### **Reddit API Keys**
- Go to [Reddit Apps](https://www.reddit.com/prefs/apps).
- Click **"create another app"** at the bottom.
- Fill in the name, select **script**, and set redirect URI to `http://localhost:8080`.
- Copy your **client_id** and **client_secret**.

#### **Google Gemini API Key**
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
- Create and copy your Gemini API key.

### 4. **Configure Your Keys**

Open the main Python script (e.g., `main.py`) and replace the placeholders at the top with your actual keys:

```python
REDDIT_CLIENT_ID = 'YOUR_CLIENT_ID'
REDDIT_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDDIT_USER_AGENT = 'user persona script by /u/YOUR_USERNAME'
GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY'
```

---

## **How to Execute**

1. **Run the script:**

   ```bash
   python main.py
   ```

2. **When prompted, enter a Reddit username or profile URL:**

   ```
   Enter Reddit profile URL or username: https://www.reddit.com/user/kojied/
   ```

3. **Wait for the script to fetch data and generate the persona.**

4. **The output will be saved as `<username>_persona.txt` in the current directory.**

---

## **Example Output**

```
User persona saved to kojied_persona.txt
```

Open the `.txt` file to view the generated persona, including citations to the user's Reddit activity.

---

## **Troubleshooting**

- **API Errors:**  
  - Make sure your API keys are correct and active.
  - If you hit rate limits or quota errors, wait and try again or upgrade your plan.

- **No Output File:**  
  - Ensure the user has public posts/comments.
  - Check for typos in the username or URL.

---

## **License**

MIT License
