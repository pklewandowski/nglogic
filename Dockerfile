# Stage 1: Base build stage
FROM python:3.13-slim AS builder

ARG APPDIR=nglogic_app
# Create the app directory
RUN mkdir /$APPDIR

# Set the working directory
WORKDIR /$APPDIR

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies first for caching benefit
RUN pip install --upgrade pip
COPY requirements.txt /$APPDIR/
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production stage
FROM python:3.13-slim

ARG APPDIR=nglogic_app

RUN useradd -m -r appuser &&  \
    mkdir /$APPDIR && \
    chown -R appuser /$APPDIR

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /$APPDIR

# Copy application code
COPY --chown=appuser:appuser . .

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Make entry file executable
RUN chmod +x  /$APPDIR/entrypoint.prod.sh

# Start the application using Gunicorn
CMD ["/nglogic_app/entrypoint.prod.sh"]