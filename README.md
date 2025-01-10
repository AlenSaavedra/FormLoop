# FormLoop  
Automate Google Forms effortlessly with Python and Selenium. FormLoop fills and submits forms automatically, saving time and effort while avoiding repetitive tasks.

## Features  
- Uses Selenium WebDriver for robust form automation.  
- Supports dynamic form interactions and multiple-choice questions.  
- Loop-based execution to fill forms multiple times.  

## Requirements  
- Python 3.x  
- `selenium` library  
- `webdriver_manager` library  

## Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/AlenSaavedra/FormLoop.git
   cd FormLoop
   ```  
2. Install the required dependencies:  
   ```bash
   pip install selenium webdriver-manager
   ```  

3. Download the appropriate browser driver if needed.  

## Usage  
1. Open `automate_google_form.py` and customize the `rsp` list with your answers.  
2. Run the script:  
   ```bash
   python automate_google_form.py
   ```  

The script will complete and submit the form 10 times automatically.

## Disclaimer  
Use this tool responsibly and ensure compliance with any terms of service of the platforms you automate.  

---
