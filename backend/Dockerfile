FROM kalilinux/kali-rolling

# Install Python and wfuzz
RUN apt update && apt install -y python3 python3-pip wfuzz

# Set working directory
WORKDIR /app

# Copy FastAPI files
COPY ./main.py .

# Install FastAPI and Uvicorn
RUN pip3 install fastapi uvicorn --break-system-packages

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
