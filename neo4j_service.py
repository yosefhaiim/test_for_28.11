from datetime import datetime
import uuid




# Todo: #  Create nodes for each device, labeled as Device.
#  Create a relationship labeled CONNECTED between the two devices.
#  Store the interaction details (e.g.,location).
#  You should choose where is the right place to store additional data ( node’s properties or relations’s )
# צור צמתים עבור כל מכשיר, המסומנים כמכשיר.
# צור קשר עם התווית CONNECTED בין שני המכשירים.
# אחסן את פרטי האינטראקציה (למשל, מיקום).


class DeviceRepository:
    def __init__(self, driver):
        # אתחול המחלקה עם Neo4j driver
        self.driver = driver

    def create_interaction(self, interaction_data):
        # יצירת אינטרקציה חדשה
        with self.driver.session() as session:
            # שאילתה ב-Cypher ליצירת אינטרקציה בין מכשירים
            query = """
            MERGE (source:Device {device_id: $from_device})
            MERGE (target:Device {device_id: $to_device})
            CREATE (source)-[c:CONNECTED]->(target) {
                interaction_id: $interaction_id,
                "method": $method,
                "signal_strength_dbm": $signal_strength_dbm,
                "distance_meters": $distance_meters,
                "duration_seconds": $duration_seconds, 
                timestamp: datetime($timestamp),
            }]->(target)
            RETURN c.interaction_id as interaction_id
            """
            # הפעלת השאילתה עם פרמטרים
            result = session.run(query, {
                'from_device': interaction_data['from_device'],  # מזהה מכשיר השולח
                'to_device': interaction_data['to_device'],  # מזהה מכשיר המקבל
                'interaction_id': str(uuid.uuid4()),  # יצירת מזהה ייחודי אינטרקציה
                'method': interaction_data['method'],
                'signal_strength_dbm': interaction_data['signal_strength_dbm'],
                'distance_meters': interaction_data['distance_meters'],
                'duration_seconds': interaction_data['duration_seconds'],
                'timestamp': datetime.strptime(
                    interaction_data['timestamp'], '%d/%m/%Y, %H:%M:%S'
                )  # המרת מחרוזת תאריך לאובייקט datetime
            })
            # החזרת מזהה אינטרקציה החדשה
            return result.single()['interaction_id']


# TODO: Expose flask’s endpoint for finding all devices connected
#  to each other using the Bluetooth method,
#  and how long is the path.
# חשוף את נקודת הקצה של הבקבוק למציאת כל ההתקנים המחוברים
# # זה לזה בשיטת Bluetooth,
# # וכמה אורך הדרך.

    def get_interaction_bluetooth(self, interaction_id):
        with self.driver.session() as session:
            # שאילתה ב-Cypher לשליפת נתוני האינטרקציה
            query = """
            MATCH (start:Device)
            MATCH (end:Device)
            WHERE start <> end
            MATCH path = shortestPath((start)-[:INTERACTED_WITH*]->(end))
            WHERE ALL(r IN relationships(path) WHERE r.method = 'Bluetooth')
            WITH path, length(path) as pathLength
            ORDER BY pathLength DESC
            LIMIT 1
            RETURN length(path)
            """
            # הפעלת השאילתה עם מזהה אינטרקציה כפרמטר
            result = session.run(query, {'interaction_id': interaction_id})
            record = result.single()  # קבלת התוצאה (שורה אחת בלבד)
            if record:
                # אם נמצאה אינטרקציה, להחזיר את הנתונים כמילון
                return dict(record)
            # אם לא נמצאה אינטרקציה, להחזיר None
            return None

# TODO: Expose flask’s endpoint for finding all devices connected to each other
#  with a signal strength stronger than -60.
# חשוף את נקודת הקצה של הבקבוק למציאת כל ההתקנים המחוברים זה לזה עם עוצמת אות חזקה מ-60.

    def get_interaction_big_from_60(self, interaction_id):
        with self.driver.session() as session:
            query = """
            MATCH (source)-[c:CONNECTION {interaction_id: $interaction_id}]->(target)
            WHERE c.signal_strength_dbm > -60
            RETURN c.interaction_id as interaction_id
            """
            # הפעלת השאילתה עם מזהה אינטרקציה כפרמטר
            result = session.run(query, {'interaction_id': interaction_id})
            record = result.single()  # קבלת התוצאה (שורה אחת בלבד)
            if record:
                # אם נמצאה אינטרקציה, להחזיר את הנתונים כמילון
                return dict(record)
            # אם לא נמצאה אינטרקציה, להחזיר None
            return None

# todo: Expose a Flask endpoint to count how many devices are
#  connected to a specific device based on a provided ID.
# חשוף נקודת קצה Flask כדי לספור כמה מכשירים מחוברים למכשיר ספציפי על סמך מזהה שסופק.

    def get_interaction_with_device(self, device_id):
        with self.driver.session() as session:
            # אני צריך שכאשר האינטרקציה במיקום של ממכשיר (from_device),
            # או במיקום של למכשיר(to_device),
            # שווה לID שהוכנס המכשיר הזה יכנס לרשימה שבה יוצגו כל המכשירים
            query = """
            
            """
            result = session.run(query, {'device_id': device_id})
            if result:
                # אם נמצאה אינטרקציה, להחזיר את הנתונים כמילון
                return dict(result)
            # אם לא נמצאה אינטרקציה, להחזיר None
            return None