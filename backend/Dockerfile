FROM kalilinux/kali-rolling

# Install required system packages
RUN apt update && apt install -y \
    python3 \
    python3-pip \
    gcc \
    libcurl4-openssl-dev \
    libssl-dev \
    wfuzz \
    python3-setuptools

# Set working directory
WORKDIR /app

# Copy FastAPI files
COPY ./main.py .

# Optional: copy the rest of the app if needed
# COPY ./controller ./controller
# COPY ./dictionaries ./dictionaries

# Install Python dependencies
RUN pip3 install --no-binary :all: pycurl --break-system-packages && \
    pip3 install fastapi uvicorn python-multipart --break-system-packages

# Expose port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
