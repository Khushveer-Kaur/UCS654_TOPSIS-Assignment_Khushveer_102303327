from flask import Flask, render_template, request
import os
import re
from topsis_logic import run_topsis
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Folder to store uploaded files and results
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form inputs
        file = request.files.get("file")
        weights = request.form.get("weights")
        impacts = request.form.get("impacts")
        email = request.form.get("email")

        # Basic validations
        if not file or file.filename == "":
            return "No file uploaded"

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Invalid email format"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(UPLOAD_FOLDER, "result.csv")

        # Save uploaded CSV
        file.save(input_path)

        try:
            # Run TOPSIS logic
            run_topsis(input_path, weights, impacts, output_path)

            # Send email with result
            send_email(email, output_path)

            return "Result sent to your email successfully!"

        except Exception as e:
            return f" Error: {str(e)}"

    return render_template("index.html")


def send_email(receiver, attachment_path):
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")

    if not sender_email or not sender_password:
        raise Exception("Email credentials not set in environment variables")

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender_email
    msg["To"] = receiver
    msg.set_content("Please find attached TOPSIS result.")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)



if __name__ == "__main__":
    app.run(debug=True)



