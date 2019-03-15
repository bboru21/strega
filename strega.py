from bs4 import BeautifulSoup
import json
import requests

# from mock_markup import VA_ABC_HTML

# def logger(msg):
#     log_file = open('log.txt', 'w+')
#     log_file.write('%s\n' % msg)
#     log_file.close()

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

urls = [
    'https://www.abc.virginia.gov/products/vermouth/martini--rossi-extra-dry-vermouth#/product?productSize=1',
    'https://www.abc.virginia.gov/products/vermouth/martini--rossi-rosso-sweet-vermouth#/product?productSize=2',
    'https://www.abc.virginia.gov/products/cordials/liquore-strega#/product?productSize=0',
    'https://www.abc.virginia.gov/products/cordials/baileys-original-irish-cream#/product?productSize=4',
    'https://www.abc.virginia.gov/products/cordials/grand-marnier#/product?productSize=4',
    'https://www.abc.virginia.gov/products/virginia-spirits/tullamore-dew-irish-whiskey#/product?productSize=3',
    'https://www.abc.virginia.gov/products/cordials/cointreau#/product?productSize=3',
    'https://www.abc.virginia.gov/products/cordials/frangelico#/product?productSize=1',
]

best_values = []

def get_price_per_liter(amount, unit, price):
    if unit == 'ml':
        amount = amount/1000
    return round(price/amount, 2)


for url in urls:

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find("div", id="productData")["data-skus"]
    products = json.loads(data)

    if products:
        best_value = None
        for p in products:
            size = p.get("size")
            size = size.split(' ')
            amount = float(size[0])
            unit = size[1]

            price = p.get("currentPrice")

            p['pricePerLiter'] = get_price_per_liter(amount, unit, price)

            if not best_value or (p.get('pricePerLiter') < best_value.get('pricePerLiter')):
                best_value = p
        best_values.append(best_value)

for p in best_values:
    productName = p.get("productName")
    currentPrice = p.get("currentPrice")
    discountPrice = p.get("discountPrice")
    retailPrice = p.get("retailPrice")
    size = p.get("size")
    pricePerLiter = p.get('pricePerLiter')
    onSale = p.get('onSale')

    if onSale:
        print "{} ({}): is on sale for ${}, a discount of ${} (${} per liter ).".format(productName, size, discountPrice, (retailPrice-currentPrice), pricePerLiter)
    else:
        print "{} ({}): is selling retail for ${} (${} per liter ).".format(productName, size, currentPrice, pricePerLiter)

print 'finis'
