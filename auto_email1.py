import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def Email(name,email,passw):
    names = []
    names.append(name)
    emails = []
    emails.append(email)
    message_template = read_template('message.txt')

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('b416016@iiit-bh.ac.in', passw) ### Password Here

    for name, email in zip(names, emails):
        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=name.title())
        msg['From']='anirudhmaurya37@gmail.com'
        msg['To']=email
        msg['Subject']="This is TEST"
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
    s.quit()
