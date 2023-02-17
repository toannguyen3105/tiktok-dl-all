from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import TiktokLinkModel
from schemas import TiktokLinkSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("TiktokLinks", __name__, description="Operations on tiktokLinks")


@blp.route("/tiktokLink/<string:tiktokLinkId>")
class TiktokLink(MethodView):
    @blp.response(200, TiktokLinkSchema)
    def get(self, tiktokLinkId):
        tiktokLink = TiktokLinkModel.query.get_or_404(tiktokLinkId)
        return tiktokLink

    def delete(self, tiktokLinkId):
        item = TiktokLinkModel.query.get_or_404(tiktokLinkId)
        db.session.delete(item)
        db.session.commit()
        return {"message": "TiktokLinkModel deleted"}


@blp.route("/tiktokLink")
class TiktokLinkList(MethodView):
    @blp.response(200, TiktokLinkSchema(many=True))
    def get(self):
        return TiktokLinkModel.query.all()

    @blp.arguments(TiktokLinkSchema)
    @blp.response(201, TiktokLinkSchema)
    def post(self, tiktokLinkData):
        tiktokLink = TiktokLinkModel(**tiktokLinkData)

        try:
            db.session.add(tiktokLink)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return tiktokLink
