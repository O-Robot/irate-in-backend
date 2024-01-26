# iRatein Chat Application

## Overview

Welcome to the iRatein Chat Application! This project is a simple chat application built using Django Rest Framework. Users can create accounts, join chat rooms, and engage in real-time conversations.

## Prerequisites

Before you start, make sure you have the following prerequisites installed:

- Python 3.x
- Django
- Redis server
- Docker

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/O-Robot/irate-in-backend.git
    cd django-chat-app
    ```

2. **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Create an environment file:**
    ```bash
    cp .env.sample .env
    ```

    Edit the `.env` file and configure the necessary settings, such as redis port and secret key.

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```

6. **Open another terminal and start the Redis server using Docker:**
    ```bash
    docker run -e ALLOW_EMPTY_PASSWORD=yes -p 6379:6379 bitnami/redis
    ```

7. **Access the application in your browser at [http://127.0.0.1:8000](http://l27.0.0.1:8000).**

## Usage

- Create a new account or log in if you already have one.
- Join existing chat rooms or create new ones.
- Start chatting with other users in real-time!

## Important Notes

- Ensure that the Redis server is running before using the chat application.
- The Redis server can be started using the following Docker command:
    ```bash
    docker run -e ALLOW_EMPTY_PASSWORD=yes -p 6379:6379 bitnami/redis
    ```

- Make sure to set up the `.env` file with the correct configuration.

## Documentation

Explore the detailed documentation for this project at [http://127.0.0.1:8000/api/v1/doc](http://l27.0.0.1:8000/api/v1/doc).

## Live Demo

Check out the live demo of the application hosted at [https://irateinchat.pythonanywhere.com/api/v1/doc/](https://irateinchat.pythonanywhere.com/api/v1/doc/)

## Contact

For any inquiries, please contact [adewaleogooluwani@gmail.com].

Happy chatting! 🎉
