
import os
import requests
from flask import jsonify

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def get_pull_requests(state):
    """
    Example of return:
    [
        {"title": "Add useful stuff", "num": 56, "link": "https://github.com/boto/boto3/pull/56"},
        {"title": "Fix something", "num": 57, "link": "https://github.com/boto/boto3/pull/57"},
    ]
    """

    # Write your code here
    url = f"https://api.github.com/repos/boto/boto3/pulls?state={state}&per_page=100"
    response = requests.get(url, headers=HEADERS)
    print("START: ", response.status_code)
    if response.status_code == 200:
        data = response.json()
        pull_requests = []
        for pr in data:
            pull_requests.append({
                "title": pr["title"],
                "num": pr["number"],
                "link": pr["html_url"]
            })
        print(pull_requests)
        print("REQUEST: ", pull_requests)
        return pull_requests
    else:
        return jsonify({"error": "Failed to retrieve pull requests."})

