import json
import requests

def get_info_threatgrid(ip_adr):
    api_key="a4eo1p4d7g5jlqn33ts0mapr8i"
    url="https://panacea.threatgrid.com/api/v2/iocs/feeds/ips?ip="+ip_adr+"&api_key="+ api_key
    req = requests.get(url)
    return req.json()


info = get_info_threatgrid('92.53.68.202')
print(info.get("items")[0].get("sample_id"))