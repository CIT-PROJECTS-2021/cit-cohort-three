import requests
import json

base_url = """https://www.coinbase.com/graphql/query?&operationName=HomeLegacyPricesQuery&extensions={"persistedQuery":{"version":1,"sha256Hash":"2f77431d0e793d9ccce6196a3666349732cba3013326b10b58918480a0bc9cd0"}}&variables={"currency":"UGX","skip":false}"""


headers = {
  "sec-ch-ua": """Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99""",
  "X-CB-Device-ID": "334ef20e-c856-43a0-b0ad-9a549e625e6c" ,
  "X-CB-Project-Name": "consumer" ,
  "Accept-Language": "en",
  "X-CB-Is-Logged-In": "false",
  "X-CB-Platform": "web" ,
  "CB-CLIENT": "CoinbaseWeb" ,
  "X-CB-Session-UUID": "26bd4685-4229-4aff-91e2-2cc3f019d4fb" ,
  "X-CB-Pagekey": "homepage" ,
  "X-CB-Version-Name": "5c8dad047b22dd8a5531ea6f6c76a304b2f1a59b" ,
  "sec-ch-ua-platform": "Windows" ,
  "redirect": "follow" ,
  "sec-ch-ua-mobile": "?0" ,
  "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42""" ,
  "credentials": "same-origin" ,
  "Content-Type": "application/json" ,
  "Accept": "application/json" ,
  "Referer": "https://www.coinbase.com/"
}

r = requests.get(base_url, headers=headers)
data = r.json()

with open('crypto_data.json', 'w') as f:
    json.dump(data, f)

print("Done")