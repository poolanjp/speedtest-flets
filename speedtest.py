#!~/python_env/bin/python3

import csv
import datetime
import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tenacity import TryAgain, retry, stop_after_attempt, wait_fixed


@retry(reraise=True,
       stop=stop_after_attempt(3),
       wait=wait_fixed(5))
def execute(driver: any, result: dict) -> bool:
    # 要素が見つかるまで、最大10秒間待機する（暗黙的な待機）
    driver.implicitly_wait(10)

    # サイトに接続する
    driver.get(URL)

    # 都道府県の一覧を選ぶ
    locator_pref_menu = (
        By.XPATH, "/html/body/main/div[1]/section[1]/div[1]/button")
    # 要素が表示されるまで最大15秒待つ
    element_pref_menu = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(locator_pref_menu))
    # クリックする
    element_pref_menu.click()

    # 都道府県を選択する（東京都）
    locator_pref = (
        By.XPATH, "/html/body/main/div[1]/section[1]/div[2]/div/div/div[2]/table[2]/tbody/tr[3]/td[2]/label")
    # 要素が表示されるまで最大5秒待つ
    element_pref = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_pref))
    # クリックする
    element_pref.click()

    # 契約サービスを選択する（NTT東日本）
    locator_srv = (
        By.XPATH, "/html/body/main/div[1]/section[2]/div/div/label[1]")
    # 要素が表示されるまで最大5秒待つ
    element_srv = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_srv))
    # クリックする
    element_srv.click()

    # サービスメニューを選択する
    locator_srvmenu_menu = (
        By.XPATH, "/html/body/main/div[1]/section[3]/div[1]/button")
    # 要素が表示されるまで最大5秒待つ
    element_srvmenu_menu = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_srvmenu_menu))
    # クリックする
    element_srvmenu_menu.click()

    # サービスメニューを選択する（NTT東光ネクスト）
    locator_srvmenu = (
        By.XPATH, "/html/body/main/div[1]/section[3]/div[2]/div/div/div[2]/table/tbody/tr[2]/td/label")
    # 要素が表示されるまで最大5秒待つ
    element_srvmenu = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_srvmenu))
    # クリックする
    element_srvmenu.click()

    # ISPを選択する
    locator_isp_menu = (
        By.XPATH, "/html/body/main/div[1]/section[4]/div[1]/button")
    # 要素が表示されるまで最大5秒待つ
    element_isp_menu = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_isp_menu))
    # クリックする
    element_isp_menu.click()

    # ISPを選択する（v6プラス）
    locator_isp = (
        By.XPATH, "/html/body/main/div[1]/section[4]/div[2]/div/div/div[2]/table/tbody/tr[30]/td[1]/label")
    # 要素が表示されるまで最大5秒待つ
    element_isp = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_isp))
    # クリックする
    element_isp.click()

    # 形態を選択する（マンション）
    locator_env = (
        By.XPATH, "/html/body/main/div[1]/section[5]/div/div/label[2]")
    # 要素が表示されるまで最大5秒待つ
    element_env = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_env))
    # クリックする
    element_env.click()

    # ネットワークを選択する（有線）
    locator_net = (
        By.XPATH, "/html/body/main/div[1]/section[6]/div/div/label[1]")
    # 要素が表示されるまで最大5秒待つ
    element_net = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_net))
    # クリックする
    element_net.click()

    # 利用規約を表示する
    locator_term = (
        By.XPATH, "/html/body/main/div[1]/section[7]/div[1]/button")
    # 要素が表示されるまで最大5秒待つ
    element_term = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_term))
    # クリックする
    element_term.click()
    # 3秒待つ
    time.sleep(3)
    # 末尾までジャンプする
    driver.find_element(
        By.XPATH, "/html/body/main/div[1]/section[7]/div[2]/div/div/div[2]/section/div[1]/ol[4]/li[3]").click()

    # 利用規約を閉じる
    locator_term_close = (
        By.XPATH, "/html/body/main/div[1]/section[7]/div[2]/div/div/div[1]/div/button")
    # 要素が表示されるまで最大5秒待つ
    element_term_close = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_term_close))
    # クリックする
    element_term_close.click()

    # 利用規約をチェックする
    locator_term_chk = (
        By.XPATH, "/html/body/main/div[1]/section[7]/span/label")
    # 要素が表示されるまで最大5秒待つ
    element_term_chk = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_term_chk))
    # クリックする
    element_term_chk.click()

    # 測定ボタンを押す
    locator_exec = (By.XPATH, "/html/body/main/div[1]/section[8]/button")
    # 要素が表示されるまで最大5秒待つ
    element_exec = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_exec))
    # クリックする
    element_exec.click()

    # 速度測定が完了するまで最大60秒待つ
    # 確認するボタンがクリック可能になったら完了とする
    locator_done = (
        By.XPATH, "/html/body/main/div[2]/div[2]/section[2]/button")
    element_done = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(locator_done))

    # IPv4ダウンロード速度を取得する
    locator_ipv4_down = (
        By.XPATH, "/html/body/main/div[2]/div[2]/section[1]/table/tbody/tr[2]/td[2]/span")
    # 要素が表示されるまで最大5秒待つ
    element_ipv4_down = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_ipv4_down))

    # IPv4アップロード速度を取得する
    locator_ipv4_up = (
        By.XPATH, "/html/body/main/div[2]/div[2]/section[1]/table/tbody/tr[2]/td[3]/span")
    # 要素が表示されるまで最大5秒待つ
    element_ipv4_up = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_ipv4_up))

    # IPv6ダウンロード速度を取得する
    locator_ipv6_down = (
        By.XPATH, "/html/body/main/div[2]/div[2]/section[1]/table/tbody/tr[3]/td[2]/span")
    # 要素が表示されるまで最大5秒待つ
    element_ipv6_down = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_ipv6_down))

    # IPv6アップロード速度を取得する
    locator_ipv6_up = (
        By.XPATH, "/html/body/main/div[2]/div[2]/section[1]/table/tbody/tr[3]/td[3]/span")
    # 要素が表示されるまで最大5秒待つ
    element_ipv6_up = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_ipv6_up))

    ipv4_down_text = element_ipv4_down.text
    ipv4_up_text = element_ipv4_up.text
    ipv6_down_text = element_ipv6_down.text
    ipv6_up_text = element_ipv6_up.text

    # 確認ボタンを押す
    locator_confirm = (
        By.XPATH, "/html/body/main/div[2]/div[2]/section[2]/button")
    # 要素がクリック可能になるまで最大5秒待つ
    element_confirm = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(locator_confirm))
    # クリックする
    element_confirm.click()

    # IPv6ダウンロード（NTT網内）速度を取得する
    locator_ipv6_flets_inner_down = (
        By.XPATH, "/html/body/main/div[2]/div[3]/section[1]/table/tbody/tr[3]/td[2]/span")
    # 要素が表示されるまで最大5秒待つ
    element_ipv6_flets_inner_down = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_ipv6_flets_inner_down))

    # IPv6アップロード（NTT網内）速度を取得する
    locator_ipv6_flets_inner_up = (
        By.XPATH, "/html/body/main/div[2]/div[3]/section[1]/table/tbody/tr[3]/td[3]/span")
    # 要素が表示されるまで最大5秒待つ
    element_ipv6_flets_inner_up = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(locator_ipv6_flets_inner_up))

    end_time = datetime.datetime.now()

    ipv6_flets_inner_down_text = element_ipv6_flets_inner_down.text
    ipv6_flets_inner_up_text = element_ipv6_flets_inner_up.text

    result['ipv4_down'] = ipv4_down_text
    result['ipv4_up'] = ipv4_up_text
    result['ipv6_down'] = ipv6_down_text
    result['ipv6_up'] = ipv6_up_text
    result['ipv6_flets_inner_down'] = ipv6_flets_inner_down_text
    result['ipv6_flets_inner_up'] = ipv6_flets_inner_up_text

    if (len(ipv4_down_text) == 0
            and len(ipv4_up_text) == 0
            and len(ipv6_down_text) == 0
            and len(ipv6_up_text) == 0
            and len(ipv6_flets_inner_down_text) == 0
            and len(ipv6_flets_inner_up_text) == 0):
        raise TryAgain
    else:
        return 'Success'


