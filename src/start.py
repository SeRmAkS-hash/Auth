import requests

def req_to_api():
    headers = {'authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJqdGkiOiJlYjBmMTUzZC04M2MxLTQyOGEtOTIyYy05MDM0NjMxZTJkZDEiLCJ0eXBlIjoiYWNjZXNzIiwiZnJlc2giOmZhbHNlLCJjc3JmIjoiIiwiaWF0IjoxNzgwMzM1NzA4LCJleHAiOjE3ODAzMzY2MDguNjIyOTI2fQ.eJB7gG0bQ-WgT0x0i2AnudwQRUG5EdknDfPfV0fwBuU '}
    responce = requests.get(url='http://127.0.0.1:8000/Test/endpoint',headers=headers)
    print(responce.status_code)
    print(responce.json())
    
req_to_api()