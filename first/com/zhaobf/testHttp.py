import requests, time

r = requests.post('http://localhost:8083/esignpro/rest/doc/save', data={
    "accountUniqueId": "test3111",
    "bizId": "12345678",
    "fileKey": "$d4020817-e6fd-4583-b583-e18b37609235$2368986772",
    "docName": "某某合同",
    "signerName": "张三",
    "redirectUrl": "http:www.test.com",
    "notifyUrl": "https://requestb.in/1eonzqb1"
})
print(r.status_code)
print(r.content)
