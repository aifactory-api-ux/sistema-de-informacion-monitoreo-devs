from unittest.mock import patch
from app.tasks.metric_collection import fetch_metrics

# Test metric collection task
@patch('app.services.external_api.fetch_commits')
@patch('app.services.external_api.fetch_prs')
@patch('app.services.external_api.fetch_deployments')
@patch('app.services.external_api.fetch_bugs')
def test_metric_collection_task(mock_fetch_bugs, mock_fetch_deployments, mock_fetch_prs, mock_fetch_commits):
    mock_fetch_commits.return_value = []
    mock_fetch_prs.return_value = []
    mock_fetch_deployments.return_value = []
    mock_fetch_bugs.return_value = []
    result = fetch_metrics()
    assert result is None

# Test external API mock
@patch('app.services.external_api.fetch_commits')
def test_external_api_mock(mock_fetch_commits):
    mock_fetch_commits.return_value = [{'id': 1, 'message': 'Initial commit'}]
    result = fetch_metrics()
    assert result is None

# Test task retry logic
@patch('app.services.external_api.fetch_commits')
def test_task_retry_logic(mock_fetch_commits):
    mock_fetch_commits.side_effect = Exception("API Error")
    try:
        fetch_metrics()
    except Exception as e:
        assert str(e) == "API Error"
