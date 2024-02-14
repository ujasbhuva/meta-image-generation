from fastapi import FastAPI
import json
from dotenv import load_dotenv
import requests

load_dotenv()

app = FastAPI(docs_url="/meta-image-generation/docs", redoc_url="/meta-image-generation/redoc")


@app.post("/generate_image")
async def generate_image(
    prompt: str
):
    cookies = {
        "datr": "VT2PZZAcR87yY3IbaTuMWKr6",
        "imgn_sess": "FoqxmZzculwWXBgOWTE0czNKcFVFN1pyM3cW%2Fvn52AwA",
    }

    headers = {
        "authority": "imagine.meta.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        # 'cookie': 'datr=VT2PZZAcR87yY3IbaTuMWKr6; imgn_sess=FoqxmZzculwWXBgOWTE0czNKcFVFN1pyM3cW%2Fvn52AwA',
        "origin": "https://imagine.meta.com",
        "referer": "https://imagine.meta.com/?prompt=A+volcano+explosion+spewing+molten+lava+over+snow-covered+mountains%2C+thunderous+storm+clouds+above+inner+illumated+by+lightning%2C+an+epic+fantasy+scene%2C+cinematic+lighting%2C+moody%2C+vibrant+--ar+4%3A7+--c+77+--s+777+--v+4",
        "sec-ch-ua": '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"macOS"',
        "sec-ch-ua-platform-version": '"14.1.1"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "x-asbd-id": "129477",
        "x-fb-friendly-name": "useImageGenerationMutation",
        "x-fb-lsd": "krvLA8AtvJvASP96VtzEQM",
    }

    data = {
        "av": "203318949522501",
        "__user": "0",
        "__a": "1",
        "__req": "2",
        "__hs": "19767.HYP:comet_loggedout_pkg.2.1..0.0",
        "dpr": "1",
        "__ccg": "UNKNOWN",
        "__rev": "1011397866",
        "__s": "mhlhub:ykiwt5:y0eq2y",
        "__hsi": "7335244924119878535",
        "__dyn": "7xeUmwlE7ibwKBAg35xu13w8CewSwMwNw9G2S0zU3ex609vCwjE1xo33w8G1Qw5Mx61vw9m1YwBgao6C0Mo2sx-0z8jwae4UaEW0D888cobEaU2eU5O0HUvw4JwJwSyES0gq0Lo6-1Fw4mwr86Dwlo18o",
        "__csr": "qcuLbpp9kl6V-qhfKVpV8-4Ey4u2qcxd3EjBgvKmiu4-anAKiq8gO4oqUx0zwHx611U4G9x2cxa6FU8A5Ehxu13xLxem9yEkwUwEwMw-wXwcG01Hac07Ysi1Ww5Zg1w87B004D6g08uo06mCElBw0mqE1AJw",
        "__comet_req": "1",
        "fb_dtsg": "NAcMLeDoJExC0oh0wlmusmuKkC2Wcwm35lfXE-JJnfl1WM2ccs2YC_g:46:1703886463",
        "jazoest": "25535",
        "lsd": "krvLA8AtvJvASP96VtzEQM",
        "__spin_r": "1011397866",
        "__spin_b": "trunk",
        "__spin_t": "1707869797",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "useImageGenerationMutation",
        "variables": f'{{"input":{{"client_mutation_id":"1","actor_id":"203318949522501","intent":null,"prompt":"{prompt}"}}}}',
        "server_timestamps": "true",
        "doc_id": "7168009043236766",
    }

    response = requests.post(
        "https://imagine.meta.com/api/graphql/",
        cookies=cookies,
        headers=headers,
        data=data,
    )

    return json.loads(response.text)
