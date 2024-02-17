from fastapi import FastAPI
import json
from dotenv import load_dotenv
import requests

load_dotenv()

app = FastAPI(
    docs_url="/meta-image-generation/docs", redoc_url="/meta-image-generation/redoc"
)


@app.post("/generate_image")
async def generate_image(prompt: str):
    cookies = {
        "datr": "VT2PZZAcR87yY3IbaTuMWKr6",
        "imgn_sess": "FoqxmZzculwWXBgOWTE0czNKcFVFN1pyM3cW%2Fvn52AwA",
    }

    headers = {
        "authority": "imagine.meta.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.6",
        "content-type": "application/x-www-form-urlencoded",
        # 'cookie': 'datr=VT2PZZAcR87yY3IbaTuMWKr6; imgn_sess=FoqxmZzculwWXBgOWTE0czNKcFVFN1pyM3cW%2Fvn52AwA',
        "origin": "https://imagine.meta.com",
        "referer": "https://imagine.meta.com/",
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
        "x-fb-lsd": "jSaWbihHqJ_bwwR1WaLIMz",
    }

    data = {
        "av": "203318949522501",
        "__user": "0",
        "__a": "1",
        "__req": "3",
        "__hs": "19770.HYP:comet_loggedout_pkg.2.1..0.0",
        "dpr": "1",
        "__ccg": "EXCELLENT",
        "__rev": "1011497322",
        "__s": "t7scfd:b78vgx:kxfing",
        "__hsi": "7336635050907052304",
        "__dyn": "7xeUmwlE7ibwKBAg35xu13w8CewSwMwNw9G2S0zU3ex609vCwjE1xo33w8G1Qw5Mx61vw9m1YwBgao6C0Mo2sx-0z8jwae4UaEW0D888cobEaU2eU5O0HUvw4JwJwSyES0gq0Lo6-1Fw4mwr86Dwlo18o",
        "__csr": "n9pkgy9XQ9AzRiF2bpHjKUhxC8DUbbxGUqyp6uaBXohx50wz9Qmfy8xebokwZwhUdWLxGdBG4E4i2acxi7rwExK3S6E-222a1iF0h87S01uJa02_n4P004Wcg0t7w0kKU0U-1Mo04Ty07sO0",
        "__comet_req": "1",
        "fb_dtsg": "NAcNKKj2kemOmpm4r1qgMfo4kmkAlykO4EIUQIX32ZcvvIZvp0HJmNg:46:1703886463",
        "jazoest": "25600",
        "lsd": "jSaWbihHqJ_bwwR1WaLIMz",
        "__spin_r": "1011497322",
        "__spin_b": "trunk",
        "__spin_t": "1708193461",
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
    print(response.text)
    return json.loads(response.text)
