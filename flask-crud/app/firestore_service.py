import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'flask-crud-255707'
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})

db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_user(user_id):
  return db.collection('users').document(user_id).get()

def getj_todos(user_id):
  return db.collection('users')\
  .document(user_id).collection('todos').get()

def user_put(user_data):
  user_ref = db.collection('users').document(user_data.username)
  user_ref.set({'password': user_data.password})

def put_todo(user_id, game, description, price, ):
  todos_collection_ref = db.collection('users').document(user_id).collection('todos')
  todos_collection_ref.add({
    'game': game,
    'description': description,
    'price': price
  })
