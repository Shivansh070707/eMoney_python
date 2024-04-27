from selenium import webdriver
from seleniumwire import webdriver as wiredriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from mailTm.email import Email
from bs4 import BeautifulSoup
import random
from faker import Faker
import threading
import csv


# Initialize Faker to generate random last names
faker = Faker()

def write_to_csv(data):
    with open('registration_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def automate_registration(proxy_url):
    try:
        # Set the path to the webdriver executable
        extension_path = "C:/Users/shiva/AppData/Local/Google/Chrome/User Data/Profile 1/Extensions/ndklagefmdogpfkffimjdnbnplllndic/2.0.1_0.crx"
        proxy_server_url = proxy_url

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
        driver = wiredriver.Chrome(seleniumwire_options=seleniumwire_options, options=opt)

        test = Email()
        print("\nDomain: " + test.domain)
        # Make new email address
        test.register()
        print("\nEmail Address: " + str(test.address))
        address = str(test.address)
        

        if address:
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])

            ele = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/a[1]/span')))
            ele.click()

            # Wait for the email input field to be visible
            username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div[1]/div[1]/input')))
            email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div[2]/div[1]/input')))
            password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div[3]/div[1]/input')))

            # Enter the email address into the input field
            username = address.split('@')[0]
            username_input.send_keys(username)
            email_input.send_keys(address)
            password_input.send_keys("Q!w2e3r4t5y6")
            time.sleep(10)

            checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div[4]/label/div')))
            checkbox.click()

            time.sleep(5)

            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/a/span')))
            next_button.click()

            time.sleep(5)

            confirmPassword_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/div/input')))
            confirmPassword_input.send_keys("Q!w2e3r4t5y6")

            time.sleep(1)

            next_button_final = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/div/a/span')))
            next_button_final.click()

            time.sleep(20)

            otp_messages = test.message_list()
            new_message = otp_messages[0]
            message_id = new_message['id']
           
            msg_data = test.message(message_id)

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

            #sumSubKyc 
            # Switch to the iframe using the XPath
            iframe_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sumsub-websdk-container"]/iframe')))
            driver.switch_to.frame(iframe_element)

            time.sleep(40)

            continue_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div/footer/button')))
            continue_button.click()

            time.sleep(10)

            continue_this_device_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/footer/div/button[1]/span')))
            continue_this_device_button.click()

            other_radio_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/main/fieldset/span/label[2]/label/span')))
            other_radio_button.click()

            agree_and_continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/footer/button/span')))
            agree_and_continue_button.click()

            email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div/main/input')))
            email_input.send_keys(address)

            send_verification_code_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/footer/div/button[1]/span')))
            send_verification_code_button.click()

            time.sleep(30)

            otp_messages = test.message_list()
            new_message = otp_messages[0]
            message_id = new_message['id']
            
            msg_data = test.message(message_id)

            html_content = msg_data['html']
           
            soup = BeautifulSoup(html_content[0], 'html.parser')

            # Find the OTP element by its tag and class
            otp_element = soup.find('h3')

            if otp_element:
                verification_code = otp_element.text.strip()
                print("OTP:", verification_code)
            else:
                print("OTP not found.")

            otp_input_xpath_template = '//*[@id="wrapper"]/div/main/label/input[{}]'
            otp_input_xpaths = [otp_input_xpath_template.format(i) for i in range(1, 7)]

            # Send each OTP digit to the respective input field
            for i in range(6):
                input_val = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, otp_input_xpaths[i])))
                input_val.send_keys(verification_code[i])

            input_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'SdkInput__input')))
            first_name_input = input_elements[0]
            last_name_input = input_elements[1]
            dob_input = input_elements[2]

            first_name = username.split("@")[0].split("_")[0].capitalize()
            first_name_input.send_keys(first_name)
            random_last_name = faker.last_name()
            last_name_input.send_keys(random_last_name)

            random_day = random.randint(1, 28)
            random_month = random.randint(1, 12)
            random_year = random.randint(1990, 1999)
            random_dob = f"{random_day:02d}-{random_month:02d}-{random_year:02d}"
            dob_input.send_keys(random_dob)

            continue_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/footer/div/button[1]')))
            continue_button.click()

            time.sleep(30)
            driver.switch_to.default_content()
            start_index = 1
            end_index = 6 
            seed_phrases = []

            for set_index in range(1, 3):
                for index in range(start_index, end_index + 1):
                    xpath = f'//*[@id="container"]/div[1]/div/div/div[2]/div/div[{set_index}]/div[{index}]'
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                    phrase = element.text.strip()
                    words = phrase.split('\n')[-1]
                    seed_phrases.append(words)

            next_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div/div[2]/a/span')))
            next_button.click()

           
            for i in range(1, 5):
                element = driver.find_element(by=By.XPATH, value=f'//*[@id="container"]/div[1]/div/div/div[2]/div[{i}]/p')
                xpath_value = element.text
                xpath_value = element.text
                value = int(xpath_value.split('#')[-1])
                seed_word = seed_phrases[value - 1]
               
                element_1 = driver.find_element(By.XPATH, f'//*[@id="container"]/div[1]/div/div/div[2]/div[{i}]/div/label[1]/div/span')
                element_value_1 = element_1.get_attribute('innerText')  
                
                element_2 = driver.find_element(By.XPATH, f'//*[@id="container"]/div[1]/div/div/div[2]/div[{i}]/div/label[2]/div/span')
                element_value_2 = element_2.get_attribute('innerText') 
               
                element_3 = driver.find_element(By.XPATH, f'//*[@id="container"]/div[1]/div/div/div[2]/div[{i}]/div/label[3]/div/span')
                element_value_3 = element_3.get_attribute('innerText')  
        
                if seed_word == element_value_1:
                    element_1.click()
                elif seed_word == element_value_2:
                    element_2.click()
                elif seed_word == element_value_3:
                    element_3.click()
                else:
                    print('no element')
          
            next_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div[1]/div[2]/a/span')))        
            next_button.click()
            time.sleep(1000)
            
            finish_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div[1]/div[2]/a/span')))        
            finish_button.click()

            registration_data = [
                username,
                "Q!w2e3r4t5y6",
                first_name,
                random_last_name,
                address
            ]
            write_to_csv(registration_data)
            formatted_seed_phrase = ' '.join(seed_phrases)  
            seed_phrase_data = [formatted_seed_phrase.replace(' ', ' ')]  
            write_to_csv(seed_phrase_data)
    except Exception as e:
        print(f"Error occurred: {e}")
        driver.close()
    
    
def create_threads():
    with open('proxy_links.txt', 'r') as file:
        proxy_links = file.readlines()

    # Shuffle the proxy links list to randomize the selection
    random.shuffle(proxy_links)

    # Take the first 10 proxy links
    selected_proxy_links = proxy_links[:2]

    threads = []
    for proxy_link in selected_proxy_links:
        proxy_url = proxy_link.strip()  # Remove newline characters
        thread = threading.Thread(target=automate_registration, args=(proxy_url,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Start the threads
create_threads()