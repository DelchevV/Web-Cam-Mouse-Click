Mouse Capture App
The Mouse Capture App is a Python application that captures the movement of the mouse cursor and takes a picture from a connected webcam when the left mouse button is clicked. The captured data, including mouse coordinates, webcam image, and timestamp, is saved in an SQLite database.

Features
Real-time tracking of mouse cursor movement.
Webcam image capture upon left mouse button click.
Storage of captured data in an SQLite database.
Requirements
Ensure you have the following installed:

Python 3.8 or later
Dependencies listed in requirements.txt
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/mouse-capture-app.git
Navigate to the project directory:

bash
Copy code
cd mouse-capture-app
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:
bash
Copy code
venv\Scripts\activate
Unix or MacOS:
bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the web server:

bash
Copy code
python webserver.py
Open your web browser and navigate to http://localhost:8080.

Move the mouse cursor, and the coordinates will be displayed in real-time.

Click the left mouse button to capture an image from the webcam. The captured data will be stored in the SQLite database.

Structure
The project is structured as follows:

app/: Python modules for different components.
__init__.py: Initialization file for the app module.
webserver.py: Web server implementation using aiohttp.
mouse_reader.py: Module for reading mouse coordinates.
webcam_capture.py: Module for capturing images from the webcam.
database.py: Module for SQLite database operations.
main.py: Main script to run the application.
requirements.txt: List of project dependencies.
static/: Static files for the web server.
templates/: HTML templates for the web server.
License
This project is licensed under the MIT License - see the LICENSE file for details.
