import smtplib
import os.path
from Crypto.Cipher import ARC4
import smtplib


def send_mail(userEmail, userPassword, to, subject, message):
    import smtplib

    to = to if type(to) is list else [to]

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (email, ", ".join(to), subject, message)

    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(userEmail, userPassword)
        server.sendmail(userEmail, to, message)
        server.close()
        print 'E-mail successfully sent!'
    except:
        print "Couldn't send mail"


if os.path.isfile('creds.txt'):

    arc4_decrypt = ARC4.new('somekey')
    readfile = open('creds.txt', 'r')

    lineArray = readfile.readline().split(':')
    email = lineArray[0]
    encryptedPassword = lineArray[1]
    password = arc4_decrypt.decrypt(encryptedPassword)

    recipients = raw_input("Enter the e-mail you want to send to. If it is multiple e-mails, separate them by one space.\r\n\r\n").split(' ')

    subj = raw_input('Subject: ')

    print "\r\nStart typing your message. When you are finished, enter the word 'ENDMESSAGE' on a new line on its own.\r\n"

    content = []
    while True:
        line = raw_input("")
        if line == 'ENDMESSAGE':
            break
        content.append(line)

    content = '\r\n'.join(content)

    send_mail(email, password, recipients, subj, content)

else:

    arc4_encrypt = ARC4.new('somekey')
    email = raw_input('E-mail: ')
    password = raw_input('Password: ')

    encryptedPassword = arc4_encrypt.encrypt(password)

    with open('creds.txt', 'w') as f:

        f.write(email+":"+encryptedPassword)

        f.close()
