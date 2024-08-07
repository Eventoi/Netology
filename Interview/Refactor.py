import email
import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail:
    def __init__(self, smtp_server, imap_server, login, password):
        self.smtp_server = smtp_server
        self.imap_server = imap_server
        self.login = login
        self.password = password

    def send_mail(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.smtp_server, 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.login, self.password)
            smtp.sendmail(self.login, recipients, msg.as_string())

    def receive_mail(self, header=None):
        with imaplib.IMAP4_SSL(self.imap_server) as imap:
            imap.login(self.login, self.password)
            imap.select("inbox")
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = imap.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = imap.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)
        return email_message

if __name__ == '__main__':
    mail = Mail(smtp_server=GMAIL_SMTP, imap_server=GMAIL_IMAP, login=l, password=passwORD)
    mail.send_mail(recipients=recipients, subject=subject, message=message)
    email_message = mail.receive_mail(header=header)