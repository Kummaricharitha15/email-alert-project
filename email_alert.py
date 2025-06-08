from transformers import pipeline
import smtplib
from email.mime.text import MIMEText

# Load AI model
classifier = pipeline("sentiment-analysis")

# Analyze input text
text = input("Enter a comment: ")
result = classifier(text)[0]
label = result["label"]
score = result["score"]

print(f"AI says: {label} (confidence: {score:.2f})")

# Only send email if highly negative
if label == "NEGATIVE" and score > 0.9:
    # Email content
    subject = "⚠ Negative Comment Alert"
    body = f"The following comment was flagged as negative:\n\n{text}\n\nScore: {score:.2f}"
    
    # Mailtrap SMTP info
    smtp_host = "smtp.mailtrap.io"
    smtp_port = 587
    username = "e197b6106f8d13"  # <-- replace
    password = "5ed8934fbdff17"  # <-- replace
    
    from_email = "alert@example.com"
    to_email = "you@example.com"

    # Send the email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.login(username, password)
        server.send_message(msg)
    
    print("✅ Email alert sent via Mailtrap!")
else:
    print("No alert needed.")