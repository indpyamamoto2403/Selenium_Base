import os, time

class FileManager:
    
    def __init__(self):
        pass
    
    def delete_folder_contents(self, folder_path):
        '''
        フォルダ内のファイルをすべて削除する。
        '''
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
    
    def wait_until_file_downloaded(self, folder_path:str, keyword:str="crdownload", span=0.3, max_retry=100):
        '''
        ファイルがダウンロードされるまで待機する
        folder_path:フォルダのパス
        keyword:対象のファイル。普通ダウンロードしてきたものは{crdownload}とされているので、
        デフォルトではcrdownloadのキーワードを設定している。
        span:リトライの頻度(秒)。デフォルトでは0.5にしている。
        max_retry: リトライの回数。デフォルトでは60回にしている。

        デフォルトでは0.5 x 60 = 30秒間、リトライを試みてだめならErrorを投げる。
        '''
        files = []
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            if keyword in file_name:
                files.append(os.path.join(folder_path, file_name))
        target = files[0]
        
        retry=0
        while True:
            try:
                with open(target,'rb'):
                    print("arere")
                print("arere")
                break
            except:
                time.sleep(span)
                retry += 1
                print(f"retry:{retry}")
                if retry > max_retry:
                    raise Exception("File Didn't open")

    def rename_downloadfile(self, folder_path:str, new_file:str,span:float=3, max_retry:int=50, keyword:str="crdownload"):
        '''
        同じ階層でリネームを行う。

        folderpath: 絶対パスを指定する。
        '''
        cnt = 0
        while True:
            if cnt > max_retry:
                raise Exception("rename error. max retries exceed but rename couldn't process.")
            else:
                try:
                    files = os.listdir(folder_path)
                    crdownloads = []
                    for file in files:
                        if keyword in file:
                            crdownloads.append(os.path.join(folder_path, file))
                    old_file_path = crdownloads[0]
                    new_file_path = os.path.join(folder_path, new_file)
                    if os.path.isfile(new_file_path):
                        os.remove(new_file_path)
                        print(f"{new_file_path}がすでに存在していたので、削除しました。")
                    os.rename(old_file_path, new_file_path)
                    break

                except Exception as e:
                    print(f"num_error perhaps while downloading. take is easy while waiting:D ,{cnt}")
                    print(e)
                    time.sleep(span)
                    cnt += 1
    def file_exists(self, folder_path, keyword):
        '''
        return bool value
        '''
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            if keyword in file_name:
                return True
        return False
    
    


    



