# Gmail Signature Editing

Author: Timothy Cuenat  
Date: 23.11.2023  
Version: 1.0.0

Bulk update and manage Google Workspace user email signatures with the Gmail API.

This project helps Google Workspace administrators standardize and automate Gmail signatures across a domain.  
Use it to apply a professional, consistent HTML signature to many users at once using data from a spreadsheet.

## Why this script?

- Save time compared to manual signature updates
- Keep company branding consistent
- Generate dynamic signatures from user data (name, role, phone, etc.)
- Automate Gmail signature deployment for Google Workspace

## Keywords

Gmail signature, Gmail API, Google Workspace, bulk signature update, email signature management, domain-wide delegation, admin automation, Python Gmail script, HTML email signature template.

## Preparation

1. Prepare the fields you want in your signature in an `.xlsx` file.
2. Prepare Google API credentials in a `.json` file (Google service account).
3. Edit the HTML template with the fields/placeholders you want to use.
4. Edit `gmail_signature_editing.py` to map your placeholders and data fields.

## Run the script

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python gmail_signature_editing.py
   ```

5. Select the `.xlsx` file containing user data.
6. Select the `.json` file containing Google API credentials.
7. Let the script update Gmail signatures.

## Typical use cases

- Roll out a new company signature format
- Update signatures after rebranding
- Apply legal disclaimers consistently
- Synchronize signatures after HR/user data changes

