from selenium import webdriver
from seleniumwire import webdriver as wiredriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from mailTm.email import Email
import re
import json
from bs4 import BeautifulSoup

# def listener(message):
#     print(message)

def automate_registration():
    # Set the path to the webdriver executable
    extension_path = "C:/Users/shiva/AppData/Local/Google/Chrome/User Data/Profile 1/Extensions/ndklagefmdogpfkffimjdnbnplllndic/2.0.1_0.crx"
    proxy_server_url = "http://f6f0d2db7cfbe235:RNW78Fm5@res.proxy-seller.com:10000"

    
    seleniumwire_options = {
        'proxy': {
            'http': proxy_server_url,
            'https': proxy_server_url,
            'no_proxy': 'localhost,127.0.0.1',
            'verify_ssl': False,
        },
    }


    opt = webdriver.ChromeOptions()
    opt.add_extension(extension_path)
    opt.add_argument('--ignore-certificate-errors')
    opt.add_argument('--ignore-ssl-errors')
    opt.add_argument('--ssl-version-max=tls1.2')
    opt.add_argument('–disable-dev-sh-usage')
    #opt.add_argument(f'--proxy-server={proxy_server_url}')
    driver = wiredriver.Chrome(seleniumwire_options=seleniumwire_options, options=opt)
    # driver.get('http://httpbin.org/ip')
    # print(driver.find_element(By.TAG_NAME, 'body').text) # { "origin": "185.199.229.156" }

    test = Email()
    print("\nDomain: " + test.domain)
    # Make new email address
    test.register()
    print("\nEmail Address: " + str(test.address))
    address = str(test.address)
    print(address)
    # test.start(listener)

    if address:
        
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        
        ele = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/a[1]/span')))
        ele.click()
        print('hii')
        

        # Wait for the email input field to be visible
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div[1]/div[1]/input')))
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div[2]/div[1]/input')))
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div[3]/div[1]/input')))

        # Enter the email address into the input field
        username =  address.split('@')[0]
        username_input.send_keys(username)
        email_input.send_keys(address)
        password_input.send_keys("Shivansh070@")
        print('hiiii')
        time.sleep(10)

        checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div[4]/label/div')))
        checkbox.click()

        time.sleep(5)

        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/a/span')))
        next_button.click()

        time.sleep(5)

        confirmPassword_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div/input')))
        confirmPassword_input.send_keys("Shivansh070@")

        time.sleep(1)

        next_button_final = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/a/span')))
        next_button_final.click()

        time.sleep(10)


        otp_messages=test.message_list()
        new_message=otp_messages[0]
        message_id= new_message['id']
        print(message_id)
        msg_data=test.message(message_id)
       
        
        html_content = msg_data['html']
        soup = BeautifulSoup(html_content[0], 'html.parser')

       # Find the OTP element by its tag and class
        otp_element = soup.find('h2', {'style': 'display: flex; align-items: center; justify-content: flex-start; position: relative; text-align: start; color: #1a6af4; font-size: 24px; font-weight: 700; margin-top: 10px;'})

        if otp_element:
         verification_code = otp_element.text.strip()
         print("OTP:", verification_code)
        else:
         print("OTP not found.")
        

        # Input the OTP into the designated field
        otp_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div/input')))
        otp_input.send_keys(verification_code)
        time.sleep(2)

        # Click on the final button
        final_submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/a/span')))
        final_submit_button.click()
        print(' otp verification done ')

        time.sleep(10)
        print(driver.window_handles,'driver.window_handles')
    
        #sumSubKyc 
        continue_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div/footer/button')))
        #continue_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div/footer/button/span')))
        continue_button.click()

        time.sleep(10)
        

        continue_this_device_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/footer/div/button[1]/span')))
        continue_this_device_button.click()

        other_radio_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/main/fieldset/span/label[2]/label/span')))
        other_radio_button.click()

        agree_and_continue_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/footer/button/span')))
        agree_and_continue_button.click()

        email_input=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div/main/input')))
        email_input.send_keys(address)

        send_verification_code_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/footer/div/button[1]/span')))
        send_verification_code_button.click()

        otp_messages=test.message_list()
        print(otp_messages)
        new_message=otp_messages[0]
        print(new_message)

        otp_input_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/main/label')))
        otp_input_button.click()
   
        time.sleep(1000)
    

automate_registration()
