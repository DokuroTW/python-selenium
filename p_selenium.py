from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用 Chrome 瀏覽器
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 打開 Google 網頁
driver.get("https://www.google.com")

# 找到搜索框
search_box = driver.find_element("name", "q")

# 在搜索框中輸入 "Selenium"
search_box.send_keys("Selenium")

# 模擬按下 Enter 鍵
search_box.send_keys(Keys.ENTER)

# 等待搜索結果加載
driver.implicitly_wait(5)

# 打印頁面標題
print(driver.title)

# 關閉瀏覽器
driver.quit()
