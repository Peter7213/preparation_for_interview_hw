import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailBox:

    def __init__(self, email_sender, password):
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"
        self.sender = email_sender
        self.password = password
        self.recipients = ['vasya@email.com', 'petya@email.com']
        self.header = None

    # send message
    def send_message(self, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.sender, self.password)
        ms.sendmail(self.sender, ms, msg.as_string())

        ms.quit()
        # send end

    # receive
    def receive_message(self):

        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.sender, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        # end receive

if __name__ == '__main__':
    mail_box = EmailBox('login@gmail.com', 'qwerty')
    mail_box.send_message('Subject', 'Message')
    mail_box.receive_message()