# max discount for each category

# print "category, product ID, discount", order by category , ascending
# print minum product_id


# PRODUCT (max discount) --> EACH CATEGORY

# group by category
# find max discount
# print product ID (min)

SELECT maxdiscount, product_id
FROM PRODUCT
GROUP BY Category
ORDER BY product_id DESC