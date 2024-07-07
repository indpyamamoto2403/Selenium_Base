import logging
import traceback

class LoggerBase:
    def __init__(self, name:str):
        self.logger = logging.getLogger(name)
        self.error_logger = logging.getLogger("error")
        self.logger.setLevel(logging.DEBUG)
        self.error_logger.setLevel(logging.ERROR)
        self.destination = 'log//history.csv'
        self.error_distination = 'log//error.log'
        self.datafmt = '%Y-%m-%d,%H:%M:%S'  # YYYY-MM-DD hh:mm:ss形式
        self.logfmt = '%(asctime)s,%(levelname)s,%(message)s'
        self.setup_handlers()

    def setup_handlers(self):
        # ファイルハンドラを作成し、ファイルにログを書き込む
        file_handler = logging.FileHandler(self.destination)
        file_handler.setLevel(logging.DEBUG)

        # コンソールハンドラを作成し、コンソールにログを表示
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        #エラーハンドラを作成し、ファイルにログを書き込む
        error_handler = logging.FileHandler(self.error_distination)
        error_handler.setLevel(logging.ERROR)
        
        # ログのフォーマットを設定
        log_format = self.logfmt
        formatter = logging.Formatter(log_format, datefmt=self.datafmt)

        # ハンドラにフォーマッタを設定
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)

        # ロガーにハンドラを追加
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        self.error_logger.addHandler(error_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message, exc_info=True):
        self.logger.error(message)
        self.logger.error(traceback.format_exc())
        self.error_logger.error(message, exc_info=exc_info)

    def critical(self, message, exc_info=True):
        self.logger.critical(message)
        self.logger.error(traceback.format_exc())
        self.error_logger.critical(message, exc_info=exc_info)

class StandardLogger(LoggerBase):
    def __init__(self):
        super().__init__('my_logger')

# 使用例
if __name__ == "__main__":
    try:
        logger = StandardLogger()
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warn("Warning message")
        1/0
    except Exception as e:
        print("ここから下エラーメッセージ")
        logger.debug("Debug message") 
        logger.error("Error message")
        logger.critical("Critical message")
