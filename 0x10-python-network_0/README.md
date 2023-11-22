# 0x10. Python - Network #0

## Overview

This project explores network programming in Python, focusing on the fundamentals of HTTP, URL parsing, cURL commands, and Bash scripting for network-related tasks. The scripts included cover a range of topics such as making HTTP requests, handling responses, dealing with JSON data, and more.

## Project Structure

The project directory contains a set of Bash and Python scripts, each addressing specific network-related tasks. Here's an overview of the scripts:

1. **0-simple_get.sh**: Simple Bash script for making a GET request to a specified URL using cURL.

2. **1-post_params.sh**: Bash script for making a POST request with parameters to a specified URL using cURL.

3. **2-get_data.sh**: Bash script for making a GET request to a URL and displaying the response body while handling errors.

4. **3-methods.sh**: Bash script for displaying the allowed HTTP methods for a given URL.

5. **4-header.sh**: Bash script for making a GET request to a URL with a custom header and displaying the response body.

6. **5-post_params.sh**: Bash script for making a POST request with parameters to a URL using cURL.

7. **6-peak.py, 6-peak.txt**: Python script and accompanying text file for finding a peak in an unsorted list of integers with optimized complexity.

8. **100-status_code.sh**: Bash script for making a request to a URL and displaying only the HTTP status code of the response.

9. **101-post_json.sh**: Bash script for sending a JSON POST request to a URL with validation of the JSON content.

10. **102-catch_me.sh**: Bash script for making a request to a URL that triggers a specific server response.

## Requirements

- All Bash scripts should be exactly 3 lines long.
- Scripts should be tested on Ubuntu 20.04 LTS.
- Python scripts should adhere to PEP8 style guidelines.
- Proper documentation using comments and docstrings in Python.

## How to Use

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/0x10-python-network-0.git
    ```

2. Navigate to the project directory:

    ```bash
    cd 0x10-python-network-0
    ```

3. Run the desired script using the appropriate command, e.g.,

    ```bash
    ./0-simple_get.sh http://example.com
    ```

## Testing

The scripts are designed to be tested in the provided sandbox environment, using the web server running on port 5000.

## Contribution

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
