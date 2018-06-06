import threading
import requests

def run(x, y):
    url = "http://127.0.0.1:8084/service/rest/seal/list"

    querystring = {"page": "1", "pageSize": "5", "sealType": "1", "showWithoutProcessTemplate": "true",
                   "source": "dingding", "orgAccountUid": "2A4C492FF38F441BAAA49FDFDF19C265",
                   "accountUid": "195EC32202454D3598F2326955F40F03", "token": "6c58029c-5ade-4271-99ea-3979d7b52424",
                   "equipId": "ding195bd6618-bb87-49a6-8430-b8a64a665df5"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "11431bdf-01e8-86ff-f889-7b38f98114d6"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

for num in range(1, 10):¡
    t1 = threading.Thread(target=run, args=(15, 20))
    t1.start()
#
# for num in range(1, 10):
#     print  num
