@echo off

REM Load environment variables
if not exist .env (
  echo Environment file (.env) not found!
  exit /b 1
)

for /f "tokens=*" %%i in ('type .env ^| findstr /r /v "^#"') do set %%i

echo Starting Docker Compose...
docker-compose up --build
