from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException
import time, datetime
import os, csv

class customDriver:
    '''
    ドライバークラスの詳細な実装をラップしたもの。
    
    クラス変数:
    標準待機時間(10秒)
    
    インスタンス変数:
    WebDriver(headlessモードやダウンロード先の指定などはコンストラクタ内で行う。)
    WebDriverWait(待機時間を制御するオブジェクト)
    '''
    wait_time = 10
    def __init__(self, 
                 download_dir = None):


        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--log-level=3')
        if download_dir != None:
            options.add_experimental_option('prefs', {'download.default_directory': download_dir})
            self.download_dir = download_dir
        self.driver = webdriver.Edge(options = options)
        self.wait = WebDriverWait(self.driver,self.wait_time)

            
    def open(self,URL:str):
        '''
        引数:URL
        '''
        self.driver.get(URL)        

    def input(self, 
              By:By, 
              element:str, 
              text:str,
              submit:bool=False):
        '''
        引数,
        By: Byオブジェクト。ID or Class, Name, XPath, CSSセレクターなどを指定する。
        element: elementの識別文字。Id名やclass名など
        text: テキストボックスやテキストエリアに入力する文字。
        '''            
        box = self.wait.until(EC.presence_of_element_located((By, element)))
        box.send_keys(text)
        if submit == True:
            box.submit()

    def click(self, 
              By:By, 
              element:str, 
              press_ctrl:bool=False):
        '''
        対象の要素をクリックする関数。
        引数,
        By: Byオブジェクト。ID or Class, Name, XPath, CSSセレクターなどを指定する。
        element: 要素の識別文字。Id名やclass名など
        press_ctrl: コントロールキーを押しながらのクリックができる。デフォルトはFalse
        '''    
        obj = self.wait.until(EC.presence_of_element_located((By, element)))
        if press_ctrl == True:
            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL)
            actions.click(obj)
            actions.perform()
        else:
            obj.click()
    

    def exists(self,
               By:By,
               element:str)->bool:
        '''
        要素があるかどうかを,bool値で返すメソッド
        By: Byオブジェクト。ID or Class, Name, XPath, CSSセレクターなどを指定する。
        element: プルダウンのelementの識別文字。Id名やclass名など
        text: テキストボックスやテキストエリアに選択する文字
        '''
        try:
            obj = self.wait.until(EC.presence_of_element_located((By, element)))
            return True
        except:
            return False



    def select(self,
               By:By,
               element:str,
               value:str):
        '''
        By: Byオブジェクト。ID or Class, Name, XPath, CSSセレクターなどを指定する。
        element: プルダウンのelementの識別文字。Id名やclass名など
        text: テキストボックスやテキストエリアに選択する文字
        '''
        pulldown = self.wait.until(EC.presence_of_element_located((By, element)))
        select = Select(pulldown)
        select.select_by_value(value)


    def select_by_index(self,
                By:By,
                element:str,
                index:int):
        '''
        By: Byオブジェクト。ID or Class, Name, XPath, CSSセレクターなどを指定する。
        element: プルダウンのelementの識別文字。Id名やclass名など
        text: テキストボックスやテキストエリアに選択する文字
        '''
        pulldown = self.wait.until(EC.presence_of_element_located((By, element)))
        select = Select(pulldown)
        select.select_by_index(index)
    
    def select_by_text(self,
                By:By,
                element:str,
                text:str):
        '''
        By: Byオブジェクト。ID or Class, Name, XPath, CSSセレクターなどを指定する。
        element: プルダウンのelementの識別文字。Id名やclass名など
        text: テキストボックスやテキストエリアに選択する文字
        '''
        if text == None:
            return
        pulldown = self.wait.until(EC.presence_of_element_located((By, element)))
        select = Select(pulldown)
        select.select_by_visible_text(text)

    def accept_alert(self)->None:
        '''
        アラートをAcceptする。現れるまで最大10秒待機する。
        '''
        try:
            time.sleep(5)
            alert = self.wait.until(EC.alert_is_present())
            self.driver.switch_to.alert
            alert.accept()
            time.sleep(1)
        except TimeoutException as e:
            print(e)
            
    
    def cancel_alert(self)->None:
        '''
        アラートをCancelする。現れるまで最大10秒待機する。
        '''
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(1)
        except TimeoutException as e:
            print(e)

    def alert_exists(self)->bool:
        '''
        alertが存在するかどうかの確認。標準待機時間ほど待機し、見つかったかどうかをbool値で返す。
        '''
        try:
            alert = self.wait.until(EC.alert_is_present())
            return True
        except:
            return False

    def switch_window(self, mode:str="next"):
        '''
        アクティブなウインドウを切り替える。
        引数:
        mode:デフォルトで"next"（次に切り替える)。
        オプションで"prev", "first"などに切り替え可能。
        '''
        current_window_handle = self.driver.current_window_handle
        all_window_handles = self.driver.window_handles
        if mode == "next":
            # 次のウィンドウに切り替える
            next_index = (all_window_handles.index(current_window_handle) + 1) % len(all_window_handles)
            new_window_handle = all_window_handles[next_index]
            self.driver.switch_to.window(new_window_handle)

        elif mode == "prev":
            # 前のウィンドウに切り替える
            prev_index = (all_window_handles.index(current_window_handle) - 1) % len(all_window_handles)
            new_window_handle = all_window_handles[prev_index]
            self.driver.switch_to.window(new_window_handle)

        elif mode == "first":
            # 最初のウィンドウに切り替える
            first_window_handle = all_window_handles[0]
            self.driver.switch_to.window(first_window_handle)

            # 最初のウィンドウ以外を閉じる
            for handle in all_window_handles[1:]:
                self.driver.switch_to.window(handle)
                self.driver.close()
            # 最初のウィンドウにフォーカスを戻す
            self.driver.switch_to.window(first_window_handle)
    
    def resize_window(self, mode:str):
        '''
        ブラウザのサイズを最小化したり最大化したりする。
        引数:mode "max":最大化, "min":最小化 
        '''
        if mode == "max":
            self.driver.maximize_window()
        elif mode == "min":
            self.driver.minimize_window()
        else:
            raise ValueError("Invalid mode. Use 'max' or 'min'.")

    def run_script(self, script: str):
        '''
        ページ内のJvascriptを直接実行する。
        
        '''
        self.driver.execute_script(script)
    
    def scroll_to_element(self, By:By, element:str):
        '''
        要素を自動でスクロールを行う。
        引数:
        By: Byオブジェクト。Elementの種類
        element: 要素の識別文字。
        '''
        obj = self.wait.until(EC.presence_of_element_located((By, element)))
        actions = ActionChains(self.driver)
        actions.move_to_element(obj).perform()
    
    def hover(self, By: By, element: str):
        '''
        ある要素に対してホバーを行う。
        引数:
        By: Byオブジェクト。Elementの種類
        element: 要素の識別文字。
        '''
        obj = self.wait.until(EC.presence_of_element_located((By, element)))
        actions = ActionChains(self.driver)
        actions.move_to_element(obj).perform()
    
    def wait_until_clickable(self, By: By, element: str):
        '''
        ある要素がクリックできるまで待機を行う。
        引数:
        By: Byオブジェクト。Elementの種類
        element: 要素の識別文字。
        '''
        self.wait.until(EC.element_to_be_clickable((By, element)))

    def upload(self, By: By, element: str, file_path: str):
        '''
        ある要素に対してファイルのアップロードを行う。
        引数:
        By: Byオブジェクト。Elementの種類
        element: 要素の識別文字。
        filepath: ファイルのパス。        
        '''
        obj = self.wait.until(EC.presence_of_element_located((By, element)))
        #obj = self.driver.find_element(By, element)
        obj.send_keys(file_path)

    def scroll_down(self):
        '''
        単にbodyタグの高さの座標まで、つまり一番下まで
        スクロールする関数。
        '''
        self.run_script('window.scrollTo(0, document.body.scrollHeight);')

    def snap(self, folder:str, file_name:str, name_as_timestamp=False):
        '''
        スクリーンショットを撮影する。
        folder:フォルダ名(str)
        file_name:ファイル名(str)
        name_as_timestamp:ファイル名にタイムスタンプを含めるかどうか。
        Trueにした場合、ファイル名に本日の日付をスタンプしたpngファイルが得られる。
        '''
        
        #本日のタイムスタンプを押せるかどうかをオプションで選べる。
        if name_as_timestamp == True:
            _now = datetime.datetime.now()
            _today_with_time = _now.strftime("%Y_%m_%d-%H_%M_%S")
            file_name = file_name + _today_with_time

        directory = os.path.join(folder, file_name + ".png")
        self.driver.save_screenshot(directory)

    def getHTML(self):
        return self.driver.page_source

    def upload_file(self, element: str, file_path: str):
        '''
        ファイルをアップロードする。
        ボタンの要素を取得し、ファイルのフルパスを送信する。
        '''
        obj = self.wait.until(EC.presence_of_element_located((By, element)))
        obj.send_keys(file_path)
    
    def hard_click(self, By: By, element: str):
        '''
        ある要素に対してhardなclickを行う。
        要素の座標に直接ジャンプし、ハードにクリックを行う。
        引数:
        By: Byオブジェクト。Elementの種類
        element: 要素の識別文字。
        '''
        obj = self.wait.until(EC.presence_of_element_located((By, element)))
        actions = ActionChains(self.driver)
        actions.move_to_element(obj).click(obj).perform()



    def close(self):
        '''
        driverを閉じる
        '''
        handle_array = self.driver.window_handles
        current_num = len(handle_array) - 1
        self.driver.close()
        self.driver.switch_to.window(handle_array[current_num-1])

    def close_except_first_window(self):
        '''
        最初のウインドウ以外を閉じていく
        '''
        while True:
            if len(self.driver.window_handles) == 1:
                return
            else:
                self.close()
                time.sleep(1)
            
    def clear(self, By, element):
        box = self.wait.until(EC.presence_of_element_located((By, element)))
        box.clear()

    def destroy(self):
        '''
        使い終わったドライバーは破棄しましょう :D 
        '''
        self.driver.quit()
