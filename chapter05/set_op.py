def main():
    store_a_products = {
        "Apples",
        "Bananas",
        "Cherries",
        "Watermelons"
    }

    store_b_products = {
        "Bananas",
        "Cherries",
        "Figs",
        "Melons"
    }

    #find common products (intersection) avalaible in both stores
    common_products = store_a_products & store_b_products
    print(common_products)
    #alternative way
    common_products2 = store_a_products.intersection(store_b_products)
    print(common_products2)
    #find all unique products(union) across both stores( a+b)
    all_products = store_a_products | store_b_products
    print(all_products)
    #using func
    all_products2 = store_a_products.union(store_b_products)
    print(all_products2)

    
    #find products available in store B but not in store A (difference)
    store_b_exclusive = store_b_products - store_a_products
    print(store_b_exclusive)
    #using func
    store_b_exclusive2 = store_b_products.difference(store_a_products)
    print(store_b_exclusive2)


    #find products that are in either A or B store but not in both
    unique_to_either_store = store_a_products.symmetric_difference(store_b_products)
    print(unique_to_either_store)


if __name__ == "__main__":
    main()