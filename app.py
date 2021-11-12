from flask import Flask, json, jsonify, request
app = Flask(__name__)

notes = [
  {
    'id': 1,
    "body": "Купить хлеб",
    "status": True,
    "dateCreation": "2021-11-11T12:37:20.976Z"
  },
  {
    'id': 2,
    "body": "Купить хлеб2",
    "status": True,
    "dateCreation": "2021-11-11T12:37:29.443Z"
  },
  {
    "id": 3,
    "body": "Купить хлеб3",
    "status": True,
    "dateCreation": "2021-11-11T12:37:34.992Z"
  },
  {
    "id": 4,
    "body": "Купить хлеб новая дата",
    "status": True,
    "dateCreation": "2021-11-11T12:38:27.202Z"
  },
  {
      "id": 5,
      "body": "Купить хлеб новая дата2",
      "status": True,
      "dateCreation": "2021-11-11T12:38:27.202Z"
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
 # maxIdNote=notes[0]['id']
 # for item in notes:
   # if item['id']> maxIdNote:
     # maxIdNote=item['id']
  #maxIdNote=maxIdNote+1
  #paramsId= '{"id":'+str(maxIdNote)+','
  new_note=request.json
  #new_note= (str(new_note)).replace('{',paramsId)
  notes.append(new_note)
  return jsonify(notes) 

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
  item= next((x for x in notes if x['id'] == note_id), None)
  params=request.json
  if not item :
    return{'message':'No note'}, 400
  item.update(params)
  return item 

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
  idNotes, _=next((x for x in enumerate(notes)
  if x[1]['id']==note_id), (None,None))
  print(idNotes)
  if  not idNotes:
    return{'message':'No note'}, 400
  notes.pop(idNotes)
  return 'Note delete',200 

if __name__ == '__main__':
    app.run()
