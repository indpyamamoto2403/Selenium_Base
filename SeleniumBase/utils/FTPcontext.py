from ftplib import FTP
from logging import Logger
from typing import Optional, List

class FTPProcessor:

    '''
    ## FTPに接続し、アップロードやダウンロードなど種々の処理を行うクラス。
    ### 使用例
    ftp_processor = FTPProcessor(ftp_host=FTP_HOST, ftp_port=FTP_PORT, ftp_user=FTP_USER, ftp_password=FTP_PASSWORD)
    ftp_processor.connect()

    ### FTP処理を実行

    ftp_processor.disconnect()
    '''

    def __init__(self, ftp_host: str, ftp_port: int = 21, ftp_user: Optional[str] = None, ftp_password: Optional[str] = None, logger: Optional[Logger] = None) -> None:
        self.ftp_host = ftp_host
        self.ftp_port = ftp_port
        self.ftp_user = ftp_user
        self.ftp_password = ftp_password
        self.ftp: Optional[FTP] = None  # FTPオブジェクトの初期化
        
        # ロガー設定
        self.logger = logger

        self.connect()

    def connect(self) -> None:
        try:
            self.ftp = FTP()
            self.ftp.connect(self.ftp_host, self.ftp_port, timeout=10)
            self.ftp.login(self.ftp_user, self.ftp_password)
            print(f"Connected to {self.ftp_host}:{self.ftp_port}")
        except Exception as e:
            print(f"Error connecting to FTP server: {e}")
            
    def set_logger(self, logger: Logger) -> None:
        self.logger = logger
    
    def get_list(self) -> List[str]:
        '''
        リストを表示させる方法。戻り値はlist[str]
        '''
        files: List[str] = []
        self.ftp.retrlines('LIST', files.append)
        return files

    def show_list(self) -> None:
        if self.logger:
            files = self.get_list()
            for file in files:
                self.logger.debug(file)

    def download(self) -> None:
        pass
    
    def upload(self, file_path: str, remote_path: str) -> None:
        '''
        ファイルをアップロードするメソッド
        file_path: ローカルのファイルパス
        remote_path: アップロード先のリモートのファイルパス
        '''
        try:
            with open(file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {remote_path}', file)
                print(f"Uploaded {file_path} to {remote_path}")
                if self.logger:
                    self.logger.info(f"Uploaded {file_path} to {remote_path}")
        except Exception as e:
            print(f"Error uploading file: {e}")
            if self.logger:
                self.logger.error(f"Error uploading file: {e}")
    
    def disconnect(self) -> None:
        if self.ftp:
            self.ftp.quit()
            print("Disconnected from FTP server")

    # その他のFTP処理メソッドを追加することができます
