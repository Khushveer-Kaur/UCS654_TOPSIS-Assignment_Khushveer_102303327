# Part 3 – TOPSIS Web Service (Flask)

This part implements the TOPSIS algorithm as a web service using Flask.

## Features
- Upload CSV file containing alternatives and criteria
- Accepts weights and impacts from user
- Validates input format
- Computes TOPSIS score and rank
- Sends result CSV to user's email

## Tech Stack
- Python
- Flask
- HTML / CSS
- SMTP (Gmail)

## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```
### Open browser and visit

```
http://127.0.0.1:5000
```
