from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_email(sender_email, sender_password, recipient_email):
    """
    Sends a email from a microsoft email addresses

    Args:
        sender_email (str) : sender email address
        sender_password (str) : sender email password
        recipient_email (str) : recipient email
    
    """
    # Establish secure connection to an SMTP (Simple Mail Transfer Protocol)
    # The first argument is the IP address of the SMTP server
    # 587 is the port number for incoming emails
    server = smtplib.SMTP('smtp.office365.com', 587)
    # Tells the microsoft server that you want to upgrade
    # the connection to a secure TLS connection - needed for encryption
    server.starttls()

    try:
        # Login to Microsoft SMTP server
        server.login(sender_email, sender_password)

        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'Daily Email'

        # Adds content to email
        msg.attach(MIMEText("TEST EMAIL\n", 'plain', 'utf-8'))

        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())

    except Exception as exception:
        print(f"An error occurred: {exception}")

    finally:
        # Close SMTP connection
        server.quit()

# Email details[CAREFUL!]
SENDER_EMAIL = ''
SENDER_PASSWORD = ''
RECIPIENT_EMAIL = ''

send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
