import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import datetime

def mail_creation():

    today = datetime.date.today()

    mail_content = '''With regards,
    Mr. Shivappa.B
    Library Assistant
    Dayananda Sagar University
    Hosur Main Road, Kudlu Gate
    Hongasandra Village, Begur Hobli,
    Bangalore, Karnataka-560068
    '''

    # the mail addresses and password
    sender_address = "XXX"
    sender_pass = "XXX"
    receiver_address = "XXXX"


    # Setup the MIME
    message = MIMEMultipart()
    message["From"] = sender_address
    message["To"] = receiver_address
    message["Subject"] = "Automated email service for Digital Library."


    # The subject line
    # he body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = "Excel_files\\" + today.strftime("%d.%m.%Y") + ".xlsx"
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase("application", "octate-stream")
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment


    # add payload header with filename
    payload.add_header("Content-Disposition", "attachment", filename = attach_file_name)
    message.attach(payload)


    # Create SMTP session for sending the mail
    session = smtplib.SMTP("smtp.gmail.com", 587) # use gmail with port
    session.starttls() # enable security
    session.login(sender_address, sender_pass) # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("Mail Sent")