import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    print(driver.title)

    # 获取输入框id
    search_key = driver.find_element_by_id("kw")
    # 输入要搜索的内容
    search_key.send_keys("selenium")
    # 获取按钮
    search_btn = driver.find_element_by_id("su")
    # 按钮点击事件
    search_btn.click()

    all_win = driver.window_handles
    print(all_win)
    # 返回之前的浏览器窗口
    # 1.获取当前浏览器的窗口
    curr = driver.current_window_handle
    driver.switch_to.window(all_win[0])
    # 获取搜索出来结果
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="3"]/h3/a').click()
    # 打开新的窗口
    time.sleep(3)
    all_o = driver.window_handles
    print(all_o)
    driver.switch_to.window(all_o[1])
    print(driver.title)
    time.sleep(8)
    cl = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/aside/section[2]/div[3]/div[1]')

    print(cl.text)

    action_chains = ActionChains(driver)
    action_chains.move_to_element(cl).perform()

    action_chains.click(cl).perform()
# 关闭tab

    # driver.quit()
