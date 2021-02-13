import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Fetch the service account key JSON file contents
cred = credentials.Certificate(
    './vaccine-percentage-firebase-adminsdk-ogi68-3623de3267.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vaccine-percentage-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('countries')

found_countries = ref.get()


# for i in found_countries:
#     if i['vaccinatedPercentage'] > 50:
#         print('Succesful vaccination: ' +str(i['name']))

for i in found_countries:
    if i['name'] == 'Chile':
        print('Vaccine percentage: ', (i['vaccinatedPercentage']), '%')