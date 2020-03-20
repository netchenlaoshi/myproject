import requests


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i':'我和你都是中国',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'15846848803956',
    'sign':'b1537e6e7d4296b0145432358da1fce0',
    'ts':'1584684880395',
    'bv':'9ef61dc3d2f65f61d71a16bd47c6e9ee',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)

