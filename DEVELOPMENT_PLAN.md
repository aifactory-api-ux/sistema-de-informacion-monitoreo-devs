# DEVELOPMENT PLAN: Sistema de informacion Monitoreo Devs

## 1. ARCHITECTURE OVERVIEW

**Components:**
- **Frontend:** React 18 SPA with lazy-loaded components for charts, KPI cards, and data tables
- **API Gateway:** Nginx reverse proxy handling routing and static asset serving
- **Backend:** FastAPI microservice with JWT authentication, rate limiting, and structured logging
- **Database:** PostgreSQL 15 for primary data storage (migrated from SQLite)
- **Cache:** Redis for KPI aggregation caching and Celery message broker
- **Async Processing:** Celery workers for background metric collection from external APIs
- **External Integrations:** Git providers, CI/CD tools, issue trackers, and ui-avatars.com

**Core Models:**
- `Developer`: Team members with name, email, avatar_url
- `Sprint`: Development cycles with start/end dates and status
- `Metric`: Performance data (commits, code_reviews, deployments, bug_fixes) linked to developer and sprint
- `User`: System users with roles (admin, manager, developer) for authentication

**APIs:**
- `GET /api/health` - Service health check
- `POST /api/auth/login` - JWT authentication
- `GET /api/developers` - CRUD for developers catalog
- `GET /api/sprints` - CRUD for sprints catalog
- `GET /api/metrics` - Metric data (read-only per requirements)
- `GET /api/kpis` - Aggregated KPI calculations with Redis caching
- `POST /api/metrics/collect` - Trigger async metric collection (admin only)

**Folder Structure:**
```
devpulse/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard/
│   │   │   ├── Auth/
│   │   │   ├── KpiCards/
│   │   │   ├── Charts/
│   │   │   └── DataTable/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── index.js
│   ├── package.json
│   ├── Dockerfile
│   └── nginx.conf
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/
│   │   │   │   │   ├── auth.py
│   │   │   │   │   ├── developers.py
│   │   │   │   │   ├── sprints.py
│   │   │   │   │   ├── metrics.py
│   │   │   │   │   └── kpis.py
│   │   │   │   └── api.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── dependencies.py
│   │   ├── crud/
│   │   │   ├── base.py
│   │   │   ├── developer.py
│   │   │   ├── sprint.py
│   │   │   ├── metric.py
│   │   │   └── user.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   ├── base_class.py
│   │   │   ├── session.py
│   │   │   └── init_db.py
│   │   ├── models/
│   │   │   ├── developer.py
│   │   │   ├── sprint.py
│   │   │   ├── metric.py
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   ├── developer.py
│   │   │   ├── sprint.py
│   │   │   ├── metric.py
│   │   │   └── user.py
│   │   ├── services/
│   │   │   ├── cache.py
│   │   │   ├── metric_calculation.py
│   │   │   └── external_api.py
│   │   ├── tasks/
│   │   │   └── metric_collection.py
│   │   ├── alembic/
│   │   │   ├── versions/
│   │   │   ├── env.py
│   │   │   └── script.py.mako
│   │   ├── main.py
│   │   └── celery_app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── alembic.ini
├── shared/
│   └── models/
│       └── dto.py
├── docker-compose.yml
├── .env.example
├── .gitignore
├── .dockerignore
├── run.sh
├── run.bat
└── README.md
```

## 2. ACCEPTANCE CRITERIA

1. **Full System Operation:** Running `./run.sh` starts all services (PostgreSQL, Redis, FastAPI, Celery, React) with health checks, and the application is accessible at `http://localhost:3000` with a functional login screen.

2. **Core Functionality:** Users can log in with JWT authentication, view developer/sprint catalogs with CRUD operations (per HU-008), view metric dashboards with KPI cards and charts, and trigger async metric collection (admin only).

3. **Data Integrity:** System initializes with seed data (5 developers × 4 sprints = 20 metric records), metrics are read-only (no edit/delete), KPI calculations are cached in Redis with TTL, and all external API calls (avatars, Git) are properly handled with fallbacks.

## 3. EXECUTABLE ITEMS

