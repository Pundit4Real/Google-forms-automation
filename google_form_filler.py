import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Wait 5 minutes between submissions
DELAY_BETWEEN_SUBMISSIONS = 5 * 60  

# Sample random data
sample_texts = ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan', 'Test', 'Sample']
sample_numbers = list(range(18, 36))

def random_age():
    return str(random.choice(sample_numbers))

def random_text():
    return random.choice(sample_texts)

def fill_and_submit_form(form_url):
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(form_url)
        time.sleep(3)

        while True:
            # Fill text/number inputs
            text_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"], input[type="number"]')
            for field in text_inputs:
                try:
                    field_type = field.get_attribute("type")
                    field.clear()
                    field.send_keys(random_age() if field_type == "number" else random_text())
                    time.sleep(0.5)
                except:
                    continue

            # Fill dropdowns
            dropdowns = driver.find_elements(By.CSS_SELECTOR, 'div[role="listbox"]')
            for dropdown in dropdowns:
                try:
                    dropdown.click()
                    time.sleep(0.5)
                    options_list = driver.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
                    if options_list:
                        random.choice(options_list).click()
                        time.sleep(0.5)
                except:
                    continue

            # Select checkboxes (random one or two)
            checkbox_groups = driver.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]')
            random.shuffle(checkbox_groups)
            for checkbox in checkbox_groups[:random.randint(1, 2)]:
                try:
                    checkbox.click()
                    time.sleep(0.5)
                except:
                    continue

            # Select radio buttons
            radio_groups = driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"]')
            for group in radio_groups:
                radios = group.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
                if radios:
                    try:
                        random.choice(radios).click()
                        time.sleep(0.5)
                    except:
                        continue

            # Click Next if available
            try:
                next_btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]/ancestor::div[@role='button']")
                next_btn.click()
                time.sleep(3)
                continue
            except:
                pass

            # Click Submit
            try:
                submit_btn = driver.find_element(By.XPATH, "//span[contains(text(), 'Submit')]/ancestor::div[@role='button']")
                submit_btn.click()
                time.sleep(5)
                break
            except:
                break

    finally:
        driver.quit()

# ========== USER INPUT ==========
form_url = input("🔗 Enter the Google Form URL: ").strip()
try:
    num_submissions = int(input("📝 Enter the number of responses to submit: ").strip())
except ValueError:
    print("❌ Please enter a valid number.")
    exit(1)

# ========== MAIN LOOP ==========
for i in range(num_submissions):
    print(f"\n📤 Submitting form #{i + 1} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    fill_and_submit_form(form_url)

    if i < num_submissions - 1:
        print(f"⏳ Waiting 5 minutes before the next submission...\n")
        time.sleep(DELAY_BETWEEN_SUBMISSIONS)

print("\n✅ All form submissions completed.")
