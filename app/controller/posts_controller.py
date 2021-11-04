from ..models.posts_models import Posts
from flask import Flask, json, jsonify,request

# /posts
# Retorna o status code mais indicado caso esteja faltando alguma chave no JSON enviado.

# PATCH /posts/<id>
# Retorna o status code mais indicado caso o JSON enviado não seja válido.

def init_app(app: Flask):

    @app.post('/posts')
    def add_post():
        data = request.json
        post = Posts(**data)
        post.insert_post()
        return jsonify(post.__dict__), 201  

    @app.get('/posts')
    def list_all():
        show_all = Posts.get_posts()
        return jsonify(show_all)


    @app.get('/posts/<int:id>')
    def get_post_by_id(id: int):
        searched_post = Posts.find_post(id)
        if searched_post:
            return jsonify(searched_post)
        else:
            return { 'error': 'The post does not exist.' }, 404  

    @app.delete('/posts/<int:id>')
    def delete_single_post(id: int):
        post_to_delete = Posts.delete_post(id)
        if post_to_delete:
            return jsonify(post_to_delete)
        else:    
            return {"error": "The post specified to be deleted does not exist"}, 404  

    @app.patch('/posts/<int:id>')
    def patch_post(id: int):
        searched_post = Posts.find_post(id)
        to_be_patched = { "$set": request.json }
        if searched_post:
            Posts.update_post(searched_post, to_be_patched)
            return jsonify(searched_post)
        else:
            return { 'error': 'The post does not exist.' }, 404                      

