import gspread
from constants import GOOGLESHEET_ID, GOOGLESHEET_WORKSHEETNAME, GOOGLESHEET_CREDENTIALS_FILE
from oauth2client.service_account import ServiceAccountCredentials

def append_to_google_sheet(data,spreadsheet_id=GOOGLESHEET_ID, worksheet_name=GOOGLESHEET_WORKSHEETNAME):
     # Use the JSON key you downloaded to authenticate and create an API client
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLESHEET_CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(spreadsheet_id).worksheet(worksheet_name)
    # Append the data
    for row in data:
        dataToInsert = [row,False]
        sheet.append_row(dataToInsert)

def test_gsheet():
    data = [
        ['hello',False]
    ]
    append_to_google_sheet(data)