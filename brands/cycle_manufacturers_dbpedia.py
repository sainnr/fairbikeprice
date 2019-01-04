from SPARQLWrapper import SPARQLWrapper, JSON
from brands.Brand import Brand

query = """
    select distinct ?domain, ?label, (GROUP_CONCAT(DISTINCT ?url; SEPARATOR=", ") AS ?url_c), ?about
    where {
      ?domain rdf:type ?type.
      ?domain rdfs:label ?label.
      ?domain foaf:homepage ?url.
      ?domain dbo:abstract ?about.
      FILTER(
        (?type = <http://dbpedia.org/class/yago/WikicatCycleManufacturers> OR 
         ?type = <http://dbpedia.org/class/yago/WikicatMountainBikeManufacturers>) AND 
        (LANG(?label) = "" OR LANGMATCHES(LANG(?label), "en")) AND
        (LANG(?about) = "" OR LANGMATCHES(LANG(?about), "en"))
      )
    }
    group by ?domain ?label ?about
    order by ?label
    """


def get_dbpedia_brands():
    print("Bike manufacturers from DBPedia")

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    brands = set()

    for result in results["results"]["bindings"]:
        print('[%s; %s; %s]' % (result["label"]["value"], result["url_c"]["value"], result["about"]["value"]))
        b = Brand(result["label"]["value"], result["url_c"]["value"], result["about"]["value"])
        brands.add(b)

    return brands
