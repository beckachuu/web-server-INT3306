from flask import request
from flask_restful import Resource

from src.const import *
from src.controller.auth import login_required
from src.services.bookmark_sv import *


class MyBookmarks(Resource):
    @login_required()
    def get(self):
        book_id = request.args.get(BOOK_ID)
        bm_name = request.args.get(BOOKMARK_NAME)
        result, status = get_bookmark(book_id, bm_name)

        if status == OK_STATUS:
            return result, OK_STATUS
        elif status == NOT_FOUND:
            return {MESSAGE: "Can't find your bookmark."}, NOT_FOUND
        else:
            return NO_IDEA_WHAT_ERROR_THIS_IS

    @login_required()
    def post(self):
        json = request.get_json()
        status = add_bookmark(json)

        return status

    @login_required()
    def put(self):
        json = request.get_json()
        status = edit_bookmark(json)

        return status

    @login_required()
    def delete(self):
        book_id = request.args.get(BOOK_ID)
        bm_name = request.args.get(BOOKMARK_NAME)
        status = add_bookmark(book_id, bm_name)

        return status