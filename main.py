import praw
import google.generativeai as genai
import re

REDDIT_CLIENT_ID = 'YOUR_CLIENT_ID'
REDDIT_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDDIT_USER_AGENT = 'user persona script by /u/YOUR_USERNAME'
GEMINI_API_KEY = 'YOUR API KEY'
POST_LIMIT = 30
COMMENT_LIMIT = 30

# Initialize Reddit and Gemini
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

def extract_username(profile_url_or_name):
    if profile_url_or_name.startswith("http"):
        match = re.search(r'reddit\.com/user/([^/]+)/?', profile_url_or_name)
        if match:
            return match.group(1)
        else:
            raise ValueError("Invalid Reddit profile URL.")
    return profile_url_or_name

def get_user_content(username, post_limit=POST_LIMIT, comment_limit=COMMENT_LIMIT):
    user = reddit.redditor(username)
    posts = []
    comments = []
    try:
        for submission in user.submissions.new(limit=post_limit):
            posts.append({
                'title': submission.title,
                'selftext': submission.selftext,
                'url': submission.url,
                'permalink': f"https://www.reddit.com{submission.permalink}"
            })
    except Exception as e:
        print(f"Error fetching posts: {e}")
    try:
        for comment in user.comments.new(limit=comment_limit):
            comments.append({
                'body': comment.body,
                'permalink': f"https://www.reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error fetching comments: {e}")
    return posts, comments

def build_persona(posts, comments):
    all_text = ""
    for post in posts:
        all_text += f"Post: {post['title']} {post['selftext']} (Link: {post['permalink']})\n"
    for comment in comments:
        all_text += f"Comment: {comment['body']} (Link: {comment['permalink']})\n"
    
    prompt = f"""
Analyze the following Reddit user's posts and comments and create a detailed user persona.
For each characteristic (age, location, interests, etc.), cite the specific post or comment (with permalink) that supports your inference.

User Content:
{all_text}
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Gemini API error:", e)
        return "Error: Could not generate persona."


profile_url_or_name = input("Enter Reddit profile URL or username: ").strip()
username = extract_username(profile_url_or_name)
print(f"Fetching data for user: {username} ...")
posts, comments = get_user_content(username)
if not posts and not comments:
    print("No posts or comments found for this user.")

print(f"Fetched {len(posts)} posts and {len(comments)} comments. Building persona...")
persona = build_persona(posts, comments)
filename = f"{username}_persona.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(persona)
print(f"User persona saved to {filename}")