### ITEM 1: Backend Foundation - Database Models & Core Infrastructure
**Goal:** Implement PostgreSQL database schema with Alembic migrations, SQLAlchemy models (Developer, Sprint, Metric, User), and core FastAPI application structure with health endpoint, structured logging, and environment validation.
**Files to create/modify:**
- `backend/app/models/developer.py` (create) - Developer model with id, name, email, avatar_url
- `backend/app/models/sprint.py` (create) - Sprint model with id, name, start_date, end_date, status
- `backend/app/models/metric.py` (create) - Metric model with id, developer_id, sprint_id, commits, code_reviews, deployments, bug_fixes, recorded_date
- `backend/app/models/user.py` (create) - User model with id, username, hashed_password, role
- `backend/app/db/base_class.py` (create) - Base SQLAlchemy model class
- `backend/app/db/base.py` (create) - Import all models for Alembic
- `backend/app/db/session.py` (create) - Database session factory with connection pooling
- `backend/app/db/init_db.py` (create) - Seed database with initial 20 metric records (5 devs × 4 sprints)
- `backend/app/core/config.py` (create) - Environment validation with pydantic-settings, fail-fast on missing secrets
- `backend/app/main.py` (create) - FastAPI app with CORS, structured JSON logging, /health endpoint
- `backend/alembic.ini` (create) - Alembic configuration
- `backend/app/alembic/env.py` (create) - Alembic environment setup
- `backend/app/alembic/versions/001_initial.py` (create) - Initial migration script
- `backend/requirements.txt` (create) - Python dependencies (fastapi, sqlalchemy, alembic, pydantic-settings, etc.)
**Tests required:**
- `tests/test_models.py`: test_model_relationships, test_metric_constraints
- `tests/test_config.py`: test_config_validation, test_missing_secret_fails
- `tests/test_health.py`: test_health_endpoint_returns_status
**Never do in this item:**
- Hardcode database credentials or JWT secret
- Use SQLite instead of PostgreSQL
- Skip foreign key constraints
**Dependencies:** None
**Validation:** `pytest backend/tests/` passes all tests, `alembic upgrade head` creates tables, `/health` returns `{"status": "healthy", "service": "devpulse-backend", "version": "1.0.0"}`

### ITEM 2: Authentication & Authorization Service
**Goal:** Implement JWT authentication with refresh tokens, role-based access control (admin, manager, developer), and secure password hashing. Protect all endpoints except /health and /auth/login.
**Files to create/modify:**
- `backend/app/core/security.py` (create) - JWT token creation/validation, password hashing with bcrypt, role checking
- `backend/app/core/dependencies.py` (create) - FastAPI dependencies for get_current_user, get_current_active_user, require_role
- `backend/app/schemas/user.py` (create) - Pydantic schemas for UserCreate, UserLogin, Token, TokenData
- `backend/app/crud/user.py` (create) - CRUD operations for User model with authentication
- `backend/app/api/v1/endpoints/auth.py` (create) - POST /auth/login, POST /auth/refresh, POST /auth/logout endpoints
- `backend/app/api/v1/api.py` (create) - API router with authentication dependency injection
**Tests required:**
- `tests/test_auth.py`: test_login_valid_credentials, test_login_invalid_password, test_token_refresh, test_role_validation_admin, test_role_validation_developer
**Never do in this item:**
- Store passwords in plain text
- Use weak JWT secret or hardcoded values
- Allow unauthorized access to protected endpoints
- Skip role validation on admin-only endpoints
**Dependencies:** Item 1 (Database Models)
**Validation:** Login with valid credentials returns JWT token, token grants access to protected endpoints, invalid token returns 401, admin role required for /api/metrics/collect

### ITEM 3: Developer & Sprint Catalog Management (HU-008)
**Goal:** Implement full CRUD API for developers and sprints catalogs as specified in HU-008, with proper validation, avatar URL generation using ui-avatars.com, and role-based permissions.
**Files to create/modify:**
- `backend/app/schemas/developer.py` (create) - Pydantic schemas for DeveloperCreate, DeveloperUpdate, DeveloperInDB
- `backend/app/schemas/sprint.py` (create) - Pydantic schemas for SprintCreate, SprintUpdate, SprintInDB
- `backend/app/crud/developer.py` (create) - CRUD operations for Developer model
- `backend/app/crud/sprint.py` (create) - CRUD operations for Sprint model
- `backend/app/crud/base.py` (create) - Base CRUD class with common operations
- `backend/app/api/v1/endpoints/developers.py` (create) - GET/POST/PUT/DELETE /api/developers with role checks
- `backend/app/api/v1/endpoints/sprints.py` (create) - GET/POST/PUT/DELETE /api/sprints with role checks
- `backend/app/services/external_api.py` (create) - Client for ui-avatars.com with fallback to local avatars
**Tests required:**
- `tests/test_developers.py`: test_create_developer, test_get_developer, test_update_developer, test_delete_developer, test_avatar_generation
- `tests/test_sprints.py`: test_create_sprint, test_get_sprint, test_update_sprint, test_delete_sprint, test_sprint_validation
**Never do in this item:**
- Allow metric editing/deletion (metrics are read-only per requirements)
- Skip validation on required fields
- Hardcode avatar URLs
**Dependencies:** Items 1-2 (Database, Authentication)
**Validation:** All CRUD operations work via API with proper authentication, avatar URLs are generated correctly, role permissions enforced (admin/managers can modify, developers read-only)

