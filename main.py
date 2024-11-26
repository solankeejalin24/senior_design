import requests, json
import os
from dotenv import load_dotenv

load_dotenv()  # This loads environment variables from .env file
# print("BASE_URL:", os.getenv('BASE_URL'))
# print("USER:", os.getenv('USER'))
# print("API_TOKEN:", os.getenv('API_TOKEN'))

class JiraClient:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        self.base_url = os.getenv('BASE_URL')
        self.user = os.getenv('USER')
        self.api_token = os.getenv('API_TOKEN')
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    
    def get_issues(self):
        """Fetch all issues from the Jira project."""
        try:
            response = requests.get(self.base_url, headers=self.headers, auth=(self.user, self.api_token))
            response.raise_for_status()  # Raise an error if the request failed
            return response.json().get("issues", [])
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

class Issue:
    def __init__(self, issue_data):
        """Initialize an Issue object from the API response data."""
        self.key = issue_data["key"]
        self.summary = issue_data["fields"].get("summary", "No summary available")
        self.issue_type = issue_data["fields"].get("issuetype", {}).get("name", "No issue type available")
        self.description = self.extract_description(issue_data["fields"].get("description", {}))
        self.assignee = issue_data["fields"].get("assignee", {}).get("displayName", "Unassigned")
        self.creator = issue_data["fields"].get("creator", {}).get("displayName", "Unknown")
        self.reporter = issue_data["fields"].get("reporter", {}).get("displayName", "Unknown")
        self.project_name = issue_data['fields']['project']['name']
        self.status = issue_data['fields']['status']['name']

    @staticmethod
    def extract_description(description_field):
        """Extract text description from the content field."""
        if not description_field:
            return "No description available"
        
        description_content = description_field.get("content", [])
        for paragraph in description_content:
            for text in paragraph.get("content", []):
                return text.get("text", "No description available")
        return "No description available"

    def display(self):
        """Print issue details."""
        print(f"Project Name: {self.project_name}")
        print(f"Issue ID: {self.key}")
        print(f"Issue Name: {self.summary}")
        print(f"Issue Type: {self.issue_type}")
        print(f"Issue Description: {self.description}")
        print(f"Assignee: {self.assignee}")
        print(f"Creator: {self.creator}")
        print(f"Reporter: {self.reporter}")
        print(f"Status: {self.status}")
        print("===========================================================")


if __name__ == "__main__":
    # Initialize JiraClient
    jira_client = JiraClient()
    
    # Fetch issues
    issues = jira_client.get_issues()
    
    # Display each issue's details
    for issue_data in issues:
        issue = Issue(issue_data)
        issue.display()

