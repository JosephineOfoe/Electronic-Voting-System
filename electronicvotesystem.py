import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print(name)
    with open('./students/student_data.txt', 'r') as f:
        data = f.read()
        if not data:
            return jsonify({"error": "No data in the file"})
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'}), 404

@app.route('/', methods=['POST'])
def register_student():
    register = json.loads(request.data)
    with open('./students/student_data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [register]
    else:
        records = json.loads(data)
        records.append(register)
    with open('./students/student_data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(register)

@app.route('/', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('./students/student_data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    print(record['id_num'])
    for r in records:
        if r['id_num'] == record['id_num']:
            r = record
        new_records.append(r)
    with open('./students/student_data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

app.run(debug=True, port=8000)