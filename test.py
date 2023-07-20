import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Ruta al Chromedriver descargado
chrome_driver_path = 'C:\\Users\\admin\\Desktop\\WebDriver\\chromedriver.exe' # En Windows | tu ruta aqui
# chrome_driver_path = '/ruta/al/chromedriver' # En macOS/Linux

# Configuración del Service de Chrome
service = ChromeService(executable_path=chrome_driver_path)

# Configuración del controlador Chrome con el Service
driver = webdriver.Chrome(service=service)

time.sleep(2)



# Acceder a la página web
driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(2)

# Type username "student" into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password "Password123" into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

# Find and click the "Submit" button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(5)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"
# Verify button Log out is displayed on the new page
log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert log_out_button_locator.is_displayed()
