import boto3
import json
import requests
import xmltodict
import cgi
import os
import sys
import subprocess
import time

documentName = "/root/Kubernetes-Python-CGI/Files/" + sys.argv[1]

cmd = "sudo chown apache:apache " + documentName
subprocess.getoutput(cmd)

num = ""

def get_vehicle_info(plate_number):
    r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=mohit_jangir".format(str(plate_number)))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    data_final = json.loads(jdata)
    data_print = json.loads(data_final['Vehicle']['vehicleJson'])
    return (data_print)


with open(documentName, 'rb') as document:
    imageBytes = bytearray(document.read())



# os.environ['AWS_PROFILE'] = "default"

# textract = boto3.client('textract', region_name='us-east-1')

# response = textract.detect_document_text(Document={'Bytes': imageBytes})

# for item in response["Blocks"]:
#     if item["BlockType"] == "LINE" and item["Confidence"]>=95 and len(item["Text"]) >= 7:
#         num = item["Text"]
#         print(num)



# result = get_vehicle_info(num)

details  = {'Description': 'MARUTI SUZUKI INDIA LTD / SWIFT ZXI ', 'RegistrationYear': '2018', 'CarMake': {'CurrentTextValue': 'MARUTI SUZUKI INDIA LTD'}, 'CarModel': {'CurrentTextValue': 'SWIFT ZXI'}, 'MakeDescription': {'CurrentTextValue': 'MARUTI SUZUKI INDIA LTD'}, 'ModelDescription': {'CurrentTextValue': 'SWIFT ZXI'}, 'VechileIdentificationNumber': 'MBHCZC63SHL10000', 'EngineNumber': 'K12MN20XXXXX', 'FuelType': {'CurrentTextValue': 'PETROL'}, 'RegistrationDate': '03/01/2018', 'Owner': 'MARUTI SUZUKI INDIA LIMITED', 'Fitness': '02-Jan-2033', 'Insurance': '03-Dec-2018', 'Location': 'RLA, GURGAON', 'ImageUrl': 'http://in.carregistrationapi.com/image.aspx/@TUFSVVRJIFNVWlVLSSBJTkRJQSBMVEQgLyBTV0lGVCBaWEkg'}

value = details.items()

result = ""

for i in value:
    if 'ImageUrl' not in i[0]:
        if type(i[1]) is dict:
            result += str(i[0] + " : " + i[1]['CurrentTextValue']) + "<br />"
        else:
            result += str(i[0] + " : " + i[1]) + "<br />"

text =f'''#!/usr/bin/python3

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

print("{result}")
'''

f = open("/var/www/cgi-bin/test.py", "w")
f.write(text)
f.close()