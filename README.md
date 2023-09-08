# Streamlit Image Alignment Demo

This project is a Streamlit web application for aligning and processing images using OpenCV. It allows users to upload an image of their choice, process it, and display the original and processed images along with length and width information.

## Features

- Upload an image in JPG, JPEG, PNG, BMP, or GIF format.
- Process the uploaded image to align metal elements and extract length and width information.
- Display the original and rotated images.
- Print the length and width of the processed metal element.

## Prerequisites

Before running the Streamlit app, make sure you have the following prerequisites installed:

- Python (3.8+ recommended)
- pip package manager
- OpenCV (`cv2`) library
- Streamlit library

You can install Streamlit and OpenCV using pip:

```bash
pip install -r requirements.txt
```

And than run streamlit app:

```bash
streamlit run app.py
```

## Running with Docker

You can run the Streamlit Image Alignment Demo using Docker for easy setup and execution. Follow these steps to run the application inside a Docker container:

1. Ensure you have Docker installed on your machine. You can download and install Docker from the [official website](https://www.docker.com/get-started).

2. Clone this repository to your local machine:

```bash
git clone https://github.com/gracikk-ds/streamlit-image-alignment-demo.git
cd streamlit-image-alignment-demo
```

3. Build a Docker image from the provided Dockerfile. This image will contain the necessary dependencies and the Streamlit app:

```bash
docker build -t streamlit-image-alignment-demo .
```

4. Once the Docker image is built, you can run the application in a Docker container:

```bash
docker run -p 8501:8501 streamlit-image-alignment-demo
```

Replace 8501 with the desired port if you want to run the app on a different port.

Access the Streamlit app in your web browser by visiting <http://localhost:8501> (or the chosen port) in your browser.

Upload an image, process it, and explore the features of the application.

When you're finished, you can stop the Docker container by pressing Ctrl+C in the terminal where it's running.
