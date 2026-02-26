from sqlalchemy.orm import Session
from backend.app.models.developer import Developer
from backend.app.models.sprint import Sprint
from backend.app.models.metric import Metric

# Seed database with initial data

def init_db(db: Session) -> None:
    # Create initial developers
    developers = [
        Developer(name=f'Developer {i}', email=f'dev{i}@example.com', avatar_url=f'https://ui-avatars.com/api/?name=Developer+{i}')
        for i in range(1, 6)
    ]
    db.add_all(developers)
    db.commit()

    # Create initial sprints
    sprints = [
        Sprint(name=f'Sprint {i}', start_date='2023-01-01', end_date='2023-01-15', status='completed')
        for i in range(1, 5)
    ]
    db.add_all(sprints)
    db.commit()

    # Create initial metrics
    for dev in developers:
        for sprint in sprints:
            metric = Metric(
                developer_id=dev.id,
                sprint_id=sprint.id,
                commits=5,
                code_reviews=3,
                deployments=2,
                bug_fixes=1,
                recorded_date='2023-01-10'
            )
            db.add(metric)
    db.commit()
