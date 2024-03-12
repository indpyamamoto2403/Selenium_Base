import sys
import datetime
import traceback
    
def error_logging(e, exe_print = False):
    error_type = type(e).__name__  # エラータイプを取得
    error_message = str(e)  # エラーメッセージを取得
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # タイムスタンプを取得
    error_traceback = traceback.format_exc()  # エラーのトレースバック情報を取得

    # エラーデータを logging_error.py に渡す
    #subprocess.run(["python", "error\\logging_error.py", error_type, error_message, timestamp, error_traceback])
    with open('error//execution_history.log', 'a') as log_file:
        log_file.write("-------------------------------------------------\n")
        log_file.write(f"Timestamp: {timestamp}\n")
        log_file.write(f"Error Type: {error_type}\n")
        log_file.write(f"Error Message: {error_message}\n")
        log_file.write(f"Error Traceback:\n{error_traceback}\n")
        log_file.write("-------------------------------------------------\n")
    if exe_print:
        print("-------------------------------------------------\n")
        print(f"Timestamp: {timestamp}\n")
        print(f"Error Type: {error_type}\n")
        print(f"Error Message: {error_message}\n")
        print(f"Error Traceback:\n{error_traceback}\n")
        print("-------------------------------------------------\n")
          