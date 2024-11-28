import phone_dispatcher
from flask import request, jsonify, Blueprint
import requests
from neo4j import GraphDatabase

from app import phone_blueprint


# TODO: Step 3: Create the Flask Application
#  Create your own Flask app to handle POST requests from the phone_dispatcher
#  and process the incoming JSON payload
#  Create routes folder and a specific route handling phone_dispatcher:

@phone_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   print(request.json)
   return jsonify({ }), 200


# TODO: Step 4: Run the Flask Application
#  Run your Flask application and then run the phone dispatcher.
#  Print request body as written above.
# להריץ את האפליקציה, לא עבד ננסה יותר מאוחר





# TODO: Expose flask’s endpoint for finding all devices connected
#  to each other using the Bluetooth method,
#  and how long is the path.
# חשוף את נקודת הקצה של הבקבוק למציאת כל ההתקנים המחוברים
# # זה לזה בשיטת Bluetooth,
# # וכמה אורך הדרך.



# TODO: Expose flask’s endpoint for finding all devices connected to each other
#  with a signal strength stronger than -60.
# חשוף את נקודת הקצה של הבקבוק למציאת כל ההתקנים המחוברים זה לזה עם עוצמת אות חזקה מ-60.


# todo: Expose a Flask endpoint to count how many devices are
#  connected to a specific device based on a provided ID.
# חשוף נקודת קצה Flask כדי לספור כמה מכשירים מחוברים למכשיר ספציפי על סמך מזהה שסופק.


# todo: Expose a Flask endpoint to determine whether
#  there is a direct connection between two devices.
# חשוף נקודת קצה Flask כדי לקבוע אם יש חיבור ישיר בין שני התקנים.

# todo: Expose a Flask endpoint to fetch the most recent interaction for a specific device,
#  sorted by timestamp.
# חשוף נקודת קצה Flask כדי להביא את האינטראקציה העדכנית ביותר עבור מכשיר ספציפי, ממוינת לפי חותמת זמן.
