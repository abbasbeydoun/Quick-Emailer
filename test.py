import smtplib
import os.path
from Crypto.Cipher import ARC4


if os.path.isfile('creds.txt'):

    arc4_decrypt = ARC4.new('somekey')
    readfile = open('creds.txt', 'r')
    lineArray = readfile.readline().split(':')
    email = lineArray[0]
    encryptedPassword = lineArray[1]
    password = arc4_decrypt.decrypt(encryptedPassword)

    print 'Email is '+email+' and passsword is '+password

else:

    arc4_encrypt = ARC4.new('somekey')
    email = raw_input('E-mail: ')
    password = raw_input('Password: ')

    encryptedPassword = arc4_encrypt.encrypt(password)

    with open('creds.txt', 'w') as f:

        print 'Email is '+email
        print 'EncryptedPassword is '+encryptedPassword

        f.write(email+":"+encryptedPassword)

        f.close()
