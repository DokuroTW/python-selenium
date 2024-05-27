from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用 Chrome 
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Google 網頁
driver.get("https://www.google.com")

# 找到搜索
search_box = driver.find_element("name", "q")

# 在搜索中輸入 "Selenium"
search_box.send_keys("Selenium")

# 按下 Enter 鍵
search_box.send_keys(Keys.ENTER)

# 等待搜索結果
driver.implicitly_wait(5)

# 關閉瀏覽器
driver.quit()
