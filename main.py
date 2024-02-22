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
        "ps_l": "0",
        "ps_n": "0",
        "datr": "LdHWZS9w-xH4vqYS1iqmcBDm",
        "imgn_sess": "FsbDxMKmt3cWEBgOREJUTzBWSnBmbTdKTHcW2MW23QwA",
    }

    headers = {
        "authority": "imagine.meta.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        # 'cookie': 'ps_l=0; ps_n=0; datr=LdHWZS9w-xH4vqYS1iqmcBDm; imgn_sess=FsbDxMKmt3cWEBgOREJUTzBWSnBmbTdKTHcW2MW23QwA',
        "origin": "https://imagine.meta.com",
        "referer": "https://imagine.meta.com/?prompt=color",
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
        "x-fb-lsd": "aVouI_GVDXHDkcHigzqPo-",
    }

    data = {
        "av": "262633830256867",
        "__user": "0",
        "__a": "1",
        "__req": "d",
        "__hs": "19775.HYP:comet_loggedout_pkg.2.1..0.0",
        "dpr": "1",
        "__ccg": "EXCELLENT",
        "__rev": "1011573177",
        "__s": "1cq29p:2t1kd0:ponxks",
        "__hsi": "7338282905951769975",
        "__dyn": "7xeUmwlE7ibwKBAg35xu13wqovzEdEc8co2qwJw8-0PEhwem0nCq1ewcG0KE33w8G1Qw5Mx61vw9m1YwBgao6C0Mo2sx-0z8jwae4UaEW0D888cobEaU2eU5O0HUvw4JwJwSyES0gq0Lo6-1Fw4mwr86Dwlo18o",
        "__csr": "hmkytduFt9u98i9yERd5Dm2HAQu3mUtGElnCyoSVt6zkWG8xaeyoS6Fox28LUnxSi0yEd8oCgy7poKmifzGwgC7ErCx65XzEcEhgswSxi483mAxa01rYgy9g0c3a4jw0hBo03K9yo09K805-6t1O01eTw1pYw04bO",
        "__comet_req": "1",
        "fb_dtsg": "NAcOAS1VaEdXU576JK7Amx3RLi0CuRquKkWonvC6vdsh9xWceKVqVqQ:8:1708577132",
        "jazoest": "25438",
        "lsd": "aVouI_GVDXHDkcHigzqPo-",
        "__spin_r": "1011573177",
        "__spin_b": "trunk",
        "__spin_t": "1708577132",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "useImageGenerationMutation",
        "variables": f'{{"input":{{"client_mutation_id":"1","actor_id":"203318949522501","intent":null,"prompt":"{prompt}"}}}}',
        "server_timestamps": "true",
        "doc_id": "7084728348279719",
    }

    response = requests.post(
        "https://imagine.meta.com/api/graphql/",
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)
    return json.loads(response.text)
