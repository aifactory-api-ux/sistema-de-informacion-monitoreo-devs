# DevPulse Monitoring System

DevPulse is a comprehensive monitoring system designed to track developer performance metrics and KPIs. It integrates with various external services to collect data and provides a user-friendly dashboard for visualization.

## Features

- **Authentication**: Secure login with JWT
- **Dashboard**: View KPIs, charts, and data tables
- **Async Processing**: Background metric collection using Celery
- **Caching**: Redis for KPI caching

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/devpulse.git
   cd devpulse
   ```

2. Copy the example environment file and configure it:
   ```bash
   cp .env.example .env
   ```

3. Run the application:
   ```bash
   ./run.sh
   ```

The application will be available at `http://localhost:3000`.

## Development

To start the development server for the frontend:

```bash
cd frontend
npm start
```

## Testing

To run tests:

```bash
cd frontend
npm test
```

## License

This project is licensed under the MIT License.
