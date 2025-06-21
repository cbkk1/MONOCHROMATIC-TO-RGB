# MONOCHROMATIC-TO-RGB

> A Flask-based B.Tech project that converts monochromatic images to full RGB color.

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)  
2. [Demo](#demo)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Requirements](#requirements)  
6. [Project Structure](#project-structure)  
7. [Contributing & Team](#contributing--team)  
8. [Contact](#contact)  

---

## 🚀 Project Overview

**MONOCHROMATIC-TO-RGB** is a web application built with Flask that takes a single-channel (monochrome) image as input, processes it through a colorization pipeline, and returns a fully colorized RGB image. Processing progress is logged in the terminal; once complete, the result is displayed in your browser.

---

## 🎬 Demo

1. Start the server:  
   ```bash
   python3 app.py


   In your browser, open the URL printed in the terminal (e.g. http://127.0.0.1:5000/).

Upload a monochrome image.

Watch the terminal for processing progress (percentage).

View your colorized image in the browser.

If an error occurs, a default placeholder image is shown; error details will appear in the terminal.

⚙️ Installation
Clone this repository

bash
Copy
Edit
git clone https://github.com/cbkk1/MONOCHROMATIC-TO-RGB.git
cd MONOCHROMATIC-TO-RGB
Create & activate a virtual environment (strongly recommended)

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
▶️ Usage
With your virtual environment activated:

bash
Copy
Edit
python3 app.py
Open the printed http://127.0.0.1:5000/ in a browser.

Upload your monochrome image.

Wait for processing to complete (progress shown in terminal).

View or download the resulting RGB image.

📦 Requirements
All Python dependencies are listed in requirements.txt. Key libraries include:

Flask – Web framework

Matplotlib – Image I/O and visualization

IPython – Interactive debugging & notebooks

Torch (optional) – If you’re using a neural-based colorization model

Other image-processing utilities

Install via:

bash
Copy
Edit
pip install -r requirements.txt
🗂 Project Structure
php
Copy
Edit
MONOCHROMATIC-TO-RGB/
├── app.py              # Flask application entry point
├── static/             # Static files (CSS, JS, default images)
├── templates/          # HTML templates
├── models/             # (Optional) Pretrained colorization models
├── requirements.txt    # Python dependencies
└── README.md           # This file
🤝 Contributing & Team
This project was developed as a B.Tech final-year project under VTU and Alva’s Institute of Engineering and Technology.

Name	Role	Email	Contact
Anooj Raj	Lead Developer	anoojraj07@gmail.com	+91-81518-25515
Ashik H. R.	Backend & Model Integration	hra72020@gmail.com	+91-97311-793195
Chetan M. Wali	Frontend & UI Design	chetanwali2001@gmail.com	+91-63638-85750
Chinmaya Bhat K. K.	Project Coordinator	chinmayabhatkk@gmail.com	+91-98958-07455
Dr. Vasudev S. Shahapur	Guide & Advisor	vasu.shahapur@aiet.org.in	+91-94495-86008

