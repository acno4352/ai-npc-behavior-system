import requests

url = "http://127.0.0.1:5000/predict_npc_response"
data = {"player_id": 1, "npc_id": 2, "interaction_type": "attack"}

response = requests.post(url, json=data)
print("Response Status Code:", response.status_code)
print("Response Text:", response.text)
