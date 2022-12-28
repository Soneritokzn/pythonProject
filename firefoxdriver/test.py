import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager



class Test:
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    url = "https://stage3.agggro.private/login"

    try:
        driver.get(url=url)
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@class='link--K8aqB loginForm__link--JSKIx']").click()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys("sales-user")
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123login123")
        driver.find_element(By.XPATH, "//span[@class='MuiButton-label']").click()
        time.sleep(5)

        # driver.get("https://stage2.agggro.private/tasks")
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Задачи')]"))).click()


        #Add locator for adding
        driver.find_element(By.XPATH,
                            "//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-fullWidth MuiInputBase-formControl']//input[@type='text']") \
            .send_keys("Autotest")
        driver.find_element(By.XPATH,
                            "//body[@style='overflow: hidden;']/div[@class='MuiDialog-root taskCreateModal--fMs_f']/div[@class='MuiDialog-container MuiDialog-scrollPaper']/div[@class='MuiPaper-root MuiDialog-paper taskCreateModal__window--3nOex MuiDialog-paperScrollPaper MuiDialog-paperWidthFalse MuiDialog-paperFullWidth MuiPaper-elevation24 MuiPaper-rounded']/div[@class='agggro scrollContainer']/form/div[@class='MuiDialogContent-root']/div[@class='formField--fhG20 taskCreateModal__formRow--VfqQd fullWidth--r_r4o']/div[@class='formField__input--ipKjU']/div[@class='MuiInputBase-root MuiOutlinedInput-root textarea--V31Md MuiInputBase-fullWidth MuiInputBase-multiline MuiOutlinedInput-multiline MuiInputBase-adornedEnd MuiOutlinedInput-adornedEnd']/textarea[1]") \
            .send_keys("Blabl")
        driver.find_element(By.XPATH,
                            "//button[@type='submit']//span[@class='MuiButton-label'][contains(text(),'Сохранить')]").click()
        task = driver.find_element(By.XPATH,
                                   "//a[@class='MuiTypography-root MuiLink-root MuiLink-underlineAlways MuiTypography-colorPrimary']")

        time.sleep(10)


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
