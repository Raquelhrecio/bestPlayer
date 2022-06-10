from morph_kgc import materialize
from rdflib import graph
from rdflib.namespace import Namespace
from rdflib.plugins.sparql import prepareQuery


def generarGrafoFem():
    config = """
            [DataSource1]
            mappings=C:/Users/raque/Documents/data/bestPlayerFemenino.ttl
            file_path=C:/Users/raque/Documents/data/female-players-22-csv.csv
         """

    graphFem = materialize(config)

    v = graphFem.serialize(destination="C:/Users/raque/Documents/data/femalePlayers.nt", format="n3")
    return v

def generarGrafoMasc():
    config = """
            [DataSource1]
            mappings=C:/Users/raque/Documents/data/bestPlayerMasculino.ttl
            file_path=C:/Users/raque/Documents/data/players-22-csv.csv
         """

    graphMasc = materialize(config)

    v = graphMasc.serialize(destination="C:/Users/raque/Documents/data/MalePlayers.nt", format="n3")
    return v

graphFem = generarGrafoFem()

def nombresFemenino():
    SCHEMA = Namespace("http://schema.org/")

    q1 = prepareQuery('''
      SELECT ?player ?name
      WHERE {
        ?player rdf:type schema:Person;
          <http://schema.org/name> ?name
      }
    ''',
                      initNs={"schema": SCHEMA})
    for r in graphFem.query(q1):
        print(r.player, r.name)

graphMasc = generarGrafoMasc()

def nombresMasculino():
    SCHEMA = Namespace("http://schema.org/")

    q1 = prepareQuery('''
      SELECT ?player ?name
      WHERE {
        ?player rdf:type schema:Person;
          <http://schema.org/name> ?name
      }
    ''',
                      initNs={"schema": SCHEMA})
    for r in graphMasc.query(q1):
        print(r.player, r.name)

def mercadoMasculino():
    SCHEMA = Namespace("http://schema.org/")
    SOCCER = Namespace("http://www.bestPlayer.com/ontology#")
    pos = "ST"

    q2 = prepareQuery('''
      SELECT ?player ?name ?media ?posicion
      WHERE {
        ?player rdf:type schema:Person;
          <http://schema.org/name> ?name.
        ?player soccer:añosRestantes 1.
        ?player soccer:posicion ?posicion
      }

    ''',
                      initNs={"schema": SCHEMA, "soccer": SOCCER})

    for r in graphMasc.query(q2):
        print(r.player, r.name, r.posicion)
