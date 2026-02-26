from celery import shared_task
from app.services.external_api import fetch_commits, fetch_pull_requests, fetch_deployments, fetch_bugs

@shared_task(bind=True, max_retries=3)
def collect_metrics(self):
    try:
        commits = fetch_commits()
        pull_requests = fetch_pull_requests()
        deployments = fetch_deployments()
        bugs = fetch_bugs()
        # Process and store metrics
        # This is a placeholder for actual processing logic
        print(f"Collected {len(commits)} commits, {len(pull_requests)} PRs, {len(deployments)} deployments, {len(bugs)} bugs")
    except Exception as exc:
        raise self.retry(exc=exc)
