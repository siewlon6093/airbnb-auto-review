import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = Options()
# chrome stay open after code end
chrome_options.add_argument('--user-data-dir=C:\\Users\\New User\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.airbnb.com/hosting')

try:
    Login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-testid='signup-login-btn']"))
    )
except:
    print("Login page not found. Skipping login process.")
else:
    # login to website
    Country = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "country"))
    )

    Country.send_keys('Malaysia')

    Phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "phoneInputphoneNumber"))
    )

    Country.send_keys('Malaysia')
    Phone.send_keys('xxxxxxxx')
    sleep(2)
    Submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='signup-login-submit-btn']"))
    )

    Submit.click()

    input('[+] Please type in 6 pin and Enter to next step:  ')

driver.get('https://www.airbnb.com/hosting/reservations/completed')

try:
    review = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, ""'reviews')]")))

except:
    print("[-] No Review Needed to do")
    driver.close()

else:
    hrefs = []
    for element in review:
        href = element.get_attribute("href")
        hrefs.append(href)

    # Write the href values to a text file
    with open("my-hrefs.txt", "w") as f:
        for href in hrefs:
            f.write(href + "\n")

    if os.path.exists("my-hrefs.txt"):
        # read URLs from text file
        with open("my-hrefs.txt", "r") as f:
            urls = f.readlines()

        # open each URL in a new browser window/tab
        for url in urls:
            driver.get(url.strip())

            # Start review
            start = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )

            start.click()

            # Start review cleanness
            review = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[@for='cid:CLEANLINESS_star_row4']")))
            review.click()

            # Done review cleanness
            review_cleanliness_done = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )

            review_cleanliness_done.click()

            sleep(3)

            # Start review house rules
            review_hr = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[@for='cid:RESPECT_HOUSE_RULES_star_row4']")))

            review_hr.click()

            # Done review house rules
            review_hr_done = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )

            review_hr_done.click()

            sleep(3)

            # Start review Community star
            review_cs = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[@for='cid:COMMUNICATION_star_row4']")))
            review_cs.click()

            # Done review Community star
            review_cs_done = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )

            review_cs_done.click()
            sleep(3)

            # Start Public Review
            review_pr = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@name='cid:public_review_text_area']")))
            review_pr.clear()
            review_pr.send_keys("Dear Guest,\n\n\
            It was a pleasure hosting you during your stay at our Airbnb. Thank you for choosing our home as your accommodation during your trip to Ipoh. We hope you enjoyed your stay and that everything met your expectations.\n\n\
            They were communicative, respectful, and left the space in excellent condition. We appreciate how tidy and organized they left everything, which made the cleaning process much easier. They were also very responsible with the keys and took good care of the property during their stay.\n\n\
            We highly recommend this guest to any other Airbnb hosts out there. It was truly a pleasure to host them, and we would welcome them back to our home anytime.\n\n\
            Thank you again for choosing our Airbnb, and we hope to have the opportunity to host you again in the future.\n\n\
            Best regards,\nAdam Chong")

            # Done review public Review
            review_pr_done = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )

            review_pr_done.click()
            sleep(3)

            # Start recommend
            review_rd = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[@id='cid:recommend_toggle_yes']")))
            review_rd.click()

            # Done review recommend
            review_rd_done = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )

            review_rd_done.click()
            sleep(3)

            # Done Submit
            Submit_review = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )

            Submit_review.click()

            sleep(3)
        # close the original window/tab
        driver.close()
    else:
        print("The text file 'my-hrefs.txt' does not exist.")
    driver.close()
