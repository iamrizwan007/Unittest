from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\\Users\\mrizwan5\Desktop\\Python\\Selenium\\chromedriver.exe')
driver.get("https://www.google.com/")
print("Title of the page is: ",driver.title)
print("current page URL:",driver.current_url)
driver.get("http://www.durgasoft.com/")
print("title:",driver.title)
print("URL:",driver.current_url)
driver.back()
print("title",driver.title)
print("URL:",driver.current_url)
driver.forward()
print(driver.title)
print(driver.current_url)
driver.close()