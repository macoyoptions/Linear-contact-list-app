# Testing for Chrome driver

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://thinking-tester-contact-list.herokuapp.com/")

# Maximize the browser window for better visibility
driver.maximize_window()

# Set an implicit wait time of 30 seconds to handle dynamic elements
driver.implicitly_wait(30)

# Testing for Negative login
# On the home page Find the email input field by its xpath and enter an email that is not used while doing registration
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[1]/input").send_keys("adeayo@gmail")
time.sleep(5)

# On the home page Find the password input field by its xpath and enter the password
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[2]/input").send_keys("adeola12")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# Initialize Chrome WebDriver again for the negative login
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://thinking-tester-contact-list.herokuapp.com/")

# Maximize the browser window for better visibility
driver.maximize_window()

# Set an implicit wait time of 30 seconds to handle dynamic elements
driver.implicitly_wait(30)

# Testing for positive login
# On the home page Find the email input field by its xpath and enter an email.
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[1]/input").send_keys("adetiba@gmail.com")
time.sleep(5)

# On the home page Find the password input field by its xpath and enter the password
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[2]/input").send_keys("adeola12")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# after successful login into the app add 10 fresh contacts
# for the first contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("Banji")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("siju")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("oshodi@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the second contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("ibrahim")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("danjuma")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1995-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("danjumii@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("gbemileke street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("adisa street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("akure")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("ondo")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1566")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 3rd contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("daniel")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("shade")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1992-06-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("jimoh@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0705453533")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ibrahim chatter street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("dodondawa street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("kano")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("zamfara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("5696")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 4th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("bimpe")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("adeolu")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("shikemiii@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kaduna")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1486")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 5th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("bisola")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("shadia")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("scylla@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0903445323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 6th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("dija")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("Adijah")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("wandey@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("iyere")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 7th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("bisola")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("shadia")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("scylla@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0903445323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 8th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("dija")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("Adijah")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("wandey@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("iyere")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 9th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("shayo")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("aina")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("scylla@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0903445323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 10th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("dija")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("Adijah")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("wandey@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("iyere")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# After successful addition of 10 new contact,navigate to logout button
# Find the logout button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/header/button').click()
time.sleep(5)

# Pause the script execution for 5 seconds to visually inspect the result
time.sleep(5)

# Quit the WebDriver, closing all associated windows and ending the session
driver.quit()


# Testing for Firefox driver

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Firefox WebDriver
driver = webdriver.Firefox()

# Navigate to the URL
driver.get("https://thinking-tester-contact-list.herokuapp.com/")

# Maximize the browser window for better visibility
driver.maximize_window()

# Set an implicit wait time of 30 seconds to handle dynamic elements
driver.implicitly_wait(30)

# Testing for Negative login
# On the home page Find the email input field by its xpath and enter an email that is not used while doing registration
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[1]/input").send_keys("adeayo@gmail")
time.sleep(5)

# On the home page Find the password input field by its xpath and enter the password
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[2]/input").send_keys("adeola12")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# Initialize Chrome WebDriver again for the negative login
driver = webdriver.Firefox()

# Navigate to the URL
driver.get("https://thinking-tester-contact-list.herokuapp.com/")

# Maximize the browser window for better visibility
driver.maximize_window()

# Set an implicit wait time of 30 seconds to handle dynamic elements
driver.implicitly_wait(30)

# Testing for positive login
# On the home page Find the email input field by its xpath and enter an email.
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[1]/input").send_keys("adegbemi@gmail.com")
time.sleep(5)

# On the home page Find the password input field by its xpath and enter the password
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[2]/input").send_keys("adeola12")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# after successful login into the app add 10 fresh contacts
# for the first contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("Banji")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("siju")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("oshodi@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the second contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("ibrahim")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("danjuma")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1995-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("danjumii@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("gbemileke street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("adisa street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("akure")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("ondo")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1566")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 3rd contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("daniel")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("shade")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1992-06-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("jimoh@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0705453533")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ibrahim chatter street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("dodondawa street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("kano")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("zamfara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("5696")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 4th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("bimpe")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("adeolu")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("shikemiii@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kaduna")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1486")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 5th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("bisola")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("shadia")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("scylla@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0903445323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 6th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("dija")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("Adijah")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("wandey@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("iyere")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 7th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("bisola")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("shadia")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("scylla@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0903445323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 8th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("dija")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("Adijah")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("wandey@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("iyere")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 9th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("shayo")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("aina")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("scylla@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0903445323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 10th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("dija")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("Adijah")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("wandey@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("iyere")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# After successful addition of 10 new contact,navigate to logout button
# Find the logout button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/header/button').click()
time.sleep(5)

