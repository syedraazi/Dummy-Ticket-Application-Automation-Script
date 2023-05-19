# Automated the --Dummy Ticket Application--
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service                   # Selenium 4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()                                   #Used to hold the window from closing
options.add_experimental_option("detach",True)                      #Used to hold the window from closing
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")      # Selenium 4
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

print("Currect URL- "+driver.current_url)
print("Currect TITLE- "+driver.title)

# Example 1 -> Dummy hotel booking  —  USD $20.00
#driver.find_element(By.XPATH,"//input[@id='product_551']").click()
# Example 2 -> Dummy ticket and hotel  —  USD $35.00
driver.find_element(By.XPATH,"//input[@id='product_3186']").click()
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("Sraz")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("RRR")
driver.find_element(By.XPATH,"//textarea[@id='order_comments']").send_keys("N/A")

##################  Date Picker(By using drop-downs) ##############################
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='dob']").click()

#Month
time.sleep(1)
dob_month=driver.find_element(By.XPATH,"//select[@aria-label='Select month']")
month=Select(dob_month)
month.select_by_visible_text("Jan")
#Year
time.sleep(1)
dob_year=driver.find_element(By.XPATH,"//select[@aria-label='Select year']")
year=Select(dob_year)
year.select_by_value("1990")
#Date
time.sleep(1)
dob_dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date in dob_dates:
    if date.text=="23":
        date.click()
        break

#Gender
driver.find_element(By.ID,"sex_1").click()

driver.find_element(By.XPATH,"//input[@id='traveltype_1']").click()
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("LKO")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("BLR")

##################  Date Picker##############################
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='departon']").click()

#Month
time.sleep(1)
travel_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
travel_month.select_by_visible_text("Jul")
#Year
time.sleep(1)
travel_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
travel_year.select_by_value("2023")
#Date
time.sleep(1)
travel_date=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for dat in travel_date:
    if dat.text=="25":
        dat.click()
        break

time.sleep(2)
# driver.find_element(By.XPATH,"//p[@id='reasondummy_field']//span[@role='combobox']")
# # time.sleep(3)
# # driver.find_element(By.XPATH,"//span[@class='select2-selection__clear']").clear()
# #abc=Select(driver.find_elements(By.XPATH,"//*[@id='select2-reasondummy-container']"))
# abc=Select(driver.find_elements(By.XPATH,"//*[@id='reasondummy_field']/span/span/span[1]/span/span[2]"))
# abc.select_by_visible_text("Visa application")

#Delivery
driver.find_element(By.XPATH,"//input[@id='deliverymethod_1']").click()

driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("8273468222")
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("sabc@gmail.com")
# abc=Select(driver.find_elements(By.XPATH,"//span[@id='select2-billing_country-container']"))
# abc.select_by_value("Canada")
driver.find_element(By.XPATH,"//input[@id='billing_address_1']").send_keys("abs street")
driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys("Bramp")

########## Drop Down which has values to be entered and then selected ########
driver.find_element(By.XPATH,"//*[@id='select2-billing_state-container']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@role='combobox']").send_keys("Alberta")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='select2-billing_state-results']/li[1]").click()

time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("216067")

## Table ####

#row=driver.find_element(By.XPATH,"//table[@class='shop_table woocommerce-checkout-review-order-table']//tr[2]").text
row=driver.find_element(By.XPATH,"//*[@id='order_review']/div[1]/table/tbody/tr/td[2]/span").text
print("Product Selected- "+ row)             # o/p -> Product Selected USD $20.00

price=driver.find_element(By.XPATH,"//*[@id='order_review']/div[1]/table/tfoot/tr[2]/td/strong/span").text
print("Order Total- "+price)                 # o/p -> Order Total USD $20.00

# Validate if the price selected is matched with the displayed
if row==price:
    print("Price Validated and is CORRECT")                  # o/p -> Price Matched
else:
    print("Price Validated and is IN-CORRECT")

time.sleep(10)
driver.close()
input("Press Enter to close the browser window...")
