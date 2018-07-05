
from firebase_admin import credentials, firestore, initialize_app

PROJECT_ID = 'gnext18-v5'
SCOPES = [
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/datastore'
]

def get_client():
  cred = credentials.Certificate('../gnext18-v5-62f86909f9fc.json')
  initialize_app(cred, {
      'projectId': PROJECT_ID
  })
  return firestore.client()

if __name__ == '__main__':
  client = get_client()
  print('students: '+[d.id for d in client.collection('students').get()])