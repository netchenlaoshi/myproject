import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'15842714306973',
    'sign':'19785bb75c1c762e6f2bc2216512357e',
    'ts':'1584271430697',
    'bv':'9ef61dc3d2f65f61d71a16bd47c6e9ee',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME'
}
response=requests.post(url,data=form_data)
print(response.text)