import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.amazon.com"


headers = {
  "authority": "www.amazon.com", 
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" ,
  "accept-language": "en-US,en;q=0.9" ,
  "cache-control": "max-age=0" ,
  "cookie": """ubid-main=130-3567748-2864429; i18n-prefs=USD; av-timezone=Africa/Nairobi; session-id=138-3868414-1014621; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1647260459939-26528.37_0; sst-main=Sst1|PQF1oNypqYZNVAWDQmF5du6nCSge2-TmpoyBcyV8bQ32n4lHrxoKiFtFNq3au_vSLldmuLR0ArpLu4xkIz7VcCDRXr6idJWlWIO2jgxBEl7piGUPr7-SfkOg268hZxg9WXGhOmz_csfkyFUGi9iGycsVE7sp6BUVYHCZ3DVsccl_YeIJnyvOlNeGTge1RedZFycijx2Z3bEd4hob_R2Png-wiGEOfcsJbRuL53tohcyTcpuVivvmE76emiGN_2FCvGXnZrzO2-ASsuXs6O_ebAjlJVAjber8LrerSnAEXDjNmLo; aws-ubid-main=316-5680151-0875684; aws-session-id=146-7413967-8842521; regStatus=registered; at-main=Atza|IwEBIJ059QSBO7D6N5Bz-XW5J7ZDcngrSCRQTc8A1d0dSU-vRMFqj8e1Av6eikikhifv_-Yz4Pz2ETXxAqxLqxwptPPLcxlO4RbyI0gaS5YpUy1AheMD4ReRmbZt5ZcCxl5I-CZzrGQM-mnVWxI62hVcSOWUJsSgS-h8ZL1PmIPiiBxqienGSjrsykJKOD6usOdYG-_YAVrMsVY2Sa6rfIzFno3H; sess-at-main=\"JjJCY0zMStjJ4O3iYUQXN8rk1EJ7N0HK2ZWFV0TVd2U=\"; session-id-time=2082787201l; aws-analysis-id=146-7413967-8842521; _mkto_trk=id:112-TZM-766&token:_mch-aws.amazon.com-1647260464027-29955; __utma=194891197.1412423239.1651950124.1661647979.1662748330.15; __utmz=194891197.1662748330.15.14.utmccn=(referral)|utmcsr=us-east-1.console.aws.amazon.com|utmcct=/|utmcmd=referral; aws-session-id-time=2293468530l; aws-session-token=EmjWBxIS3HAIqJ66h+UwSId6Nk674NsH3sg9s5sDarLhXGd9ED9f2CUxb2K5gfMNGcfUhfHueSNEt3Zlno2W6wjWzfJLqm+M2Gngl0+A6q7iyoTwFgGR9Pto7yJ0w58wItmy3TNpFCPZOC/La+VFOPvy0aVeKJDn7dhsfAaoOUFyDzWMyTdIcRGAjwtZTl9Z2NhvOnoI9CFJUZkyc33O36HT06ZIhTgWNX7ka8IHEWNkRgqEVF/7ownMA8ieevO9; aws-x-main=\"Yg@M5X4kmwuhXmplIl0Ms@@fBhLyKdiYOMQ9?DbLQuLqNbaL5ucVx1381CG3itMp\"; aws-at-main=Atza|IwEBIPtclinLy6lnfndOXCbgSa1D5XLYjMIaTjKQn3sl1v4RucBshfnjuaGtrpIvjY2jCOn4x8haSsrO0WpPKFPNpS-EpQ5_mmDDlV6oJ5x0-h99KYmltDwDWv_VHPiZMn4v4DL2rL8TCJfMp9ObwIHyAVY4sDAeORuy38s3Iv4mF1G5ii9KOALagQw2pHjAubYVVsZw88TuHoMgWnQ5AuB6T6WxuLMkL4qTI1wO78IGbWh-Kpq4PtmRrQm6IsOhlYE1qlE; sess-aws-at-main=\"tQE7Nbsa+tCqWhZ1HLvlWVPNiNbqUDrsldIfA0RT1KQ=\"; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A255643351814%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22tumuhirwe%2520iden%22%2C%22keybase%22%3A%22ee1si9IDBtl9rmvyEB7QplVvceXNc9bMcy2nKa%2FzwVc%5Cu003d%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6ImFmY2M3ZGEzLWQyNWMtNGNmMC04ZTdkLWEzOGMyOTlhNTUxNSJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cHM6XC9cL3d3dy5hbWF6b24uY29tXC9hcFwvc2lnbmluIiwia2V5YmFzZSI6ImVlMXNpOUlEQnRsOXJtdnlFQjdRcGxWdmNlWE5jOWJNY3kybkthXC96d1ZjPSIsImFybiI6ImFybjphd3M6aWFtOjoyNTU2NDMzNTE4MTQ6cm9vdCIsInVzZXJuYW1lIjoidHVtdWhpcndlJTIwaWRlbiJ9.-w1M8GbLZcLd7vmitqxKIrwP61CocBz0l0He6cmuyggeAO4Cl2gIkvhOgwcWKfAh6myCHu0zmhDiY_uK60R9C4Mv_DJ6T2umPwUqFewr2f4UG8pqwjRHkPX2tqKgI7hH; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19245%7CMCMID%7C36909720565670673730489826915289737865%7CMCAID%7CNONE%7CMCOPTOUT-1662756718s%7CNONE%7CvVersion%7C4.4.0; sp-cdn=\"L5Z9:MU\"; lc-main=en_US; skin=noskin; session-token=j8DCOgBKC9bfmUegYUc2H21kKGR9KVwRJmIJAprBDFlvlxR3TwklodOMrXRA0zjLkvhLxMaWCFxXSD42xo4MZT7kXGzXGYem7qbyW9t4icpt8ZFGSPmqRv8RfEG3juZZLOTVR6ttWj5U1M2c8j7Deo6SRGHFxcOrxBrQ0uMsmN5azRi6a5PvnxiA9YsaKwlsY+xf+XJrHNEODImRkqCXrOwxOiW+3eq+; csm-hit=adb:adblk_no&t:1665675934737&tb:5STYN3A793N9MK52A43S+s-SDRDZ9T2BQY4K6D608Z5|1665675934736""" ,
  "device-memory": "8" ,
  "downlink": "0.75", 
  "dpr": "1" ,
  "ect": "3g" ,
  "rtt": "700" ,
  "sec-ch-device-memory": "8" ,
  "sec-ch-dpr": "1", 
  "sec-ch-ua": """"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99\"""", 
  "sec-ch-ua-mobile": "?0", 
  "sec-ch-ua-platform": "Windows\"", 
  "sec-ch-viewport-width": "1600",
  "sec-fetch-dest": "document", 
  "sec-fetch-mode": "navigate", 
  "sec-fetch-site": "none", 
  "sec-fetch-user": "?1", 
  "upgrade-insecure-requests": "1",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42", 
  "viewport-width": "1600" 
}

search_term = input("Which product do you want to search for? ")

url = base_url + "/s?k=" + search_term.replace(" ", "+")
# chrome book => chrome+book

amazon_products = {}

r = requests.get(url, headers=headers).text

doc = BeautifulSoup(r, "html.parser")

products = doc.find_all("div", class_="s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border")

for product in products:
    image = product.find("img", class_="s-image")["src"]
    title = product.find("span", class_="a-size-medium a-color-base a-text-normal").text
    num_reviews = product.find("span", class_="a-size-base s-underline-text").text
    price = product.find('span', class_="a-offscreen").text
    link = product.find("a", class_ = "a-link-normal")['href']
    link = base_url + link
    
    amazon_products[title] = {
        "image": image,
        "title": title,
        "num_reviews": num_reviews,
        "price": price,
        "link": link
    }


with open("amazon_products.json", "w") as file:
    json.dump(amazon_products, file, indent=4)

print("Done")