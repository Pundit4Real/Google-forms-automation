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



## ⚙️ Setup Instructions

### 1. Clone the Project (or download the script)

```bash
git clone https://github.com/yourusername/google-form-filler.git
cd google-form-filler
```
### 2. Create and Activate a Virtual Environment

- For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
- For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Required Python Packages

- Instead of installing individual packages manually, you can install all dependencies listed in the requirements.txt file.

```bash
pip install -r requirements.txt
```

## ▶️ How to Use

Run the script from your terminal or command prompt:

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
```
#### 🔁 Step 2: Convert the Script

```bash
pyinstaller --onefile --noconsole google_form_filler.py
```

#### 📂 Step 3: Locate Your Executable
- Your .exe file will be available in the dist/ folder:

        dist/
        └── google_form_filler.exe

✅ Now you can run the executable directly without needing Python!

✅ **Notes**

- Works best with Google Forms that don’t require login or CAPTCHA.
- Handles most field types automatically.
- For advanced customization (e.g., specific answers to questions), the script can be extended easily.

🧠 **License & Contribution**

This project is free and open-source. Feel free to fork it, submit issues, or open pull requests.

Made with ❤️ using Python + Selenium
