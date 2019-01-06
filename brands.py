from brands import brands_az
from brands import dbpedia

if __name__ == '__main__':
    b1 = brands_az.get_blog_brands()
    b2 = dbpedia.get_dbpedia_brands()

    print("%s %s" % (len(b1), len(b2)))
