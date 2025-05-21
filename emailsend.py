import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_email, sender_password)
        text = message.as_string()
        session.sendmail(sender_email, recipient_email, text)
        session.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

send_email(
    sender_email='shieldcyber59@gmail.com',
    sender_password='rvkj tlmv pzid koio',
    recipient_email='recipient@example.com',
    subject='Instagram Password Reset – Suspicious Activity Detected',
    body='''
Hi,

We’ve detected suspicious activity on your Instagram account. As a security measure, we’ve temporarily locked your account and recommend that you reset your password immediately.

Please click the link below to reset your password:


Thank you,
Instagram Security Team
'''
)
