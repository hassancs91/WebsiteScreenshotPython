from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium_stealth import stealth

start_time = time.time()


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(
    options=options, executable_path="E:\TechVideos\Python\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


url = "https://learnwithhasan.com"  # change the url

driver.get(url)

driver.save_screenshot("test3.png")  # change image name

elapsed = "%s seconds" % (time.time() - start_time)

print("Done in " + elapsed)
