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