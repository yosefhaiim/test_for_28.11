import phone_dispatcher
from flask import request, jsonify
import requests






# TODO: Step 3: Create the Flask Application
#  Create your own Flask app to handle POST requests from the phone_dispatcher and process the incoming JSON payload
#  Create routes folder and a specific route handling phone_dispatcher:
#  @phone_blueprint.route("/api/phone_tracker", methods=['POST'])
#  def get_interaction():
#    print(request.json)
#    return jsonify({ }), 200

# צור אפליקציית Flask משלך,
# כדי לטפל בבקשות POST מה-phone_dispatcher ולעבד את מטען ה-JSON הנכנס
# # צור תיקיית מסלולים וטיפול מסלול ספציפי phone_dispatcher:




@phone_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   print(request.json)
   return jsonify({ }), 200
