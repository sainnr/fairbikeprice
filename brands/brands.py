from brands.bike_brands_az import get_blog_brands
from brands.cycle_manufacturers_dbpedia import get_dbpedia_brands

if __name__ == '__main__':
    b1 = get_blog_brands()
    b2 = get_dbpedia_brands()

    print("%s %s" % (len(b1), len(b2)))
