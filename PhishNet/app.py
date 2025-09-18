from flask import Flask, render_template, request
import instaloader
import re
import requests

app = Flask(__name__)

# ---------------- URL CHECK ---------------- #
def check_url_safety(url: str) -> str:
    # Placeholder logic: You can replace with Google Safe Browsing API
    if "http" not in url:
        return "Invalid URL"
    if "phish" in url or "scam" in url:
        return "Suspicious"
    return "Safe"

# ---------------- INSTAGRAM CHECK ---------------- #
def check_instagram_account(username: str) -> dict:
    result = {"username": username, "status": "Safe", "reasons": []}
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        followers = profile.followers
        following = profile.followees
        posts = profile.mediacount
        bio = profile.biography

        if any(char.isdigit() for char in username) and len(username) > 12:
            result["status"] = "Fake Suspected"
            result["reasons"].append("Suspicious username pattern.")

        suspicious_words = ["http", "click", "win", "offer", "free", "money"]
        if any(word.lower() in bio.lower() for word in suspicious_words):
            result["status"] = "Fake Suspected"
            result["reasons"].append("Bio contains suspicious links/words.")

        if posts == 0:
            result["status"] = "Fake Suspected"
            result["reasons"].append("Profile has no posts.")

        if following > 5 * (followers + 1):
            result["status"] = "Fake Suspected"
            result["reasons"].append("Follows too many accounts compared to followers.")

        if followers > 1000 and posts < 3:
            result["status"] = "Fake Suspected"
            result["reasons"].append("High followers but very few posts.")

        if not result["reasons"]:
            result["status"] = "Likely Safe"
            result["reasons"].append("No major red flags detected.")

    except Exception as e:
        result["status"] = "Error"
        result["reasons"].append(f"Exception occurred: {e}")

    return result

# ---------------- APK CHECK ---------------- #
def check_apk_file(file) -> str:
    # Placeholder: just check extension
    if not file.filename.endswith(".apk"):
        return "Invalid file format"
    # In real project, integrate VirusTotal / static APK analyzer
    return "Safe (Basic Check)"

# ---------------- ROUTES ---------------- #
@app.route("/", methods=["GET", "POST"])
def index():
    url_status = None
    insta_report = None
    apk_status = None

    if request.method == "POST":
        if "url" in request.form:
            url = request.form.get("url")
            url_status = check_url_safety(url)

        if "instagram" in request.form:
            username = request.form.get("instagram")
            if username:
                insta_report = check_instagram_account(username)

        if "apk" in request.files:
            file = request.files["apk"]
            if file:
                apk_status = check_apk_file(file)

    return render_template("index.html",
                           url_status=url_status,
                           insta_report=insta_report,
                           apk_status=apk_status)

if __name__ == "__main__":
    app.run(debug=True)   