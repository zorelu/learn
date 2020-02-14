import http.client


conn = http.client.HTTPSConnection("s.197.com")

payload = "{\"isRememberPwd\":1,\"password\":\"666666\",\"userName\":\"77019900001\"}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "78a41b3a-537e-9f68-c9f8-89c610923ed3",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

conn.request("POST", "/web-smp/user/login/in", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

conn = http.client.HTTPSConnection("s.197.com")

payload = "{\"enableSupperMemberPrice\":1,\"categoryIds\":[403502],\"coverImage\":\"201905/15/sns/sns_btAm9QP11C0516JVQQGCHF.jpg\",\"imgTextHybr\":[{\"img\":\"201905/15/sns/sns_RKiy8FGSxE0516JVQQGMJ1.jpg\"}],\"goodsDesc\":\"\",\"imgUrls\":[],\"mainImagesUrl\":[\"201905/15/sns/sns_btAm9QP11C0516JVQQGCHF.jpg\"],\"inventory\":99999,\"isInfiniteInventory\":2,\"isSpecial\":1,\"name\":\"aaa\",\"originalPrice\":0,\"price\":600,\"type\":1,\"tagType\":null,\"moneyType\":1,\"isSupportMemberCardPay\":2,\"openProductDistributionSetting\":1,\"restrictedPurchase\":1,\"status\":1,\"openLikeAndComment\":2}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "d8a362d2-b650-5c40-12f4-0de645a880f2",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

conn.request("POST", "/web-smp/smp/org/product/add", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))