SELENIUM_ENDPOINT = "192.168.2.224:14444/wd/hub"
URL = "http://www.speed-visualizer.jp/"
OUTFILE = "result.csv"

# Chrome Optionsの設定
options = ChromeOptions()
options.add_argument("--disable-dev-shm-usage")  # ディスクのメモリスペースを使う
# GPUハードウェアアクセラレーションを無効。headlessモードで暫定的に必要なフラグ
# options.add_argument("--disable-gpu")
# options.add_argument("--headless")              # headlessモードを使用する
options.add_argument("--no-sandbox")            # sandboxモードを解除する

# Selenium Serverに接続
driver = webdriver.Remote(
    command_executor=SELENIUM_ENDPOINT,
    options=options
)

start_time = datetime.datetime.now()
result = {'ipv4_down': "",
          'ipv4_up': "",
          'ipv6_down': "",
          'ipv6_up': "",
          'ipv6_flets_inner_down': "",
          'ipv6_flets_inner_up': ""}

try:
    exec_result = execute(driver, result)
except TryAgain:
    exec_result = 'Failed'
finally:
    driver.close()
    driver.quit()

    end_time = datetime.datetime.now()

    start_time_text = start_time.strftime('%Y-%m-%d %H:%M:%S')
    end_time_text = end_time.strftime('%Y-%m-%d %H:%M:%S')

    print('Content-Type: text/plain; charset=UTF-8\n')
    print(start_time_text)
    print(end_time_text)

    print(result['ipv4_down'])
    print(result['ipv4_up'])
    print(result['ipv6_down'])
    print(result['ipv6_up'])

    print(result['ipv6_flets_inner_down'])
    print(result['ipv6_flets_inner_up'])

    # 上位ディレクトリパスを取得
    parent = Path(__file__).resolve().parent
    # 結果ファイルを取得
    path = parent.joinpath(OUTFILE)
    is_file = os.path.isfile(path)
    # 結果ファイルがなければ新規作成しヘッダを追記
    if is_file:
        pass
    else:
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['start_time',
                             'end_time',
                             'ipv4_down',
                             'ipv4_up',
                             'ipv6_down',
                             'ipv6_up',
                             'ipv6_down_flets_inner',
                             'ipv6_up_flets_inner'])
    # 結果を追記
    if exec_result == 'Success':
        with open(path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([start_time_text,
                            end_time_text,
                            result['ipv4_down'],
                            result['ipv4_up'],
                            result['ipv6_down'],
                            result['ipv6_up'],
                            result['ipv6_flets_inner_down'],
                            result['ipv6_flets_inner_up']
                             ])
    else:
        pass

exit()
