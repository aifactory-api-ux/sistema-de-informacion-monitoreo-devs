import pytest
from backend.app.models import Developer, Sprint, Metric, User

def test_developer_model():
    developer = Developer(name='John Doe', email='john@example.com', avatar_url='http://example.com/avatar.jpg')
    assert developer.name == 'John Doe'
    assert developer.email == 'john@example.com'
    assert developer.avatar_url == 'http://example.com/avatar.jpg'

def test_sprint_model():
    sprint = Sprint(name='Sprint 1', start_date='2023-01-01', end_date='2023-01-15', status='active')
    assert sprint.name == 'Sprint 1'
    assert sprint.start_date == '2023-01-01'
    assert sprint.end_date == '2023-01-15'
    assert sprint.status == 'active'

def test_metric_model():
    metric = Metric(commits=10, code_reviews=5, deployments=2, bug_fixes=1)
    assert metric.commits == 10
    assert metric.code_reviews == 5
    assert metric.deployments == 2
    assert metric.bug_fixes == 1

def test_user_model():
    user = User(username='admin', email='admin@example.com', role='admin')
    assert user.username == 'admin'
    assert user.email == 'admin@example.com'
    assert user.role == 'admin'
