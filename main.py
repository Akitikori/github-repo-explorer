import requests
from tabulate import tabulate

# Ask the user for their username
username = input("Enter the GitHub username: ")

# Define the API URL
url = f"https://api.github.com/users/{username}/repos"

# Send the GET request to the GitHub API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    repos = response.json()
    print(f"Fetched {len(repos)} repositories for user '{username}'")
    # prepare table
    table = []
    # Loop through the repositories and print details
    for repo in repos:
        table.append([repo['name'],repo['stargazers_count'], repo['description']])
    headers = ['Repository Name', 'Stars','Description']
    print(tabulate(table, headers=headers, tablefmt='grid'))
else:
    # Handle errors (e.g., user not found or rate limit exceeded)
    print(f"Failed to fetch repositories. Status code: {response.status_code}")