# python-selenium
python selenium

### 取得標籤 ID、CSS_SELECTOR

`<div id='head'>網頁</div>`

`<div data_abc='test'>字串</div>'`

```CMD
driver.find_element(By.ID,"head")

driver.find_element(By.CSS_SELECTOR,"[data_abc=test]")
```

### 鍵盤操作

```CMD
element = driver.find_element("_____")
element.send_key(keys.ENTER)
```

### 執行

`SHELL:> python p_selenium.py`
