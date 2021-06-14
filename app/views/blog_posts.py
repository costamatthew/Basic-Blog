from flask import Blueprint, render_template

from ..models.posts_model import KlogPosts



bp = Blueprint("bp_blog_posts", __name__)




@bp.route("/api", methods=['GET'])
def get_posts():
    posts = KlogPosts().query.all()

    if posts == []:
        return render_template("no_content.html")

    return render_template("base.html")



@bp.route("/api/posts", methods=['GET'])
def form_for_new_posts():
    pass



@bp.route("/api/posts", methods=['POST'])
def new_posts():
    pass




@bp.route("/api/<int:post_id>", methods=['GET'])
def get_one_post(post_id):
    pass

