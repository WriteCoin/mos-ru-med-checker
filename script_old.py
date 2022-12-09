import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep, time
from for_selenium.captcha.captcha import ManualCaptcha
from for_selenium.driver.script import Script, FindOptions

class MosRuMedChecker(Script):
    pass

if __name__ == '__main__':
    script = MosRuMedChecker(url="https://mos.ru", cookie_path="cookies", driver=uc.Chrome())
    try:
        with script.start():
            t0 = time()
            script.sleep(1.25)
            t1 = time()
            print(f"time: {t1 - t0}")
    except RuntimeError as e:
        if e.__str__() == "generator didn't stop":
            pass
        else:
            raise e

    # driver = uc.Chrome()
    # driver.get('https://translate.yandex.ru')
    # textarea = driver.find_element(By.CSS_SELECTOR, '#fakeArea')
    # textarea.send_keys("На сопках Маньчжурии")
    # sleep(5)
    # driver.close()