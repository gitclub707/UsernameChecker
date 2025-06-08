import requests
import time
import os

# OPTIONAL: Set your GitHub Personal Access Token here for higher rate limits
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # or replace with your token as a string

def check_username(username):
    url = f"https://api.github.com/users/{username}"
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return "Available"
    elif response.status_code == 200:
        return "Taken"
    else:
        return f"Error ({response.status_code})"

def main():
    # Read usernames from list.txt
    with open("list.txt", "r") as f:
        usernames = [line.strip() for line in f if line.strip()]

    for username in usernames:
        status = check_username(username)
        print(f"{username}: {status}")
        # Sleep to avoid hitting rate limits
        time.sleep(1 if not GITHUB_TOKEN else 0.1)  # Faster if authenticated

if __name__ == "__main__":
    main()
