import smtplib

#add username / password / reciever email variables
username = input("Enter username: ")  #uwo4436
password = input("Enter password: ")  #eceuwo2017
reciever = input("Enter the email address you wish to send the email to: ")

sent_from = username
to = [reciever]
subject = 'My message using smtplib'
body = 'Hey, whats up?\n\n- Aaryn/Nikita'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

#use smtplib to send the email
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(username, password)
    server.sendmail(username, to, email_text)
    server.close()

    print ('Email sent!')
except Exception as e:
    print ('Something went wrong...', e)
