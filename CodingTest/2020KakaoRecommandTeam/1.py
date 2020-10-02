def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here
    count = 0
    product = dict(zip(products, productPrices))
    sold = dict(zip(productSold, soldPrice))
    for key in sold.keys():
        if key in product and product[key] != sold[key]:
            count += 1
        
    return count

product = ["eggs", 'milk', 'cheese']
productPrices = [2.89, 3.29, 5.79]
productSold= ["eggs", "eggs", 'cheese', 'milk']
soldPrice = [2.89, 2.99, 5.97, 3.29]
priceCheck(product, productPrices, productSold, soldPrice)
