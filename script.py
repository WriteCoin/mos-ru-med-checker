# %%
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from for_selenium.driver.script import Script, FindOptions
import json
from functools import reduce
from typing import Optional

class MosRuMedChecker(Script):
    data: dict


if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get("https://mos.ru")
    auth_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label=\"Вход/Регистрация\"")
    auth_btn.click()
    script = MosRuMedChecker(url="https://mos.ru", cookie_path="cookie")
    script.set_driver(driver)
    with open("data.json", 'r') as fd:
        script.data = json.load(fd)[0]
    input_login_btn = script.wait_element(FindOptions(By.CSS_SELECTOR, "input#login"))
    input_password_btn = script.wait_element(FindOptions(By.CSS_SELECTOR, "input#password"))

    # %%
    auth_btn = script.wait_element(FindOptions(By.CSS_SELECTOR, "button#bind"))

    # %%
    input_login_btn.send_keys(script.data["login"])
    input_password_btn.send_keys(script.data["password"])
    auth_btn.click()

    # %%
    auth_btn = script.wait_element(FindOptions(By.CSS_SELECTOR, "button[aria-label=\"Меню пользователя\"]"))
    auth_btn

    # %%
    script.hover_element(auth_btn)

    # %%
    personal_link_btn_opt = FindOptions(By.LINK_TEXT, "Личный кабинет")
    while not script.is_element_exists(personal_link_btn_opt):
        auth_btn.click()
    personal_link_btn = script.find_element(personal_link_btn_opt)
    personal_link_btn

    # %%
    personal_link_btn.click()

    # %%
    # new_record_btn = script.wait_element(FindOptions(By.LINK_TEXT, "Новая запись"))
    driver.refresh()
    new_record_btn = script.wait_element(FindOptions(By.CSS_SELECTOR, "span.nlk-button__content"))
    new_record_btn

    # %%
    driver.refresh()
    new_record_btn = script.wait_element(FindOptions(By.CSS_SELECTOR, "span.nlk-button__content"))
    script.hover_element(new_record_btn)
    new_record_btn = script.wait_element(FindOptions(By.CSS_SELECTOR, "span.nlk-button__content"))
    new_record_btn.click()

    # %%
    elem_list = script.find_elements(FindOptions(By.TAG_NAME, "button"))
    result = None
    if not script.driver is None: 
        # result = script.driver.execute_script(" var x = $('arguments[0]').find(\":contains('<svg ')\"); return x;", argument)
        pass
    text = "Продолжить"
    def reducer_func(el_prev: Optional[WebElement], el: Optional[WebElement]):
        def has(el: Optional[WebElement]) -> bool:
            if not el is None:
                # print(el.get_attribute('innerHTML'))
                return el.get_attribute('innerHTML').__contains__(text)
            return False
        if has(el_prev):
            return el_prev
        elif has(el):
            return el
        return None
    result = reduce(reducer_func, elem_list)
    # print(result)
    # frame_list = script.find_elements(FindOptions(By.TAG_NAME, 'frame'))
    # iframe_list = script.find_elements(FindOptions(By.TAG_NAME, 'iframe'))
    # for frame in frame_list:
    #     elem_list.extend(script.find_elements(FindOptions(By.TAG_NAME, 'button'), frame))
    # for iframe in iframe_list:
    #     elem_list.extend(script.find_elements(FindOptions(By.TAG_NAME, 'button'), iframe))
    # elem_list
    # for elem in elem_list:
    #     print("Текст: ", elem.get_attribute('innerHTML'))
    # script.find_elements(FindOptions(By.TAG_NAME, "iframe"))
    print(result)
    print(elem_list)
    # result.get_attribute('innerHTML')

    # %%
    script.find_elements(FindOptions(By.CSS_SELECTOR, '*'))

    # %%
    # elem = script.find_element(FindOptions(By.XPATH, "//[normalize-space(.)='Новая запись' and contains(@class, 'mos-h1')]"))
    elem = driver.find_element(By.XPATH, '//[normalize-space(.)="Новая запись" and contains(@class, "mos-h1")]')

    # %%
    text = 'Продолжить'
    elem_list = script.find_elements(FindOptions(By.CSS_SELECTOR, "h1"))

    result = []
    for elem in elem_list:
        if elem.get_attribute('innerHTML') == text:
            result.append(elem)
    if len(result) == 1:
        result = result[0]

    print(result)
    for elem in elem_list:
        print("Текст: ", elem.get_attribute('innerHTML'))

    # %%
    # result.click()
