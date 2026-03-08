import timeit

# frozenset explanation
"""
frozenset is an immutable version of a set.
Normal sets can change, frozensets cannot.
They are used as dictionary keys or in caching systems where immutability is required.
"""

bundle_discounts = {
frozenset({'Electronics','Books'}):10,
frozenset({'Clothing','Home'}):15
}

def check_bundle_discount(cart):

    categories = {p.category for p in cart}

    for bundle,discount in bundle_discounts.items():
        if bundle.issubset(categories):
            return discount

    return 0


# Benchmark
set_time = timeit.timeit("set([1,2,3])",number=100000)
frozenset_time = timeit.timeit("frozenset([1,2,3])",number=100000)

print("Set time:",set_time)
print("Frozenset time:",frozenset_time)