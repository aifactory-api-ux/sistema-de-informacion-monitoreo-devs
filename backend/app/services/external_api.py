import os

# Mock implementations for external API clients

def fetch_commits():
    # Mock fetching commits from a Git provider
    return [
        {"id": "commit1", "message": "Initial commit"},
        {"id": "commit2", "message": "Added new feature"}
    ]

def fetch_pull_requests():
    # Mock fetching pull requests from a Git provider
    return [
        {"id": "pr1", "title": "Fix bug"},
        {"id": "pr2", "title": "Improve performance"}
    ]

def fetch_deployments():
    # Mock fetching deployments from a CI/CD tool
    return [
        {"id": "deploy1", "status": "success"},
        {"id": "deploy2", "status": "failed"}
    ]

def fetch_bugs():
    # Mock fetching bugs from an issue tracker
    return [
        {"id": "bug1", "description": "Crash on load"},
        {"id": "bug2", "description": "UI glitch"}
    ]
