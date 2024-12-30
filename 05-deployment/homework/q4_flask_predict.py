import requests

host = 'localhost:9696'
url = f'http://{host}/predict'

customer_id = 'xyz-123'

client = {"job": "student", 
          "duration": 280, 
          "poutcome": "failure"
        }

response = requests.post(url, json=client).json()
print(response)

if response['churn'] == True:
    print(f"Sending promo email to {customer_id}")
else:
    print(f'Not sending promo email to {customer_id}')

