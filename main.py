from flask import request, jsonify, Blueprint
import requests


phone_blueprint = Blueprint('phone_blueprint', __name__)
# TODO: Step 3: Create the Flask Application
#  Create your own Flask app to handle POST requests from the phone_dispatcher
#  and process the incoming JSON payload
#  Create routes folder and a specific route handling phone_dispatcher:

@phone_blueprint.route("/phone_tracker", methods=['POST'])
def get_interaction():
   print(request.json)
   return jsonify({ }), 200


# TODO: Step 4: Run the Flask Application
#  Run your Flask application and then run the phone dispatcher.
#  Print request body as written above.
# work!!!!!!!!!

# todo: Expose a Flask endpoint to determine whether
#  there is a direct connection between two devices.
# חשוף נקודת קצה Flask כדי לקבוע אם יש חיבור ישיר בין שני התקנים.


# todo: Expose a Flask endpoint to fetch the most recent interaction for a specific device,
#  sorted by timestamp.
# חשוף נקודת קצה Flask כדי להביא את האינטראקציה העדכנית ביותר עבור מכשיר ספציפי, ממוינת לפי חותמת זמן.
