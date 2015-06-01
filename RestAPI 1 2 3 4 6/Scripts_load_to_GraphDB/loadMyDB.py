from py2neo import neo4j, Node, rel, Graph, authenticate
from urllib import urlopen
import json, sys

reload(sys)
sys.setdefaultencoding("utf8")

graph_DB_url = "http://localhost:7474/db/data/"

def getAddress(id=0):
    authenticate("localhost:7474", "neo4j", "1111")
    graph = Graph(graph_DB_url)
    res = graph.cypher.execute("MATCH (n:Address {id:{id}}) RETURN n", {"id": id})

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

def getObject(id=0):
    authenticate("localhost:7474", "neo4j", "1111")
    graph = Graph(graph_DB_url)
    res = graph.cypher.execute("MATCH (n:Object {id:{id}}) RETURN n", {"id": id})

    if 0 != len(res):
        return res
    else:
        return None

def getDocumentBase(id=0):
    authenticate("localhost:7474", "neo4j", "1111")
    graph = Graph(graph_DB_url)
    res = graph.cypher.execute("MATCH (n:DocumentBase {id:{id}}) RETURN n", {"id": id})

    if 0 != len(res):
        return res
    else:
        return None

def getEncumbrance(id=0):
    authenticate("localhost:7474", "neo4j", "1111")
    graph = Graph(graph_DB_url)
    res = graph.cypher.execute("MATCH (n:Encumbrance {id:{id}}) RETURN n", {"id": id})

    if 0 != len(res):
        return res
    else:
        return None

def clear():
    authenticate("localhost:7474", "neo4j", "1111")
    graph = Graph(graph_DB_url)
    graph.cypher.execute("MATCH (n)"
                           "OPTIONAL MATCH (n)-[r]-()"
                           "DELETE n,r")




######################################
class AddressLoader(object):

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "1111")
        self.graph_db = Graph(graph_DB_url)
        self.api_url = "http://127.0.0.1:8000/api/v1/address/?format=json"
        self.statement = "MERGE (n:Address {id: {ID}, country:{C}, index:{I}, area:{A}, region:{R}, city:{CI}, " \
                         "street:{S}, home:{H}}) RETURN n"

    def whipUp(self):
        objects = json.load(urlopen(self.api_url))["objects"]
        db = self.graph_db.cypher.begin()
        for object in objects:
            args = {}
            args["ID"]=object["id"]
            args["C"]=object["Country"]
            args["I"]=object["Index"]
            args["A"]=object["Area"]
            args["R"]=object["Region"]
            args["CI"]=object["City"]
            args["S"]=object["Street"]
            args["H"]=object["Home"]

            db.append(self.statement, args)

        db.process()
        db.commit()

class PersonLoader(object):

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "1111")
        self.graph_db = Graph(graph_DB_url)
        self.api_url = "http://127.0.0.1:8000/api/v1/person/?format=json"
        self.statement = "MERGE (n:Person {Name:{N}, Identification:{I}, id: {ID}, NonResidentForeigner:{NR}," \
                         "MoreInformation:{MI}}) RETURN n"

    def whipUp(self):
        objects = json.load(urlopen(self.api_url))["objects"]

        for object in objects:
            args = {}
            args["ID"]=object["id"]

            args["I"]=object["Identification"]
            args["NR"]=object["NonResidentForeigner"]
            args["N"]=object["Name"]
            args["MI"]=object["MoreInformation"]
            #args["AD"]=object["Address"]["id"]

            perCh = getPerson(Name=args["N"])
            if perCh!=None:
                continue

            db = self.graph_db.cypher.begin()
            db.append(self.statement, args)
            db.commit()
            address = getAddress(id=int(object["Address"]["id"]))
            person = getPerson(id=int(args["ID"]))

            self.graph_db.create(rel(person.one, "LIVED", address.one))


        #db.process()
        #db.commit()

class ObjectLoader(object):

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "1111")
        self.graph_db = Graph(graph_DB_url)
        self.api_url = "http://127.0.0.1:8000/api/v1/object/?format=json"
        self.statement = "MERGE (n:Object {Name:{N}, id: {ID}, SerialNumber:{SN}, RegNumber:{RN}," \
                         "AddedInfoForUNMovable:{AI}}) RETURN n"

    def whipUp(self):
        objects = json.load(urlopen(self.api_url))["objects"]
        db = self.graph_db.cypher.begin()

        for object in objects:
            args = {}
            args["ID"]=object["id"]

            args["N"]=object["Name"]
            args["SN"]=object["SerialNumber"]
            args["RN"]=object["RegNumber"]
            args["AI"]=object["AddedInfoForUNMovable"]

            db.append(self.statement, args)

        db.process()
        db.commit()

class DocumentBaseLoader(object):

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "1111")
        self.graph_db = Graph(graph_DB_url)
        self.api_url = "http://127.0.0.1:8000/api/v1/documentbase/?format=json"
        self.statement = "MERGE (n:DocumentBase {Name:{N}, id: {ID}, PublisherName:{PN}, Number:{NU}," \
                         "Date:{D}}) RETURN n"

    def whipUp(self):
        objects = json.load(urlopen(self.api_url))["objects"]
        db = self.graph_db.cypher.begin()

        for object in objects:
            args = {}
            args["ID"]=object["id"]

            args["N"]=object["Name"]
            args["PN"]=object["PublisherName"]
            args["NU"]=object["Number"]
            args["D"]=object["Date"]

            db.append(self.statement, args)

        db.process()
        db.commit()

class EncumbranceLoader(object):

    def __init__(self):
        authenticate("localhost:7474", "neo4j", "1111")
        self.graph_db = Graph(graph_DB_url)
        self.api_url = "http://127.0.0.1:8000/api/v1/encumbrance/?format=json"
        self.statement = "MERGE (n:Encumbrance {NStatement:{NS}, id: {ID}, DateStatement:{DS}, Date:{D}," \
                         "AddedInfo:{AI}}) RETURN n"

    def whipUp(self):
        objects = json.load(urlopen(self.api_url))["objects"]

        for object in objects:
            args = {}
            args["ID"]=object["id"]

            args["NS"]=object["NStatement"]
            args["DS"]=object["DateStatement"]
            args["D"]=object["Date"]
            args["AI"]=object["AddedInfo"]

            db = self.graph_db.cypher.begin()
            db.append(self.statement, args)
            db.commit()

            enc = getEncumbrance(id=int(args["ID"]))
            obj = getObject(id=int(object["Obj"]["id"]))
            docBase = getDocumentBase(id=int(object["DocBase"]["id"]))

            if obj != None:
                self.graph_db.create(rel(enc.one, "HAVE_OBJECT", obj.one))
            if docBase != None:
                self.graph_db.create(rel(enc.one, "HAVE_DOCUMENT", docBase.one))

            for sp in object["SPerson"]:
                s_p = getPerson(id=int(sp["id"]))
                self.graph_db.create(rel(enc.one, "HAVE_DEPTOR", s_p.one))

            for wp in object["WPerson"]:
                w_p = getPerson(id=int(wp["id"]))
                self.graph_db.create(rel(enc.one, "HAVE_WEIGHT", w_p.one))


clear()

er = AddressLoader()
er.whipUp()

er = PersonLoader()
er.whipUp()

er = ObjectLoader()
er.whipUp()

er = DocumentBaseLoader()
er.whipUp()

er = EncumbranceLoader()
er.whipUp()