### ITEM 4: Metrics & KPI Calculation Service
**Goal:** Implement metrics data API (read-only), KPI aggregation service with Redis caching, and metric calculation logic for the 5 defined KPIs (sprint completion, PR review time, bug density, deployment frequency, platform adoption).
**Files to create/modify:**
- `backend/app/schemas/metric.py` (create) - Pydantic schemas for MetricCreate, MetricInDB, KPIResponse
- `backend/app/crud/metric.py` (create) - Read-only operations for Metric model
- `backend/app/services/cache.py` (create) - Redis client with connection pooling, cache get/set with TTL
- `backend/app/services/metric_calculation.py` (create) - Business logic for calculating all 5 KPIs from metric data
- `backend/app/api/v1/endpoints/metrics.py` (create) - GET /api/metrics (read-only, filtered by developer/sprint)
- `backend/app/api/v1/endpoints/kpis.py` (create) - GET /api/kpis with Redis caching (cache hit/miss logic)
**Tests required:**
- `tests/test_metrics.py`: test_get_metrics_filtered, test_metrics_read_only
- `tests/test_kpis.py`: test_kpi_calculation_sprint_completion, test_kpi_calculation_pr_review, test_redis_cache_hit, test_redis_cache_miss
- `tests/test_cache.py`: test_cache_set_get, test_cache_expiry
**Never do in this item:**
- Implement edit/delete for metrics (violates requirements)
- Calculate KPIs on every request without caching
- Hardcode KPI formulas without business logic
**Dependencies:** Items 1-3 (Database, Auth, CRUD)
**Validation:** KPI endpoint returns correct calculations, Redis caches results with 5-minute TTL, cache miss triggers recalculation, metrics endpoint returns filtered data

### ITEM 5: Async Metric Collection with Celery
**Goal:** Implement Celery workers for background metric collection from external APIs (Git, CI/CD, issue trackers), task queue with Redis broker, and admin endpoint to trigger collection.
**Files to create/modify:**
- `backend/app/celery_app.py` (create) - Celery application configuration with Redis broker
- `backend/app/tasks/metric_collection.py` (create) - Async tasks for fetching commits, PRs, deployments, bugs from external APIs
- `backend/app/api/v1/endpoints/metrics.py` (modify) - Add POST /api/metrics/collect (admin-only) to trigger async collection
- `backend/app/services/external_api.py` (modify) - Add clients for Git providers, CI/CD tools, issue trackers with mock implementations
**Tests required:**
- `tests/test_tasks.py`: test_metric_collection_task, test_external_api_mock, test_task_retry_logic
- `tests/test_metrics_endpoints.py`: test_trigger_collection_admin_only, test_collection_endpoint_validation
**Never do in this item:**
- Block HTTP requests waiting for external API calls
- Skip authentication on admin endpoint
- Hardcode external API credentials
**Dependencies:** Items 1-4 (all backend services)
**Validation:** Admin can trigger metric collection via API, Celery worker processes task, external API calls use mock when credentials missing, cache invalidated after collection

### ITEM 6: React Frontend Dashboard
**Goal:** Implement React 18 SPA with authentication flow, dashboard layout, KPI cards, lazy-loaded charts, and data tables for developers/sprints/metrics.
**Files to create/modify:**
- `frontend/src/App.jsx` (create) - Main app with routing (React Router)
- `frontend/src/components/Auth/Login.jsx` (create) - Login form with JWT token storage
- `frontend/src/components/Dashboard/Dashboard.jsx` (create) - Main dashboard layout
- `frontend/src/components/KpiCards/KpiCards.jsx` (create) - Display 5 KPI cards with values and trends
- `frontend/src/components/Charts/Charts.jsx` (create) - Lazy-loaded charts (line/bar) for metric trends
- `frontend/src/components/DataTable/DataTable.jsx` (create) - Interactive tables for developers/sprints/metrics
- `frontend/src/services/api.js` (create) - Axios client with auth interceptors
- `frontend/src/services/auth.js` (create) - Token management and role checking
- `frontend/package.json` (create) - React 18 dependencies with charting library
- `frontend/Dockerfile` (create) - Multi-stage build with nginx for production
- `frontend/nginx.conf` (create) - Nginx configuration for SPA routing
**Tests required:**
- `frontend/src/__tests__/Auth.test.jsx`: test_login_success, test_login_failure
- `frontend/src/__tests__/KpiCards.test.jsx`: test_kpi_cards_render, test_data_fetching
**Never do in this item:**
- Store JWT tokens in localStorage without secure flags
- Hardcode API URLs
- Skip loading states for async data
**Dependencies:** Items 1-5 (backend APIs must be available)
**Validation:** Frontend builds without errors, login works, dashboard displays KPI cards and charts, tables show data from backend

### ITEM 7: Infrastructure & Deployment (REQUIRED — PROJECT MUST RUN)
**Goal:** Complete Docker setup — zero manual steps, runs with './run.sh'
**Files to create/modify:**
- `docker-compose.yml` (create) - All services (postgres, redis, backend, celery, frontend) with healthchecks + depends_on
- `backend/Dockerfile` (create) - Multi-stage build with Python 3.11, non-root user, production optimizations
- `frontend/Dockerfile` (create) - Multi-stage build with Node 18, nginx serving built assets
- `.env.example` (create) - All variables with descriptions: DATABASE_URL, REDIS_URL, JWT_SECRET, EXTERNAL_API_KEYS, etc.
- `.gitignore` (create) - Exclude node_modules, dist, .env, __pycache__, *.pyc, .DS_Store
- `.dockerignore` (create) - Exclude