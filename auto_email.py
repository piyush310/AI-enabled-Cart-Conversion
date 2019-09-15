import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def Email(name,email,passw,checkout):
    names = []
    names.append(name)
    emails = []
    emails.append(email)
    if(checkout):
        message_template = read_template('message_checkout.txt')
    else:
        message_template = read_template('message.txt')
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('b416016@iiit-bh.ac.in', passw) ### Password Here

    for name, email in zip(names, emails):
        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=name.title())
        msg['From']="b416016@iiit-bh.ac.in"
        msg['To']=email
        if(checkout):
            msg['Subject']="Dell - Please Complete the payment"
        else:
            msg['Subject']="Dell - Please Proceed to checkout"
        
        msg.attach(MIMEText(message, 'plain'))
        fp = open('dell.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        # msgImage.add_header('Content-ID', '<image1>')
        # msg.attach(msgImage)
        # fp = open('Capture1.png', 'rb')
        # msgImage = MIMEImage(fp.read())
        # fp.close()
        msgImage.add_header('Content-ID', '<image2>')
        msg.attach(msgImage)
        fp = open('Capture2.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<image3>')
        msg.attach(msgImage)
        s.send_message(msg)
        del msg
    s.quit()
# Email("Anirudh", "b416056@iiit-bh.ac.in", True)