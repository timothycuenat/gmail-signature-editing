import time
from string import Template

import easygui
import pandas as pd
from google.auth.exceptions import RefreshError, TransportError
from google.oauth2 import service_account
from googleapiclient.discovery import build


def get_api_credentials(key_path):
    API_scopes = ['https://www.googleapis.com/auth/gmail.settings.basic',
                  'https://www.googleapis.com/auth/gmail.settings.sharing']
    credentials = service_account.Credentials.from_service_account_file(key_path, scopes=API_scopes)
    return credentials


def update_sig(full_name, title, email, address, phone, sig_template, credentials, live=False):
    sig = sig_template.substitute(full_name=full_name,
                                  title=title,
                                  email=email,
                                  address=address,
                                  phone=phone
                                  )
    if live:
        credentials_delegated = credentials.with_subject(email)
        gmail_service = build("gmail", "v1", credentials=credentials_delegated)
        addresses = gmail_service.users().settings().sendAs().list(userId='me',
                                                                   fields='sendAs(isPrimary,sendAsEmail)').execute().get(
            'sendAs')

        # this way of getting the primary address is copy & paste from google example
        address = None
        for address in addresses:
            if address.get('isPrimary'):
                break
        if address:
            rsp = gmail_service.users().settings().sendAs().patch(userId='me',
                                                                  sendAsEmail=address['sendAsEmail'],
                                                                  body={'signature': sig}).execute()
            print(f"    Signature changed with SUCCESS")
    else:
        print(f"    ERROR: Could not find primary address")


def main():
    # GET THE EXCEL FILE WITH THE SIGNATURES CONTENT
    excelfile = easygui.fileopenbox(msg="Please open the .xlsx file with signature",
                                    title="SIGNATURES CONTENT XLSX",
                                    filetypes=["*.xlsx"])
    if not excelfile:
        print("No signature .xlsx file selected, so stopping")
        return

    # READ THE EXCEL FILE
    user_data = pd.ExcelFile(excelfile)
    df = pd.read_excel(excelfile)

    # GET THE GOOGLE API CREDENTIALS
    key_path = easygui.fileopenbox(msg="Please open the confidential Google secret .json file",
                                   title="GOOGLE API CREDENTIALS JSON",
                                   filetypes=["*.json"])
    credentials = get_api_credentials(key_path=key_path)
    if not credentials:
        print("No credential file selected, so stopping")
        return

    # GET THE TEMPLATE FILE
    try:
        sig_file = open("html/template.html", "r")
        sig_template = Template(sig_file.read())
    except (FileNotFoundError, IOError):
        print("Could not open the template file")
        raise

    # GO THROUGH EACH ROW OF THE EXCEL FILE (EXCEPT THE FIRST ONE)
    for index, row in df.iterrows():
        first_name = row["FIRST_NAME"]
        last_name = row["LAST_NAME"]
        full_name = first_name + " " + last_name
        title = row["TITLE"]
        email = row["EMAIL"]
        address = row["ADDRESS"]
        phone = row["PHONE"]

        print(f"- Updating signature for: {email} ({full_name})")

        # MODIFY SIGNATURE
        retry_count = 0
        while retry_count < 3:
            try:
                print(f"    Trying to change signature ...")
                update_sig(full_name=full_name,
                           title=title,
                           email=email,
                           address=address,
                           phone=phone,
                           sig_template=sig_template,
                           credentials=credentials,
                           live=True)
                break
            except (RefreshError, TransportError) as e:
                retry_count += 1
                print(f"  ERROR: encountered retrying (attempt {retry_count}). Error was: {e}")
                time.sleep(2)
                continue
            except Exception as e:
                raise


if __name__ == '__main__':
    print('| Author: Timothy Cuenat | Date: 23.11.2023 | Version: 1.0.0 |')
    print('--- Google Workspace Signature Script ---')
    main()
    print('--- Script finished ---')
