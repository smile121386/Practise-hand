import requests
test_url = "https://mail.163.com/"
form_data = {}
reponses = requests.post(test_url)
print(reponses.status_code)
if reponses.status_code == 200:
    print("请求成功")
else:
    print("请求失败")