import json
import requests
from requests.models import Response

def get_response_json(ip_adr):
    token = "xxx"
    url = "https://ipinfo.io/" + ip_adr + "?token="+token
    req = requests.get(url)
    return req.json()

def get_result_one_IP():
    ip = input("what is the IP address? : ")
    result_json = get_response_json(ip)
    result = "IP address:"+ ip + "\tHostname:"+ result_json['hostname'] + "\tCountry:" + result_json['country'] + "\tOrganisation:" + result_json['org']
    return result

def get_result_multiple_IP():
    path_file = input("Please provide full file path:")
    with open(path_file,'r') as f:
        ip_addresses = f.readlines()
    print("IP address,Country,Organisation,Hostname")
    for ip_adr in ip_addresses:
        result_json = get_response_json(ip_adr)
        result = result_json['ip'] + "," + result_json['country'] + "," + result_json['org'] + ","
        try:
            result += result_json['hostname']
        except:
            result += "N/A"
        print(result)

def get_info_threatgrid(ip_adr):
    api_key="xxx"
    url="https://panacea.threatgrid.com/api/v2/ips/" + ip_adr + "?api_key="+ api_key
    req = requests.get(url)
    print(req.json())

def main():
    print("If you want to get result for \n\ta single IP, please write ip \n\tmultiple IP, please write file")
    choise = input("Do you want to search (ip/file)?")

    if choise == "ip":
        print(get_result_one_IP())
    elif choise == "file":
        get_result_multiple_IP()
    else:
        print("there is no parameter like this " + choise)

main()
