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
        "datr": "6BrVZSNSJBFGlEVr3FRTih0w",
        "imgn_sess": "FoqxmZzculwWEhgONUlpYjdOeGh3RnFiMXcWmOyo3QwA",
    }

    headers = {
        "authority": "imagine.meta.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        # 'cookie': 'ps_l=0; ps_n=0; datr=6BrVZSNSJBFGlEVr3FRTih0w; imgn_sess=FoqxmZzculwWEhgONUlpYjdOeGh3RnFiMXcWmOyo3QwA',
        "dpr": "2",
        "origin": "https://imagine.meta.com",
        "referer": "https://imagine.meta.com/?prompt=light",
        "sec-ch-prefers-color-scheme": "light",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "viewport-width": "414",
        "x-asbd-id": "129477",
        "x-fb-friendly-name": "useImageGenerationMutation",
        "x-fb-lsd": "kG56YOhOXo349l3BJl_pJ3",
    }

    data = {
        "av": "203318949522501",
        "__user": "0",
        "__a": "1",
        "__req": "9",
        "__hs": "19773.HYP:comet_loggedout_pkg.2.1..0.0",
        "dpr": "1.5",
        "__ccg": "EXCELLENT",
        "__rev": "1011526444",
        "__s": "isu981:cuc3f1:zqo31w",
        "__hsi": "7337800911972071563",
        "__dyn": "7xeUmwlE7ibwKBAg35xu13wqovzEdEc8co2qwJw8-0PEhwem0nCq1ewcG0KE33w8G1Qw5Mx61vw9m1YwBgao6C0Mo2sx-0z8jwae4UaEW0D888cobEaU2eU5O0HUvw4JwJwSyES0gq0Lo6-1Fw4mwr86Dwlo18o",
        "__csr": "hytetqq-lui8XXx3z9ut5y8qx2uEeax68zcxrgcogyFpm8yAeCUGbxmUhwDU6m1DBXKdG3ymEeoS26cDK2mmEb9UtwCDwi8mwxx-0R805LC324C02_4o9gO8w0i-803J-U0vcw0nMU71w0js80uayt00VQw",
        "__comet_req": "1",
        "fb_dtsg": "NAcNa0iRki9nxh9kBTBt20rh4wJ3P5hNEPVJpc8oY0ccZGyewLvuaiw:9:1708464908",
        "jazoest": "25534",
        "lsd": "kG56YOhOXo349l3BJl_pJ3",
        "__spin_r": "1011526444",
        "__spin_b": "trunk",
        "__spin_t": "1708464909",
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
