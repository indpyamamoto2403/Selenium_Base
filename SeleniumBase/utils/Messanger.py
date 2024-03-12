from tkinter import messagebox as msbox

class Messanger:
    @staticmethod
    def ShowError(title, message):
        msbox.showerror(title, message)
    
    @staticmethod
    def ShowInfo(title, message):
        msbox.showinfo(title, message)
    
    @staticmethod
    def ShowWarning(title, message):
        msbox.showwarning(title, message)
    
    @staticmethod
    def ShowFailed():
        msbox.showerror("Error", "シナリオの実行に失敗しました。エラーログをご確認ください。")


Messanger.ShowFailed()