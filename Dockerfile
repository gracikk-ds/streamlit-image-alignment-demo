FROM python:3.10-slim-buster
LABEL maintainer="asgordeev"

ARG PORT=8501

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY files to container
WORKDIR /app
COPY src/ src/
COPY app.py .
COPY setup.py .
RUN pip install .

# Run app
CMD streamlit run app.py --server.port $PORT
