# Running the Pink Todo App Locally

Follow these steps to run the application locally:

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd pink-todo-simulation
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Migrate the database:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    # Follow the prompts to create a user.
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7.  **Access the app in your browser:**

    Open your web browser and go to `http://localhost:8000/`
