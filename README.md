# Gmail Signature Editing

Author: Timothy Cuenat
Date: 23.11.2023
Version: 1.0.0

Welcome to the Gmail Signature Editing Script repository! This script is a powerful tool designed for administrators of
Google Workspace. It allows you to efficiently manage and modify the email signatures of all users within your Google
Workspace domain, streamlining the process of maintaining a consistent and professional email signature across your
organization.

## Prepare

1. Prepare the fields you want in your signature in a .xslx file.
2. Prepare the Google API credentials in a .json file (create a Google Services account).
3. Edit the HTML template with the fields you want to use in your signature.
4. Edit `gmail_signature_editing.py` with the fields you want to use in your signature.

## Script

1. Create a virtual environment (VENV):

   ```bash
   python -m venv venv
    ```
2. Activate the VENV:

   ```bash
   source venv/bin/activate
   ```
3. Install the requirements:

   ```bash
    pip install -r requirements.txt
    ```
4. Run the script:

   ```bash
    python gmail_signature_editing.py
    ```

5. Select .xslx file with data

6. Select .json file with Google API credentials

7. Enjoy!

