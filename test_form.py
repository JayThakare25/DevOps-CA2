import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class TestStudentFeedbackForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup Chrome driver (ensure Chrome is installed on your system)
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless') # Uncomment if you want tests to run headlessly
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        # Get absolute path of the index.html
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cls.file_url = f"file:///{current_dir}/index.html"
        
        cls.driver.get(cls.file_url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Wait a bit before closing down
        time.sleep(2)
        cls.driver.quit()

    def setUp(self):
        # Refresh the page before each test string to start clean
        self.driver.get(self.file_url)
        time.sleep(1) # wait for page to render

    def test_01_page_opens_successfully(self):
        # Check whether the form page opens successfully
        self.assertIn("Student Feedback Registration Form", self.driver.title)
        form_element = self.driver.find_element(By.ID, "feedbackForm")
        self.assertTrue(form_element.is_displayed())

    def test_02_valid_data_submission(self):
        # Enter valid data and verify successful submission
        self.driver.find_element(By.ID, "studentName").send_keys("John Doe")
        self.driver.find_element(By.ID, "emailId").send_keys("johndoe@example.com")
        self.driver.find_element(By.ID, "mobileNumber").send_keys("1234567890")
        
        # Dropdown
        department_select = Select(self.driver.find_element(By.ID, "department"))
        department_select.select_by_value("CS")
        
        # Radio button
        self.driver.find_element(By.ID, "genderMale").click()
        
        # Textarea (min 10 words)
        self.driver.find_element(By.ID, "feedbackComments").send_keys("This is a feedback comment that definitely has more than ten distinct words in it.")
        
        # Submit
        self.driver.find_element(By.ID, "submitBtn").click()
        
        # Check success message
        success_msg = self.driver.find_element(By.ID, "successMessage")
        self.assertFalse("hidden" in success_msg.get_attribute("class"))
        self.assertIn("Form submitted successfully", success_msg.text)

    def test_03_mandatory_fields_blank(self):
        # Leave mandatory fields blank and check error messages
        self.driver.find_element(By.ID, "submitBtn").click()
        
        name_err = self.driver.find_element(By.ID, "error-studentName").text
        email_err = self.driver.find_element(By.ID, "error-emailId").text
        
        self.assertEqual("Student Name cannot be empty.", name_err)
        self.assertEqual("Please enter a valid Email ID.", email_err)

    def test_04_invalid_email_format(self):
        # Enter invalid email format and verify validation
        self.driver.find_element(By.ID, "emailId").send_keys("invalid-email")
        self.driver.find_element(By.ID, "submitBtn").click()
        
        email_err = self.driver.find_element(By.ID, "error-emailId").text
        self.assertEqual("Please enter a valid Email ID.", email_err)

    def test_05_invalid_mobile_number(self):
        # Enter invalid mobile number and verify validation
        self.driver.find_element(By.ID, "mobileNumber").send_keys("12345")
        self.driver.find_element(By.ID, "submitBtn").click()
        
        mobile_err = self.driver.find_element(By.ID, "error-mobileNumber").text
        self.assertEqual("Mobile Number must be exactly 10 digits.", mobile_err)

    def test_06_dropdown_selection_works(self):
        # Check whether dropdown selection works properly
        department_select = Select(self.driver.find_element(By.ID, "department"))
        department_select.select_by_value("IT")
        
        selected_option = department_select.first_selected_option
        self.assertEqual("Information Technology", selected_option.text)

    def test_07_buttons_work_correctly(self):
        # Check whether buttons such as Submit and Reset work correctly
        # Fill some data
        name_field = self.driver.find_element(By.ID, "studentName")
        name_field.send_keys("Jane Doe")
        
        # Reset
        self.driver.find_element(By.ID, "resetBtn").click()
        
        # Verify it's empty
        self.assertEqual("", name_field.get_attribute("value"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
