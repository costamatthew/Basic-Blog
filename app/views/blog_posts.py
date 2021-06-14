from flask import Blueprint


bp = Blueprint("bp_blog_posts", __name__)




@bp.route("/api", methods=['GET'])
def get_posts():
    pass




@bp.route("/api/posts", methods=['POST'])
def posts_from_blog():
    pass




@bp.route("/api/<int:post_id>", methods=['GET'])
def get_one_post(post_id):
    pass