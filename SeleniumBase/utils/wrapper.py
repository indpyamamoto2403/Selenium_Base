from time import sleep

def retry(max_retries, interval):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            cnt = 1
            while True:
                try:
                    print("前処理")
                    func(*args, **kwargs)
                    print("後処理")
                    1/0
                    break
                except Exception as e:
                    print(f"{cnt}回目の処理、失敗しました。")
                    cnt += 1
                    sleep(interval)
                    if cnt > max_retries:
                        raise Exception("hahaha")
        return wrapper
    return decorator



#使用例
@retry(max_retries = 5, interval=5)
def my_function():
    print("関数の本処理")
try:
    my_function()
except Exception as e:
    print("最大リトライ数を超過しました。")


@retry(max_retries=3, interval=1)
def test_function():
    print("テスト関数が呼び出されました。")
    raise ValueError("テスト用のエラーです。")

if __name__ == "__main__":
    try:
        test_function()
    except Exception as e:
        print("テストが最大回数を超えて失敗しました:", e)
