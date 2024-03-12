

class LoginException(Exception):
    def __init__(self, username, message="ログインに失敗しました。"):
        self.username = username
        super().__init__(message)

class LogoutException(Exception):
    def __init__(self, message="ログアウトに失敗しました。"):
        super().__init__(message)

class FileDownloadException(Exception):
    def __init__(self, message="ファイルのダウンロードに失敗しました。"):
        super().__init__(message)

class FileUploadException(Exception):
    def __init__(self, filename, message="ファイルのアップロードに失敗しました。"):
        self.filename = filename
        super().__init__(message)

class MailSendException(Exception):
    def __init__(self, message="メールの送信に失敗しました。"):
        super().__init__(message)

# 使用例
# if __name__ == "__main__":
#     try:
#         raise LoginException()
#     except LoginException as e:
#         print(f"例外を捕捉しました: {e}")

#     try:
#         raise LogoutException("ログアウトに失敗しました。")
#     except LogoutException as e:
#         print(f"例外を捕捉しました: {e}")

#     try:
#         raise FileDownloadException()
#     except FileDownloadException as e:
#         print(f"例外を捕捉しました: {e}")

#     try:
#         raise FileUploadException("ファイルのアップロードに失敗しました。")
#     except FileUploadException as e:
#         print(f"例外を捕捉しました: {e}")

#     try:
#         raise MailSendException()
#     except MailSendException as e:
#         print(f"例外を捕捉しました: {e}")



# if __name__ == "__main__":
#     try:
#         raise LoginException("john_doe")
#     except LoginException as e:
#         print(f"ユーザー名 {e.username} でログインエラーが発生しました: {e}")

#     try:
#         raise FileUploadException("example.txt")
#     except FileUploadException as e:
#         print(f"ファイル {e.filename} のアップロードエラーが発生しました: {e}")