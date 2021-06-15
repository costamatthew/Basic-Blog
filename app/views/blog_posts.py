from flask import Blueprint, render_template, request, redirect
from app import db

from ..models.posts_model import KlogPosts
from ..services.helper import check_data



bp = Blueprint("bp_blog_posts", __name__)




@bp.route("/api", methods=['GET'])
def get_posts():
    posts = KlogPosts().query.all()

    if posts == []:
        return render_template("no_content.html"), 404

    return render_template("posts.html", posts=posts), 200




@bp.route("/api/posts", methods=['GET'])
def form_for_new_posts():
    return render_template("new_post.html")




@bp.route("/api/posts", methods=['POST'])
def new_posts():
    result = request.form

    try:
        data = check_data(result)

        new_post = KlogPosts(
            title=data["title"],
            date=data["date"],
            contents=data["contents"],
            author=data["author"],
            email=data["email"]
        )
        
        db.session.add(new_post)
        db.session.commit()

        return redirect("/api"), 201
    except KeyError as e:
        return e.args[0], 402
    
    




@bp.route("/api/posts/<int:post_id>", methods=['GET'])
def get_one_post(post_id):
    get_post = KlogPosts.query.filter(KlogPosts.id==post_id).all()

    if get_post:
        return render_template("posts.html", posts=get_post), 200


    return render_template("not_found.html"), 404


