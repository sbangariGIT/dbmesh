# Use a lightweight Python image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Install uv package manager
RUN pip install --no-cache-dir uv

# Copy the application files
COPY app.py pyproject.toml /app/

# Install dependencies using uv
RUN uv venv && uv pip install --system --no-cache-dir

# Expose port for FastAPI server
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "dbmesh.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

