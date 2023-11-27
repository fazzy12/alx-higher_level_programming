# Python - Network #1

This repository contains Python scripts that demonstrate various network-related tasks 
using the `requests` library. Each script focuses on different aspects of network programming, 
including making HTTP requests, handling errors, and interacting with web APIs.

## Scripts

1. **0-hbtn_status.py**

   - Fetches the status of a specified URL using the `urllib` library.
   - Demonstrates how to use the `urlopen` function and handle the response.

2. **1-hbtn_header.py**

   - Takes a URL as a command-line argument, sends a request, and displays the value of the `X-Request-Id` variable from the response header.
   - Uses the `urllib` and `sys` libraries.

3. **2-post_email.py**

   - Sends a POST request to a specified URL with an email as a parameter.
   - Displays the body of the response.
   - Utilizes the `urllib` and `sys` libraries.

4. **3-error_code.py**

   - Takes a URL as a command-line argument, sends a request, and displays the body of the response.
   - Handles `urllib.error.HTTPError` exceptions and prints the HTTP status code if it's greater than or equal to 400.

5. **4-hbtn_status.py**

   - Fetches the status of a specified URL using the `requests` library.
   - Demonstrates the simplicity of making HTTP requests with the `requests` library.

6. **5-hbtn_header.py**

   - Takes a URL as a command-line argument, sends a request, and displays the value of the `X-Request-Id` variable from the response header.
   - Uses the `requests` and `sys` libraries.

7. **6-post_email.py**

   - Sends a POST request to a specified URL with an email as a parameter using the `requests` library.
   - Displays the body of the response.

8. **7-error_code.py**

   - Takes a URL as a command-line argument, sends a request, and displays the body of the response.
   - Prints an error message if the HTTP status code is greater than or equal to 400.
   - Uses the `requests` and `sys` libraries.

9. **8-json_api.py**

   - Takes a letter as a command-line argument, sends a POST request to a search API, and displays the results.
   - Handles JSON formatting and displays the id and name if the response is valid.
   - Uses the `requests` and `sys` libraries.

10. **10-my_github.py**

    - Takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user's id.
    - Demonstrates Basic Authentication with a personal access token.
    - Uses the `requests` and `sys` libraries.

11. **100-github_commits.py**

    - Takes repository name and owner name as command-line arguments, and uses the GitHub API to list the 10 most recent commits.
    - Prints commit information including SHA and author name.
    - Uses the `requests` and `sys` libraries.

## How to Run

To run these scripts, ensure you have Python installed on your machine. Execute each script by running the command `./script_name.py` in your terminal, providing any necessary command-line arguments.

Example:

```bash
./0-hbtn_status.py
```

#### Note
Be mindful of rate limits for unauthenticated requests, especially when using the GitHub API.