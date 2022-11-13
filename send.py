#!/usr/bin/env python3

import requests

token = '2o2FhNoEyaecySH1e13RMPDtItbCb3FIiqo4VYWo1cT'
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

# 修改為你要傳送的訊息內容
message = 'Notify from LINE, HELLO WORLD'
# 修改為你的權杖內容

lineNotifyMessage(token, message)
