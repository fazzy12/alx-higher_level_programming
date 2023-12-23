# JavaScript - Web scraping

## Overview
This project focuses on JavaScript programming, specifically web scraping. Through a series of tasks, you'll get hands-on experience with manipulating JSON data, working with the request module, and utilizing APIs, especially the Star Wars API.

## Learning Objectives
- Understand why JavaScript programming is exceptional.
- Gain proficiency in manipulating JSON data.
- Familiarize yourself with the request and fetch API.
- Learn how to read and write files using the fs module.

## Prerequisites
**Node.js**: Ensure you have Node 14.x installed. If not, you can install it using the provided commands.

```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```
**Semi-Standard**: To ensure code consistency, the semi-standard coding style is recommended. Install it globally with:
```
sudo npm install semistandard --global
```
**Request Module**: This module simplifies making HTTP requests and is used extensively in the tasks.

```
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```
## Setup and Usage
1. Clone the repository:

```
git clone [repository-url]
cd 0x14-javascript-web_scraping
```
2. Navigate to the respective directory of each task and execute the script as demonstrated in the task descriptions.

## Tasks Overview
0. **0-readme.js**: Reads and prints the content of a file.
1. **1-writeme.js**: Writes a given string to a file.
2. **2-statuscode.js**: Displays the status code of a GET request.
3. **3-starwars_title.js**: Prints the title of a Star Wars movie based on its ID.
4. **4-starwars_count.js**: Determines the number of movies a specific Star Wars character appears in.
5. **5-request_store.js**: Retrieves content from a webpage and stores it in a file.
6. **6-completed_tasks.js**: Calculates the number of tasks completed by a user.
7. **100-starwars_characters.js**: Lists all characters from a Star Wars movie.
8. **101-starwars_characters.js**: Lists characters in the order they appear in the movie.

## Notes
- Ensure that all JavaScript files are executable.
- All scripts must adhere to the provided guidelines regarding file headers and coding standards.
- Always check the README of each task directory for specific instructions or notes.

**Copyright © 2023 ALX, All rights reserved**.