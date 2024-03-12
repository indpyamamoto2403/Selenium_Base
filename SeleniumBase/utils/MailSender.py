import smtplib
from email.mime.text import MIMEText

class MailSender:

    def __init__(self, from_addr: str, to_addr: list[str], subject: str, message: str, password:str):
        '''
        このときはインスタンスにプロパティをあてはめるだけ。
        '''
        self.from_addr: str = from_addr
        self.to_addr: list[str] = to_addr
        self.subject: str = subject
        self.message: str = message
        self.password:str = password

        

    def create_object(self) -> None:
        """ObjectをCreateする。"""

        self.msg: MIMEText = MIMEText(self.message, 'plain')
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.from_addr
        self.msg['To'] = ','.join(self.to_addr)

    def login(self, host, port) ->None:
        '''
        メールサーバーにログイン。
        '''
        self.server: smtplib.SMTP = smtplib(host, port)
        self.server.starttls()
        self.server.login(self.from_addr, self.password)

    def send(self) ->None:
        '''
        メールの送信を行う。
        '''
        # メールを送信
        self.server.send_message(self.msg)
    
    def dispose(self)->None:
        '''
        メールインスタンスの破棄を担う。
        '''
        self.server.quit()
