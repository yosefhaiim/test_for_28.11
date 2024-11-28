from neo4j import GraphDatabase


# TODO: Initiate data and create nodes and relationships for every call interaction:
# התחל נתונים וצור צמתים וקשרים לכל אינטראקציה של שיחה:


def init_neo4j():
   # יצירת אובייקט Driver המתחבר ל- Neo4j באמצעות פרוטוקול Bolt
   neo4j_driver = GraphDatabase.driver(
      "bolt://neo4j:7687",
      auth=("neo4j", "password")
   )
   return neo4j_driver