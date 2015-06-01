from py2neo import rel, Graph, authenticate
from urllib import urlopen
import json, sys

reload(sys)
sys.setdefaultencoding("utf8")

graph_DB_url = "http://localhost:7474/db/data/"


def getAddress(id=0, Street=None):
    authenticate("localhost:7474", "neo4j", "1111")
    graph = Graph(graph_DB_url)

    if Street==None:
        res = graph.cypher.execute("MATCH (n:Address {id:{id}}) RETURN n", {"id": id})
    else:
        res = graph.cypher.execute("MATCH (n:Address { id:{id}, street:{S} }) RETURN n", {"id": id, "S":Street})

    if 0 != len(res):
        return res
    else:
        return None

def getPerson(id=None, Name=None):
    authenticate("localhost:7474", "neo4j", "1111")
    graph = Graph(graph_DB_url)
    if Name==None and id!=None:
        res = graph.cypher.execute("MATCH (n:Person {id:{id}}) RETURN n", {"id": id})
    elif id==None and Name!=None:
        res = graph.cypher.execute("MATCH (n:Person {Name:{N}}) RETURN n", {"N":Name})
    else:
        res = graph.cypher.execute("MATCH (n:Person {id:{id},Name:{N} }) RETURN n", {"id": id, "N":Name})

    if 0 != len(res):
        return res
    else:
        return None

def getFilia(id=0):
    authenticate("localhost:7474", "neo4j", "1111")
    graph = Graph(graph_DB_url)
    res = graph.cypher.execute("MATCH (n:Filia {id:{id}}) RETURN n", {"id": id})

    if 0 != len(res):
        return res
    else:
        return None

def getSocialFormation(id=0):
    authenticate("localhost:7474", "neo4j", "1111")
    graph = Graph(graph_DB_url)
    res = graph.cypher.execute("MATCH (n:SocialFormation {id:{id}}) RETURN n", {"id": id})

    if 0 != len(res):
        return res
    else:
        return None


######################################
class AddressLoader(object):

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "1111")
        self.graph_db = Graph(graph_DB_url)
        self.api_url = "http://127.0.0.1:9000/api/v1/address/?format=json"
        self.statement = "MERGE (n:Address {id: {ID}, city:{C}, home:{H}, street:{S}, phone:{P}}) RETURN n"

    def whipUp(self):
        objects = json.load(urlopen(self.api_url))["objects"]

        db = self.graph_db.cypher.begin()
        for object in objects:
            args = {}
            args["ID"]=object["id"]

            args["C"]=object["City"]
            args["H"]=object["House"]
            args["P"]=object["Phone"]
            args["S"]=object["Street"]

            db.append(self.statement, args)

        db.process()
        db.commit()

class PersonLoader(object):

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "1111")
        self.graph_db = Graph(graph_DB_url)
        self.api_url = "http://127.0.0.1:9000/api/v1/person/?format=json"
        self.statement = "MERGE (n:Person {id: {ID}, Name:{N}, Phone:{P}}) RETURN n"

    def whipUp(self):
        objects = json.load(urlopen(self.api_url))["objects"]

        for object in objects:
            args = {}
            args["ID"]=object["id"]

            args["N"]=object["Surname"] + " " + object["Name"]
            args["P"]=object["Phone"]

            perCh = getPerson(Name=args["N"])
            if perCh!=None:
                continue

            #print args
            db = self.graph_db.cypher.begin()
            db.append(self.statement, args)
            db.commit()

class SocialFormationLoader(object):

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "1111")
        self.graph_db = Graph(graph_DB_url)
        self.api_url = "http://127.0.0.1:9000/api/v1/socialformation/?format=json"
        self.statement = "MERGE (n:SocialFormation {id: {ID}, Name:{N}, DateReg:{DR}, RegNumb:{RN}}) RETURN n"

    def whipUp(self):
        objects = json.load(urlopen(self.api_url))["objects"]

        for object in objects:
            args = {}
            args["ID"]=object["id"]

            args["N"]=object["Name"]
            args["DR"]=object["DateReg"]
            args["RN"]=object["RegNumb"]

            #print args
            db = self.graph_db.cypher.begin()
            db.append(self.statement, args)
            db.commit()

            sf = getSocialFormation(args["ID"])
            adr = getAddress(id = int(object["Address"]["id"]), Street = object["Address"]["Street"])
            #per = getPerson(id = int(object["Person"]["id"]), Name = (object["Person"]["Surname"] + " " + object["Person"]["Name"]))
            per = getPerson(Name = (object["Person"]["Surname"] + " " + object["Person"]["Name"]))

            if adr != None:
                self.graph_db.create(rel(sf.one, "HAVE_ADDRESS", adr.one))
            if per != None:
                self.graph_db.create(rel(sf.one, "SF_HAVE_PERSON", per.one))

class FiliaLoader(object):

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "1111")
        self.graph_db = Graph(graph_DB_url)
        self.api_url = "http://127.0.0.1:9000/api/v1/filia/?format=json"
        self.statement = "MERGE (n:Filia {id: {ID}, Name:{N}, DateReg:{DR}}) RETURN n"

    def whipUp(self):
        objects = json.load(urlopen(self.api_url))["objects"]

        for object in objects:
            args = {}
            args["ID"]=object["id"]

            args["N"]=object["Name"]
            args["DR"]=object["DateReg"]
            #print args
            db = self.graph_db.cypher.begin()
            db.append(self.statement, args)
            db.commit()

            f = getFilia(args["ID"])
            adr = getAddress(id = int(object["Address"]["id"]), Street = object["Address"]["Street"])
            #per = getPerson(id = int(object["Person"]["id"]), Name = (object["Person"]["Surname"] + " " + object["Person"]["Name"]))
            per = getPerson(Name = (object["Person"]["Surname"] + " " + object["Person"]["Name"]))

            soc = getSocialFormation(id = int(object["SocialFormation"]["id"]))

            if adr != None:
                self.graph_db.create(rel(f.one, "HAVE_ADDRESS", adr.one))
            if per != None:
                self.graph_db.create(rel(f.one, "FILIA_HAVE_PERSON", per.one))
            if soc != None:
                self.graph_db.create(rel(f.one, "HAVE_SocialFormation", soc.one))

#clear()

er = AddressLoader()
er.whipUp()

er = PersonLoader()
er.whipUp()

er = SocialFormationLoader()
er.whipUp()

er = FiliaLoader()
er.whipUp()