import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
def verify_URL(expected_url,actual_url):
    assert expected_url == actual_url
def verify_workout_title(expected_workout_titletitle, actual_workout_title):
    assert expected_workout_title == actual_workout_title


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://cloud.tacx.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//button[contains(text(),'Sign in with Garmin')]").click()
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "gauth-widget-frame-gauth-widget")))
driver.switch_to.frame("gauth-widget-frame-gauth-widget")
driver.find_element(By.ID,"lnkCreateAccount").click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("popup-iframe-id")
driver.find_element(By.NAME,"name").send_keys("Aisha")
driver.find_element(By.NAME,"email").send_keys("aishazulukhw993@gmail.com")
driver.find_element(By.NAME,"emailMatch").send_keys("aishazulukhw993@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Aisha@123")
driver.find_element(By.NAME,"passwordMatch").send_keys("Aisha@123")
driver.find_element(By.NAME,"globalOptIn").click()
driver.find_element(By.NAME,"termsOfUse").click()
driver.find_element(By.ID,"confirmAge").click()
driver.find_element(By.ID,"submitBtn").click()
driver.switch_to.default_content()
WebDriverWait(driver,30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".active>.ng-binding")))
expected_url = driver.current_url
actual_url = "https://cloud.tacx.com/#/dashboard"
verify_URL(expected_url,actual_url)
driver.find_element(By.CSS_SELECTOR,".sidenav-element:nth-child(4) .ng-binding").click()
driver.find_element(By.CSS_SELECTOR, ".md-button:nth-child(2) .training-type").click()
driver.find_element(By.CSS_SELECTOR, ".md-button:nth-child(2) .training-target").click()
driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").click()
time.sleep(3)
element = driver.find_element(By.XPATH, "//button[@class='cursor-btn up-btn increase-indicator-value-control disable-md-button-for-touch md-button md-ink-ripple']//ng-md-icon[@class='ng-scope']//*[name()='svg']")
for i in range(0, 20):
    element.click()
    time.sleep(1)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".action-btn.save-btn").click()
element_input = driver.find_element(By.CSS_SELECTOR, ".ng-pristine.ng-valid.md-input")
element_input.click()
element_input.clear()
element_input.send_keys("MyWorkout")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".md-button.md-ink-ripple.md-altTheme-theme:nth-child(2").click()
WebDriverWait(driver,30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".class-text-style.ng-binding.ng-scope")))
expected_workout_title = driver.find_element(By.CSS_SELECTOR, ".class-text-style.ng-binding.ng-scope").text
print(expected_workout_title)
actual_workout_title = "MyWorkout"
verify_workout_title(expected_workout_title, actual_workout_title)
time.sleep(2)
driver.find_element(By.XPATH, "//div[normalize-space()='Sign Out']").click()

