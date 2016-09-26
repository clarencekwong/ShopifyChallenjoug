import json, urllib2

#Set up some basic paramaters that will be used
site = "http://shopicruit.myshopify.com/products.json?page="
page = 1
grand_total = 0

while True:
    # Create the url that information will be pull from
    url = site + `page`
    # Open the URL we are trying to see
    webinfo = urllib2.urlopen(url)
    # Read the information
    info = webinfo.read()
    # Decode the information
    d_info = json.loads(info)
    # Test whether data exists in the page, breaks if empty
    if not len(d_info["products"]):
        break
    # Look for the product_type of watch and clock and add their pricing onto the grand_total
    for product in d_info["products"]:
    # Check for product being part of clock or watch
        if product["product_type"].lower() == "clock" or product["product_type"].lower() == "watch":
    # Checking through the API references for product listing, price of within each product branch is split into product property of variants
            for variant in product["variants"]:
                grand_total += float(variant["price"])
    # increase the page
    page += 1

print "The grand total of all the gizmos are: ",grand_total

