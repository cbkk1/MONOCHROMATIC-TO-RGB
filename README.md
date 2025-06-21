```markdown

# MONOCHROMATIC-TO-RGB

> A Flask-based B.Tech project that converts monochrome images to full RGB color.

![Project Banner](https://via.placeholder.com/800x200?text=Monochromatic+to+RGB+Colorization) <!-- Replace with your actual banner image URL -->

## 📋 Table of Contents

1. [Project Overview](#-project-overview)

2. [Demo](#-demo)

3. [Installation](#%EF%B8%8F-installation)

4. [Usage](#%EF%B8%8F-usage)

5. [Requirements](#-requirements)

6. [Project Structure](#-project-structure)

7. [Contributing & Team](#-contributing--team)

8. [Contact](#-contact)

---

## 🚀 Project Overview

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

Developed as final-year B.Tech project under VTU & Alva's Institute of Engineering and Technology.

| Name               | Role                          | Email                      | Contact        |

|--------------------|-------------------------------|----------------------------|----------------|

| Anooj Raj          | Lead Developer                | anoojraj07@gmail.com       | +91-81518-25515 |

| Ashik H. R.        | Backend & Model Integration   | hra72020@gmail.com         | +91-97311-793195 |

| Chetan M. Wali     | Frontend & UI Design          | chetanwali2001@gmail.com   | +91-63638-85750 |

| Chinmaya Bhat K. K.| Project Coordinator           | chinmayabhatkk@gmail.com   | +91-98958-07455 |

| Dr. Vasudev S. Shahapur | Guide & Advisor          | vasu.shahapur@aiet.org.in  | +91-94495-86008 |

---

## 📞 Contact

For questions or contributions:

- Open a [GitHub Issue](https://github.com/cbkk1/MONOCHROMATIC-TO-RGB/issues)

- Email project coordinator: chinmayabhatkk@gmail.com

- Contact any team member directly

---

*Thank you for using MONOCHROMATIC-TO-RGB! 🎨✨*

```

