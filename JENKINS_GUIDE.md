# Jenkins Setup & Execution Guide

This document will walk you through Sub Task 5: Use of Jenkins to automate the execution of the Selenium tests we just created.

## 1. Install Jenkins
If you haven't installed Jenkins yet, follow these steps:
1. Download Jenkins for Windows from the official site: [Jenkins Download](https://www.jenkins.io/download/)
2. Run the installer and complete the setup wizard.
3. Open a browser and navigate to `http://localhost:8080`.
4. Fetch the initial admin password from `C:\Program Files\Jenkins\secrets\initialAdminPassword` (or wherever it was installed) to unlock Jenkins.
5. Install suggested plugins and create your first admin user.

## 2. Create a Simple Jenkins Job
1. From the Jenkins dashboard, click on **New Item**.
2. Enter a project name (e.g., `Student_Feedback_Form_Tests`).
3. Select **Freestyle project** and click **OK** (or select **Pipeline** if you prefer to use the Jenkinsfile in this repo).

## 3. Connect the Project Folder (or GitHub)
If running this locally:
1. In the job configuration page, go to the **General** tab.
2. Click on **Advanced...**.
3. Check the box **Use custom workspace**.
4. In the **Directory** field, enter your absolute project path where this repo is checked out.

*(Optional) If using GitHub: Select "Git" under "Source Code Management" and paste your Repository URL.*

## 4. Configure the Job to Run Selenium Test Scripts
1. Scroll down to the **Build Steps** section.
2. Click on **Add build step** -> **Execute Windows batch command**.
3. Enter the following commands to activate the Python environment and run the tests:

```bat
@echo off
echo "Installing Dependencies"
python -m venv venv
call .\venv\Scripts\activate.bat
pip install -r requirements.txt

echo "Running Selenium Automation Tests"
pytest -v test_form.py
```

## 5. Execute the Job
1. Click **Save** at the bottom of the configuration page.
2. You will be taken back to the job dashboard. Click on **Build Now** on the left menu.
3. A new build will appear under **Build History**.

## 6. Observe the Build Status
1. Click on the build number, then click on **Console Output**.
2. You will see Jenkins creating the virtual environment, installing dependencies, and running `test_form.py`.
3. If all tests pass, the console output will say `SUCCESS`.
