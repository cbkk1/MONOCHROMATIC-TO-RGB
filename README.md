MONOCHROMATIC-TO-RGB
A Flask-based B.Tech project that converts monochromatic images to full RGB color.

TABLE OF CONTENTS

Project Overview

Demo

Installation

Usage

Requirements

Project Structure

Contributing & Team

Contact

PROJECT OVERVIEW
MONOCHROMATIC-TO-RGB is a web application built with Flask that takes a single-channel (monochrome) image as input, processes it through a colorization pipeline, and returns a fully colorized RGB image. Processing progress is logged in the terminal; once complete, the result is displayed in your browser.

DEMO

Start the server:
python3 app.py

In your browser, open the URL printed in the terminal (e.g. http://127.0.0.1:5000/).

Upload a monochrome image.

Watch the terminal for processing progress (percentage).

View your colorized image in the browser.

If an error occurs, a default placeholder image is shown; error details will appear in the terminal.

INSTALLATION

Clone this repository
git clone https://github.com/cbkk1/MONOCHROMATIC-TO-RGB.git
cd MONOCHROMATIC-TO-RGB

Create & activate a virtual environment (strongly recommended)
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

USAGE
With your virtual environment activated:
python3 app.py
– Open the printed http://127.0.0.1:5000/ in a browser.
– Upload your monochrome image.
– Wait for processing to complete (progress shown in terminal).
– View or download the resulting RGB image.

REQUIREMENTS
All Python dependencies are listed in requirements.txt. Key libraries include:
• Flask – Web framework
• Matplotlib – Image I/O and visualization
• IPython – Interactive debugging & notebooks
• Torch (optional) – If you’re using a neural-based colorization model
• Other image-processing utilities

Install via:
pip install -r requirements.txt

PROJECT STRUCTURE
MONOCHROMATIC-TO-RGB/
├── app.py Flask application entry point
├── static/ Static files (CSS, JS, default images)
├── templates/ HTML templates
├── models/ (Optional) Pretrained colorization models
├── requirements.txt Python dependencies
└── README.txt This file

CONTRIBUTING & TEAM
This project was developed as a B.Tech final-year project under VTU and Alva’s Institute of Engineering and Technology.

Name	Role	Email	Contact
Anooj Raj	Lead Developer	anoojraj07@gmail.com	+91-81518-25515
Ashik H. R.	Backend & Model Integration	hra72020@gmail.com	+91-97311-793195
Chetan M. Wali	Frontend & UI Design	chetanwali2001@gmail.com	+91-63638-85750
Chinmaya Bhat K. K.	Project Coordinator	chinmayabhatkk@gmail.com	+91-98958-07455
Dr. Vasudev S. Shahapur	Guide & Advisor	vasu.shahapur@aiet.org.in	+91-94495-86008

CONTACT
For questions or contributions, feel free to open an issue or reach out to any of the project associates listed above.

Thank you for using MONOCHROMATIC-TO-RGB! 🎨✨





