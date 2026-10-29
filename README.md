# Factory Traffic Management System

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/cooperverse/factory-traffic-management)

This repository contains the backend service for a factory traffic management system. Built with Django and Django REST Framework, it provides a robust API to manage traffic junctions, process sensor data, control traffic signals, and maintain historical audit logs. The system is designed to intelligently manage vehicle flow within a factory or industrial complex.

## Project Structure

The project is organized into several distinct Django apps, each with a specific responsibility:

-   **`junctions`**: Manages the core entities of the system, including traffic junctions and the state of their individual signals (e.g., North, South, East, West).
-   **`sensors`**: Handles the intake and processing of data from vehicle detection sensors. It records events like vehicle arrivals and departures at junctions.
-   **`traffic_control`**: Contains the central logic for traffic management. It maintains the vehicle queue for each junction approach and manages the operational state (mode, phase) of each junction.
-   **`controllers`**: Facilitates communication with the physical traffic light controller hardware. It is responsible for sending commands (e.g., set signal state) and processing incoming events (e.g., acknowledgements, status updates) from the devices.
-   **`history`**: Provides an audit trail by logging all significant events, state changes, and commands issued within the system.
-   **`core`**: The main Django project configuration, including settings and URL routing.

## Features

-   **Junction Management**: Create and manage traffic junctions with individual signal states for each direction.
-   **Sensor Event Processing**: Ingest and process real-time events from sensors indicating vehicle presence.
-   **Vehicle Queueing**: Maintain a queue of waiting vehicles for each junction and direction.
-   **Traffic State Control**: Manage the operational mode (Automatic, Manual, Emergency) and traffic phase (North-South, East-West) of each junction.
-   **Controller Communication**: Abstract layer for sending commands to and receiving feedback from signal controllers.
-   **Device Status Monitoring**: Track the operational status (Online, Offline, Degraded) of controllers and sensors.
-   **Auditing**: Comprehensive logging of system activities for history and analysis.
-   **RESTful API**: A complete set of API endpoints to interact with and manage the system.

## Getting Started

To run the project locally, follow these steps.

### Prerequisites

-   Python 3.8+
-   `pip`

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/cooperverse/factory-traffic-management.git
    cd factory-traffic-management
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser account (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The API will now be available at `http://127.0.0.1:8000/`. You can access the Django admin interface at `http://127.0.0.1:8000/admin/`.

## API Endpoints

The following are the primary API endpoints provided by the service.

### Junctions (`/api/junctions/`)

-   `GET /api/junctions/`: List all created junctions.
-   `POST /api/junctions/`: Create a new junction.
-   `GET /api/junctions/<int:pk>/`: Retrieve details for a specific junction.

### Sensors (`/api/sensors/`)

-   `POST /api/sensors/events/submit/`: Submit a new sensor event (e.g., vehicle arrived/cleared).
-   `GET /api/sensors/events/`: List all received sensor events.

### Traffic Control (`/api/traffic-control/`)

-   `GET /api/traffic-control/states/`: List the control states for all junctions.
-   `GET /api/traffic-control/states/<int:pk>/`: Retrieve the control state for a specific junction.
-   `GET /api/traffic-control/queue/`: List all vehicles currently waiting in queues across all junctions.

### Controllers (`/api/controllers/`)

-   `GET /api/controllers/commands/`: List all commands sent to controllers.
-   `POST /api/controllers/events/submit/`: Endpoint for controllers to submit events (e.g., acknowledgements, status).
-   `GET /api/controllers/events/`: List all events received from controllers.
-   `GET /api/controllers/devices/`: List the operational status of all registered devices (controllers, sensors).

### History (`/api/history/`)

-   `GET /api/history/`: List all audit log entries for the system.
