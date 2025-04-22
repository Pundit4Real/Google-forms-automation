import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ⏳ Delay in seconds between submissions (1.2 hours = 4320 seconds)
DELAY_BETWEEN_SUBMISSIONS = 3 * 60  # 4320 seconds

def random_age(min_age=18, max_age=35):
    return str(random.randint(min_age, max_age))

def fill_and_submit_form(form_url):
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(form_url)
        time.sleep(3)

        while True:
            # Fill the age input (first input field expected)
            input_fields = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"], input[type="number"]')
            for field in input_fields:
                try:
                    field.clear()
                    field.send_keys(random_age())
                    time.sleep(0.5)
                    break
                except:
                    continue

            # Select radio buttons
            all_questions = driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"]')
            for group in all_questions:
                options = group.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')

                if not options:
                    continue

                found_uenr = False
                for option in options:
                    try:
                        label = option.get_attribute("aria-label")
                        if label and "UENR" in label:
                            option.click()
                            found_uenr = True
                            time.sleep(0.5)
                            break
                    except:
                        continue

                if not found_uenr:
                    try:
                        random.choice(options).click()
                        time.sleep(0.5)
                    except:
                        continue

            # Try clicking "Next"
            try:
                next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]/ancestor::div[@role='button']")
                next_button.click()
                time.sleep(3)
                continue
            except:
                pass

            # Try clicking "Submit"
            try:
                submit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Submit')]/ancestor::div[@role='button']")
                submit_button.click()
                time.sleep(3)
                break
            except:
                break

    finally:
        driver.quit()

# ========== User Input ==========
form_url = input("🔗 Enter the Google Form URL: ").strip()
try:
    num_submissions = int(input("📝 Enter the number of responses to submit: ").strip())
except ValueError:
    print("❌ Please enter a valid number.")
    exit(1)

# ========== Start Scheduled Submissions ==========
for i in range(num_submissions):
    print(f"\n📤 Submitting form #{i + 1} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    fill_and_submit_form(form_url)

    if i < num_submissions - 1:
        print(f"🕐 Waiting 3 minutes before next submission...\n")
        time.sleep(DELAY_BETWEEN_SUBMISSIONS)

print("\n✅ All scheduled submissions completed.")


