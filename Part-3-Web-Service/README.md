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
- Render (Deployment)

## Deployed Web Service

The TOPSIS web service has been successfully deployed using Render.

### Live URL:  
<https://topsis-web-service-bq7q.onrender.com/>

> Note: Since this is deployed on Render free tier, the first request may take some time due to cold start.

## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```
### Open browser and visit

```
http://127.0.0.1:5000
```
