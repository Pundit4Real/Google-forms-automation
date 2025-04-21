# 📝 Google Forms Auto-Filler Bot

This Python script automatically fills and submits any Google Form based on dynamic detection of form fields like input boxes, radio buttons, checkboxes, dropdowns, etc.

## 🚀 Features

- Supports **any** Google Form.
- Dynamically identifies:
  - Text/number input fields (e.g., age)
  - Radio button groups
  - Checkboxes
  - Drop-downs
- Randomized responses to simulate human input
- Supports multiple submissions
- Schedules each submission at **5-minute intervals**
- Works with latest versions of **Google Chrome** and **Selenium WebDriver**
- Converts easily to `.exe` for non-Python users

---

## 📦 Requirements

- Python 3.8+
- Google Chrome
- ChromeDriver (compatible with your Chrome version)


## 2. Install Required Python Packages

Make sure you have Python installed, then run:

```bash
pip install selenium

## ▶️ How to Use

Run the script from your terminal or command prompt:

```bash
python google_form_filler.py

### 🛠️ When Prompted:

- Paste the **Google Form URL**
- Enter the **number of responses** you want to submit

---

### ✅ The Script Will:

- Open the form in a browser
- Automatically fill in fields with randomized data
- Randomly select radio buttons, checkboxes, dropdowns
- Wait **5 minutes** between each form submission

### 💻 Convert Script to .exe (For Windows Users)

If you'd like to share the script or use it on a system without Python installed:

---

#### 🧱 Step 1: Install `pyinstaller`

```bash
pip install pyinstaller

#### 🔁 Step 2: Convert the Script

```bash
pyinstaller --onefile --noconsole google_form_filler.py

#### 📂 Step 3: Locate Your Executable
- Your .exe file will be available in the dist/ folder:

        dist/
        └── google_form_filler.exe

✅ Now you can run the executable directly without needing Python!