import undetected_chromedriver as uc
import time
if __name__ == '__main__':
    driver = uc.Chrome(headless=True,use_subprocess=False)
    driver.get('https://nowsecure.nl')
    time.sleep(2)
    driver.save_screenshot('nowsecure.png')