from flask import Blueprint, request, jsonify, current_app
from ..models import db, Client

bp = Blueprint("clients", __name__)

@bp.route("/", methods=["GET"])
def list_clients():
    clients = Client.query.order_by(Client.id).all()
    return jsonify([c.to_dict() for c in clients]), 200

@bp.route("/", methods=["POST"])
def create_client():
    data = request.get_json() or {}
    name = data.get("name")
    if not name:
        return jsonify({"error": "name is required"}), 400
    c = Client(
        name=name,
        age=data.get("age"),
        weight=data.get("weight"),
        program=data.get("program"),
        calories=data.get("calories"),
    )
    db.session.add(c)
    db.session.commit()
    return jsonify(c.to_dict()), 201

@bp.route("/<int:client_id>", methods=["GET"])
def get_client(client_id):
    c = Client.query.get_or_404(client_id)
    return jsonify(c.to_dict()), 200

@bp.route("/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    c = Client.query.get_or_404(client_id)
    data = request.get_json() or {}
    for field in ("name","age","weight","program","calories"):
        if field in data:
            setattr(c, field, data[field])
    db.session.commit()
    return jsonify(c.to_dict()), 200

@bp.route("/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    c = Client.query.get_or_404(client_id)
    db.session.delete(c)
    db.session.commit()
    return jsonify({"deleted": client_id}), 200