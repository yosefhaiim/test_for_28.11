from flask import Blueprint, request, jsonify, current_app  # ייבוא כלים מ-Flask
import json  # עבודה עם JSON
import logging  # רישום לוגים

from neo4j_service import DeviceRepository  # ייבוא המחלקה לטיפול ב-Neo4j

# יצירת Blueprint בשם 'interaction_bp' לניהול נקודות הקצה של אינטרקציות
interaction_up = Blueprint('interaction_up', __name__)


@interaction_up.route('/', methods=['POST'])
def create_interaction():
    # נקודת קצה ליצירת אינטרקציה חדשה

    # קריאת נתוני הבקשה (JSON)
    data = request.get_json()


    # שדות החובה ליצירת אינטרקציה
    required_fields = ['from_device', 'to_device', 'method', 'signal_strength_dbm', 'distance_meters', 'duration_seconds', 'timestamp']

    # בדיקה אם כל שדות החובה קיימים בנתונים
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # יצירת מופע של TransactionRepository עם ה-Neo4j Driver של האפליקציה
        repo = DeviceRepository(current_app.neo4j_driver)

        # קריאה לפונקציה ליצירת אינטרקציה, וקבלת מזהה אינטרקציה
        interaction_id = repo.create_interaction(data)

        # החזרת תגובה מוצלחת עם מזהה אינטרקציה
        return jsonify({
            'status': 'success',
            'interaction_id': interaction_id
        }), 201
    except Exception as e:
        # טיפול בשגיאה: רישום הודעת שגיאה בקונסול ובקובץ לוג
        print(str(e))
        logging.error(str(e))

        # החזרת תגובה עם הודעת שגיאה
        return jsonify({'error': 'internal server error'}), 500


# endpoint for get interaction by bluetooth
@interaction_up.route('/api/interaction_bluetooth/<interaction_id>', methods=['GET'])
def get_interaction_bluetooth():
    interaction_id = request.args.get('interaction_id')
    repo = DeviceRepository(current_app.neo4j_driver)
    interaction = repo.get_interaction_bluetooth(interaction_id)
    return jsonify({'interaction': interaction}), 200


# endpoint for get interaction if signal_strength_dbm > -60
@interaction_up.route('/api/interaction/<interaction_id>', methods=['GET'])
def get_interaction_big_from_60():
    interaction_id = request.args.get('interaction_id')
    repo = DeviceRepository(current_app.neo4j_driver)
    interaction = repo.get_interaction_big_from_60(interaction_id)
    return jsonify({'interaction': interaction}), 200

# endpoint for get more devices if they connected with this device
@interaction_up.route('/api/interaction/<interaction_id>', methods=['DELETE'])
def get_interaction_with_device():
    interaction_id = request.args.get('interaction_id')
    repo = DeviceRepository(current_app.neo4j_driver)
    interactions = list(repo.get_interaction_with_device(interaction_id))
    return jsonify({'interactions': interactions}), 200