from flask import request, jsonify
from app import app, db
from app.models import Issue

@app.route('/issues', methods=['GET'])
def get_issues():
    issues = Issue.query.all()
    return jsonify([issue.to_dict() for issue in issues])

@app.route('/issues', methods=['POST'])
def create_issue():
    data = request.get_json()
    new_issue = Issue(title=data['title'], description=data['description'])
    db.session.add(new_issue)
    db.session.commit()
    return jsonify(new_issue.to_dict()), 201

@app.route('/issues/<int:id>', methods=['PUT'])
def update_issue(id):
    issue = Issue.query.get_or_404(id)
    data = request.get_json()
    issue.title = data['title']
    issue.description = data['description']
    issue.status = data['status']
    db.session.commit()
    return jsonify(issue.to_dict())

@app.route('/issues/<int:id>', methods=['DELETE'])
def delete_issue(id):
    issue = Issue.query.get_or_404(id)
    db.session.delete(issue)
    db.session.commit()
    return '', 204
