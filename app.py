from flask import Flask, json, jsonify, request
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
notes = [
  {
    'id': 1,
    "body": "Купить хлеб",
    "status": True,
  },
  {
    'id': 2,
    "body": "Купить хлеб2",
    "status": True,
  },
  {
    "id": 3,
    "body": "Купить хлеб3",
    "status": True,
  },
  {
    "id": 4,
    "body": "Купить хлеб новая дата",
    "status": True,
  },
  {
      "id": 5,
      "body": "Купить хлеб новая дата2",
      "status": True,
    }
]


@app.route('/notes', methods=['GET'])
def get_list():
    return jsonify(notes) 

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
  item= next((x for x in notes if x['id'] == note_id), None)
  if not item :
    return{'message':'No note'}, 400
  return item 

@app.route('/notes', methods=['POST'])
def update_list():
  maxIdNote=notes[0]['id']
  for item in notes:
    if item['id']> maxIdNote:
      maxIdNote=item['id']
  maxIdNote=maxIdNote+1
  new_note=request.json
  new_note["id"]=maxIdNote
  print(type(new_note))
  notes.append(new_note)
  return jsonify(notes) 

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
  item= next((x for x in notes if x['id'] == note_id), None)
  params=request.json
  if not item :
    return{'message':'No note'}, 400
  item.update(params)
  return jsonify(notes) 

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
  idNotes, _=next((x for x in enumerate(notes)
  if x[1]['id']==note_id), (None,None))
  print(idNotes)
  if  not idNotes:
    return{'message':'No note'}, 400
  notes.pop(idNotes)
  return jsonify(notes), 200 

if __name__ == '__main__':
    app.run()
