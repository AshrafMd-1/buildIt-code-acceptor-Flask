import requests
import json


def get_answers(session, qid):
    url = "http://13.234.234.30:5000/submissions/user/21951a6612/"+qid
    headers = {
        "authorization": session.cookies['token'],
        "content-type": "application/json"}
    response = requests.get(i, headers=headers)
    ans = json.loads(response.text)
    for j in ans:
        if j['score'] == 100 and j['languageId'] == 34:
            return str(j['sourceCode'])
