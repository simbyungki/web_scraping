import urllib.request


url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSilvTrade?serviceKey=pTq6xkPfF5sUADVpWj2H6tVmhiwQZdT1%2FdneZjnMZUWg7F7IO1KvuyQyZynSlhAF568pUCgy2xaYzDUhhaQTxA%3D%3D&LAWD_CD=28260&DEAL_YMD=202009&'

request = urllib.request.Request(url)
request.get_method = 'GET'
response_body = urllib.request.urlopen(url).read()
print(response_body)