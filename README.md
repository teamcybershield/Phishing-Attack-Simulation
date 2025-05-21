# Phishing-Attack-Simulation
# Email Sending
# Imports the necessary Python libraries to handle SMTP communication and construct email content using MIME format.
# Defines the send_email() function, which accepts sender credentials, recipient email, subject, and message body as parameters.
# Constructs a MIME multipart email message, including standard headers such as From, To, and Subject.
# Attaches the message body as plain text to ensure compatibility across email clients.
# Establishes a connection to Gmail’s SMTP server (smtp.gmail.com) using port 587.
# Initiates a secure TLS session to encrypt the communication channel.
# Authenticates the sender using the provided email address and password.
# Sends the formatted email to the specified recipient.
# Gracefully terminates the SMTP session once the email is sent.
# Implements error handling to capture and report any exceptions that may occur during the email sending process.
# Executes the send_email() function with predefined parameters to deliver a security-related password reset notification concerning suspicious activity on an Instagram account.

