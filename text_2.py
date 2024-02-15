from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 启动浏览器并打开网页
driver = webdriver.Chrome()
driver.get("your_webpage_url")

# 等待页面加载完成
wait = WebDriverWait(driver, 10)

# 定位到div元素
div_element = wait.until(EC.presence_of_element_located((By.ID, "div_id")))

# 获取div元素的父元素
parent_element = div_element.find_element_by_xpath("..")

# 创建noscript元素
noscript_element = driver.execute_script("""
    var no_script = document.createElement('NOSCRIPT');
    no_script.innerHTML = 'Your desired content here';
    return no_script;
""")

# 将noscript元素插入到div元素之前
driver.execute_script("arguments[0].insertBefore(arguments[1], arguments[2]);", parent_element, noscript_element, div_element)