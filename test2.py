import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NUM_SUBMISSIONS = 3

def get_random_text():
    return random.choice(["Alpha", "Bravo", "Charlie", "Delta", "Echo"])

def get_random_number():
    return str(random.randint(18, 60))

def fill_dynamic_form():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://forms.gle/HLYhxzCrXkdfycfm9")
        time.sleep(3)

        while True:
            # === Fill Text/Number Fields ===
            inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"], input[type="number"]')
            for field in inputs:
                try:
                    if 'number' in field.get_attribute('type'):
                        field.send_keys(get_random_number())
                    else:
                        field.send_keys(get_random_text())
                    time.sleep(0.3)
                except:
                    continue

            # === Select One Radio Button Per Group ===
            radio_groups = driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"]')
            for group in radio_groups:
                radios = group.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
                if radios:
                    try:
                        random.choice(radios).click()
                        time.sleep(0.3)
                    except:
                        continue

            # === Check Checkboxes (Optional) ===
            checkbox_containers = driver.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]')
            if checkbox_containers:
                checkboxes_to_click = random.sample(checkbox_containers, k=random.randint(1, len(checkbox_containers)))
                for cb in checkboxes_to_click:
                    try:
                        cb.click()
                        time.sleep(0.2)
                    except:
                        continue

            time.sleep(1)

            # === Go to Next or Submit ===
            try:
                next_btn = driver.find_element(By.XPATH, '//span[text()="Next"]/ancestor::div[@role="button"]')
                next_btn.click()
                time.sleep(3)
            except:
                break  # No "Next" means we should submit

        # === Submit the Form ===
        try:
            submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]')))
            submit_btn.click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "response has been recorded")]')))
            print("✅ Form submitted successfully.")
        except Exception as e:
            print("⚠️ Submit failed:", e)

        time.sleep(2)

    except Exception as e:
        print("⚠️ Error:", e)
    finally:
        driver.quit()


# === Run Multiple Submissions ===
for i in range(NUM_SUBMISSIONS):
    print(f"\n➡️ Submitting form #{i + 1}")
    fill_dynamic_form()
    time.sleep(3)

'''
🔄 Loop through a list of real names or data,

📊 Store submission logs,

🤖 Run this on a schedule (like every hour),

🛠 Add proxy or stealth options for many entries,

'''