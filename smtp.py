import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Email configuration
sender_email = 'prajapatiawanish'
receiver_email = 'awanishprajapati96@gmail.com'
subject = 'Test Email'
message_body = 'This is a test email sent from Python.'

# Create a MIMEText object for the email content
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message body
msg.attach(MIMEText(message_body, 'plain'))

# Connect to the SMTP server (Gmail in this case)
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # 587 is the default port for secure TLS connections
smtp_username = 'awanishkr@gmail.com.com'
smtp_password = 'Gpt@#123'

# Create an SMTP connection and login
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Send the email
server.sendmail(sender_email, receiver_email, msg.as_string())

# Disconnect from the server
server.quit()

print('Email sent successfully!')