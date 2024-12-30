import requests

host = 'localhost:9696'
url = f'http://{host}/predict'

customer_id = 'xyz-123'

client = {"job": "management", 
          "duration": 400, 
          "poutcome": "success"
        }

response = requests.post(url, json=client).json()
print(response)

if response['churn'] == True:
    print(f"Sending promo email to {customer_id}")
else:
    print(f'Not sending promo email to {customer_id}')

