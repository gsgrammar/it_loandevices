from django.shortcuts import render
import requests
import datetime
from .config import auth_token, api_url

header = {'Authorization': f'Bearer {auth_token}'}
url = api_url + "/api/v1/hardware?search=Loan&sort=name&order=asc"

def home(request):
    loan_devices=[]
    response = requests.get(url,headers=header)
    response_time = response.headers['Date']
    response_json = (response.json()['rows'])
    for x in response_json:
        device_status = (x['status_label']['status_meta'])
        if  device_status == "deployed":
            asset_name = str(x['name'])
            loan_number = asset_name.replace("Loan Device ","")
            date_obj = datetime.datetime.strptime(str(x['last_checkout']['datetime']), '%Y-%m-%d %H:%M:%S')
            checked_out_date = date_obj.strftime("%d/%m")
            checked_out_to = str(x['assigned_to']['name'])
            current_date = datetime.datetime.now()
            loan_date_date_difference = current_date-date_obj
            device_info = [loan_number, checked_out_date, checked_out_to,loan_date_date_difference.days]
            loan_devices.append(device_info)
        else:
            asset_name = str(x['name'])
            loan_number = asset_name.replace("Loan Device ","")
            checked_out_date = ''
            checked_out_to = ''
            loan_date_date_difference = '-1'
            device_info = [loan_number, checked_out_date, checked_out_to,loan_date_date_difference]
            loan_devices.append(device_info)
    return render(request, 'home.html', {
        'data' : loan_devices,
        'date' : response_time
    }
    )