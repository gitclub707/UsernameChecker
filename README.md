
# UsernameChecker

**Bulk GitHub Username Checker**

UsernameChecker is a simple Python tool that checks the availability of multiple GitHub usernames in bulk. It reads a list of usernames from a text file and uses the GitHub API to determine if each username is taken or available.

---

## Features

- Bulk checking of GitHub usernames
- Reads usernames from a file (`list.txt`)
- Simple, clear output
- Supports GitHub API authentication for higher rate limits

---

## Requirements

- Python 3.7+
- [requests](https://pypi.org/project/requests/) Python package

---

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/DexterZero/UsernameChecker.git
   cd UsernameChecker
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

---

## Usage

1. **Prepare your `list.txt`:**

   Add one username per line in `list.txt`, for example:
   ```
   octocat
   somefakename123
   anotheruser
   ```

2. **(Optional) Set your GitHub API token for higher rate limits:**

   - Create a [personal access token](https://github.com/settings/tokens).
   - Set it as an environment variable:
     ```bash
     export GITHUB_TOKEN=your_token_here
     ```

3. **Run the checker:**
   ```bash
   python g.py
   ```

---

## Example Output

```
octocat: Taken
somefakename123: Available
anotheruser: Taken
```

---

## Notes

- **Rate Limiting:**  
  - Unauthenticated: 60 requests/hour  
  - Authenticated: 5,000 requests/hour

- **Customization:**  
  You can adjust the script to save results to a file or change the delay between requests.

---

## License

This project is licensed under the MIT License.
