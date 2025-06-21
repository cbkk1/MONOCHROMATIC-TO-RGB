```markdown
# MONOCHROMATIC-TO-RGB
##  Table of Contents
1. [Project Overview](#project-overview)
2. [Demo](#demo)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Requirements](#requirements)
6. [Project Structure](#project-structure)
7. [Contributing & Team](#contributing--team)
8. [Contact](#contact)
```
---

##Project Overview

**MONOCHROMATIC-TO-RGB** is a web application built with Flask that:

- Accepts single-channel (monochrome) images

- Processes them through a colorization pipeline

- Returns fully colorized RGB images

- Shows real-time processing progress in terminal

- Displays results directly in the browser

---

## 🎬 Demo

1. **Start the server**:

```bash

python3 app.py

```

2. Open the URL shown in terminal (e.g. `http://127.0.0.1:5000/`)

3. Upload a monochrome image

4. Monitor terminal for processing progress (%)

5. View colorized result in browser

> 💡 *Note: If errors occur, a placeholder image is shown with detailed errors in terminal*

---

## ⚙️ Installation

1. Clone repository:

```bash

git clone https://github.com/cbkk1/MONOCHROMATIC-TO-RGB.git

cd MONOCHROMATIC-TO-RGB

```

2. Create & activate virtual environment:

```bash

python3 -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate    # Windows

```

3. Install dependencies:

```bash

pip install -r requirements.txt

```

---

## ▶️ Usage

1. Start Flask server:

```bash

python3 app.py

```

2. Visit `http://localhost:5000` in browser

3. Upload monochrome image via web interface

4. Wait for processing (terminal shows progress)

5. Download/view colorized result

---

## 📦 Requirements

Core dependencies (see `requirements.txt` for full list):

- Flask (Web framework)

- Matplotlib (Image I/O)

- Torch (Neural network backend)

- OpenCV (Image processing)

- NumPy (Numerical operations)

Install all requirements:

```bash

pip install -r requirements.txt

```

---

## 🗂 Project Structure

```

MONOCHROMATIC-TO-RGB/

├── app.py              # Flask application entry point

├── static/             # CSS, JS, default images

├── templates/          # HTML templates

├── models/             # Pretrained colorization models

├── requirements.txt    # Python dependencies

└── README.md           # Project documentation

```

---

## 🤝 Contributing & Team

Developed as project under VTU & Alva's Institute of Engineering and Technology.

|Name-------------------|Role--------------------------|Email----------------------|Contact--------|

|-----------------------|------------------------------|---------------------------|---------------|

|Anooj Raj--------------|---------HIDDEN---------------|anoojraj07@gmail.com-------|----HIDDEN-----|

|Ashik H. R.------------|---------HIDDEN---------------|hra72020@gmail.com---------|----HIDDEN-----|

|Chetan M. Wali---------|---------HIDDEN---------------|chetanwali2001@gmail.com---|----HIDDEN-----|

|Chinmaya Bhat K. K.----|---------HIDDEN---------------|cs24s501@iittp.com---------|+91-98958-07455|

|Dr. Vasudev S. Shahapur|Guide & Advisor---------------|vasu.shahapur@aiet.org.in--|+91-94495-86008|

---

## 📞 Contact

For questions or contributions:

- Open a [GitHub Issue](https://github.com/cbkk1/MONOCHROMATIC-TO-RGB/issues)

- Email: cs24s501@iittp.com

- Contact any team member directly

---
```
*Thank you for using MONOCHROMATIC-TO-RGB! 🎨✨*

```

