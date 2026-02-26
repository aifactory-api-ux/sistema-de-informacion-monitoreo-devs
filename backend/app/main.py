from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Structured logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "devpulse-backend", "version": "1.0.0"}

# Environment validation
if not os.getenv('DATABASE_URL'):
    logger.error('DATABASE_URL environment variable is required')
    raise EnvironmentError('DATABASE_URL environment variable is required')