# Pause the script execution for 5 seconds to visually inspect the result
time.sleep(5)

# Quit the WebDriver, closing all associated windows and ending the session
driver.quit()

# Testing for Edge driver

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Edge WebDriver
driver = webdriver.Edge()

# Navigate to the URL
driver.get("https://thinking-tester-contact-list.herokuapp.com/")

# Maximize the browser window for better visibility
driver.maximize_window()

# Set an implicit wait time of 30 seconds to handle dynamic elements
driver.implicitly_wait(30)

# Testing for Negative login
# On the home page Find the email input field by its xpath and enter an email that is not used while doing registration
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[1]/input").send_keys("adeayo@gmail.com")
time.sleep(5)

# On the home page Find the password input field by its xpath and enter the password
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[2]/input").send_keys("adeola12")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# Initialize Edge WebDriver again for the negative login
driver = webdriver.Edge()

# Navigate to the URL
driver.get("https://thinking-tester-contact-list.herokuapp.com/")

# Maximize the browser window for better visibility
driver.maximize_window()

# Set an implicit wait time of 30 seconds to handle dynamic elements
driver.implicitly_wait(30)

# Testing for positive login
# On the home page Find the email input field by its xpath and enter an email.
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[1]/input").send_keys("adeyeri@gmail.com")
time.sleep(5)

# On the home page Find the password input field by its xpath and enter the password
driver.find_element(By.XPATH, "/html/body/div[3]/form/p[2]/input").send_keys("adeola12")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# after successful login into the app add 10 fresh contacts
# for the first contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("Banji")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("siju")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("oshodi@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the second contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("ibrahim")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("danjuma")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1995-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("danjumii@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("gbemileke street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("adisa street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("akure")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("ondo")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1566")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 3rd contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("daniel")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("shade")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1992-06-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("jimoh@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0705453533")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ibrahim chatter street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("dodondawa street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("kano")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("zamfara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("5696")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 4th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("bimpe")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("adeolu")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("shikemiii@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kaduna")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1486")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 5th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("bisola")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("shadia")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("scylla@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0903445323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 6th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("dija")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("Adijah")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("wandey@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("iyere")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 7th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("bisola")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("shadia")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("scylla@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0903445323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 8th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("dija")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("Adijah")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("wandey@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("iyere")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 9th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("shayo")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("aina")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("scylla@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("0903445323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("ilorin")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# for the 10th contact,Find the add new contact button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/p[2]/button').click()
time.sleep(5)

# On the add new contact page find the firstname input field by its ID and enter the firstname
driver.find_element(By.ID, "firstName").send_keys("dija")
time.sleep(5)

# On the add new contact page Find the lastname input field by its xpath and enter the lastname
driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input[2]").send_keys("Adijah")
time.sleep(5)

# On the add new contact page Find the date of birth input field by its ID and enter the DOB
driver.find_element(By.ID, "birthdate").send_keys("1993-04-12")
time.sleep(5)

# On the add new contact page Find the Email input field by its ID and enter the email
driver.find_element(By.ID, "email").send_keys("wandey@gmail.com")
time.sleep(5)

# On the add new contact page Find the number input field by its ID and enter the number
driver.find_element(By.ID, "phone").send_keys("09034563323")
time.sleep(5)

# On the add new contact page Find the first address input field by its ID and enter the street
driver.find_element(By.ID, "street1").send_keys("ajayi goearge street")
time.sleep(5)

# On the add new contact page Find the second address input field by its ID and enter the street
driver.find_element(By.ID, "street2").send_keys("agbaje kuti street")
time.sleep(5)

# On the add new contact page Find the city input field by its ID and enter the city
driver.find_element(By.ID, "city").send_keys("iyere")
time.sleep(5)

# On the add new contact page Find the state input field by its ID and enter the state
driver.find_element(By.ID, "stateProvince").send_keys("kwara")
time.sleep(5)

# On the add new contact page Find the postal input field by its ID and enter the postal code
driver.find_element(By.ID, "postalCode").send_keys("1906")
time.sleep(5)

# On the add new contact page Find the country input field by its ID and enter the country
driver.find_element(By.ID, "country").send_keys("nigeria")
time.sleep(5)

# Find the submit button using ID and click on it
driver.find_element(By.ID, 'submit').click()
time.sleep(5)

# After successful addition of 10 new contact,navigate to logout button
# Find the logout button using xpath and click on it
driver.find_element(By.XPATH, '/html/body/div/header/button').click()
time.sleep(5)

# Pause the script execution for 5 seconds to visually inspect the result
time.sleep(5)

# Quit the WebDriver, closing all associated windows and ending the session
driver.quit()
