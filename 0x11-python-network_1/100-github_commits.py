#!/usr/bin/python3
"""
Fetches and lists the 10 most recent commits from a GitHub repository.

Usage:
    ./100-github_commits.py <repository_name> <owner_name>
"""


import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    api_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(api_url)

    if response.status_code == 200:
        commits = response.json()[:10]

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits. Status Code:\
            {response.status_code}")
