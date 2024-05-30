import email
import imaplib

class EmailClient:
    def _init_(self, email, password, server):
        self.email = email
        self.password = password
        self.server = server
        self.mail = imaplib.IMAP4_SSL(self.server)

    def login(self):
        self.mail.login(self.email, self.password)

    def select_mailbox(self, mailbox):
        self.mail.select(mailbox)

    def search_emails(self, criterion='ALL'):
        status, data = self.mail.search(None, criterion)
        if status != 'OK':
            raise Exception("Failed to search emails.")
        return data

    def fetch_email(self, email_id):
        status, data = self.mail.fetch(email_id, '(RFC822)')
        if status != 'OK':
            raise Exception(f"Failed to fetch email with ID {email_id}.")
        return data

    def process_emails(self, email_ids, specific_person):
        for email_id in email_ids:
            data = self.fetch_email(email_id)
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    mail_from = message['from']
                    mail_subject = message['subject']
                    mail_content = self.get_mail_content(message)

                    if specific_person in mail_from:
                        print(f'From: {mail_from}')
                        print(f'Subject: {mail_subject}')
                        print(f'Content: {mail_content}')

    def get_mail_content(self, message):
        if message.is_multipart():
            mail_content = ''
            for part in message.get_payload():
                if part.get_content_type() == 'text/plain':
                    mail_content += part.get_payload()
            return mail_content
        else:
            return message.get_payload()

if __name__ == "_main_":
    EMAIL = 'kaique.trabalho010@gmail.com'
    PASSWORD = 't s c s g g n s j h d w d a bu'
    SERVER = 'imap.gmail.com'
    SPECIFIC_PERSON = ''

    client = EmailClient(EMAIL, PASSWORD, SERVER)
    client.login()
    client.select_mailbox('inbox')  # ou '[Gmail]/Starred' para favoritos
    data = client.search_emails()
    
    mail_ids = []
    for block in data:
        mail_ids += block.split()
    
    client.process_emails(mail_ids, SPECIFIC_PERSON)