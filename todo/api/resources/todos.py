from flask_restx import Resource

from todo.api.namespaces import todo_ns as ns
from todo.api.models.todos import todo, DAO


@ns.route("/")
class TodoList(Resource):
    @ns.doc("list_todos")
    @ns.marshal_list_with(todo)
    def get(self):
        return DAO.todos

    @ns.doc("create_todo")
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        return DAO.create(ns.payload), 201


@ns.route("/<int:id>")
@ns.response(404, "Todo not found")
@ns.param("id", "The task identifier")
class Todo(Resource):
    @ns.doc("get_todo")
    @ns.marshal_with(todo)
    def get(self, id):
        return DAO.get(id)

    @ns.doc("delete_todo")
    @ns.response(204, "Todo deleted")
    def delete(self, id):
        DAO.delete(id)
        return "", 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        return DAO.update(id, ns.payload)
