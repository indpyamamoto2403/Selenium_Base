from ftplib import FTP

class FTPProcessor:

    '''
    ## FTPに接続し、アップロードやダウンロードなど種々の処理を行うクラス。
    ### 使用例
    ftp_processor = FTPProcessor(ftp_host=FTP_HOST, ftp_port=FTP_PORT, ftp_user=FTP_USER, ftp_password=FTP_PASSWORD)
    ftp_processor.connect()

    ### FTP処理を実行

    ftp_processor.disconnect()
    '''

    def __init__(self, ftp_host, ftp_port=21, ftp_user=None, ftp_password=None):
        self.ftp_host = ftp_host
        self.ftp_port = ftp_port
        self.ftp_user = ftp_user
        self.ftp_password = ftp_password
        self.ftp = None  # FTPオブジェクトの初期化

        self.connect()

    def connect(self):
        try:
            self.ftp = FTP()
            self.ftp.connect(self.ftp_host, self.ftp_port, timeout=10)
            self.ftp.login(self.ftp_user, self.ftp_password)
            print(f"Connected to {self.ftp_host}:{self.ftp_port}")
        except Exception as e:
            print(f"Error connecting to FTP server: {e}")

    def show_list(self):
        '''
        リストを表示させる方法。戻り値はlist[str]
        '''
        
        return self.ftp.retrlines('LIST')


    def download(self):

        pass
    
    def upload(self):
        pass
    
    def disconnect(self):
        if self.ftp:
            self.ftp.quit()
            print("Disconnected from FTP server")

    # その他のFTP処理メソッドを追加することができます

