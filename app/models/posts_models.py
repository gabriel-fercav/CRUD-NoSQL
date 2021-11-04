import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['kenzie']

class Posts():
    def __init__(self, title: str, author: str, tags: list, content: str):
        self._id = Posts.create_id()
        self.created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
        self.updated_at = "Never"
        self.title = title.title()
        self.author = author.title()
        self.tags = tags
        self.content = content           

    def insert_post(self):
        db.posts.insert_one(self.__dict__)            

    @staticmethod
    def get_posts():
        all_posts = list(db.posts.find())    
        return all_posts

    @staticmethod
    def delete_post(id):
        show_all = Posts.get_posts() 
        for post in show_all:
            print(post['_id'])
            print(id)
            if post['_id'] == id:
                saved_post = post
                db.posts.delete_one({"_id": id})
                return saved_post
        return False      

    @staticmethod
    def find_post(id):
        show_all = Posts.get_posts()
        for post in show_all:
            if post['_id'] == id:
                return post    

    @staticmethod
    def create_id():
        show_all = Posts.get_posts()
        biggest_id = 0
        for posts in show_all:
            if posts['_id'] > biggest_id:
                biggest_id = posts['_id']      
        return biggest_id + 1 

    @staticmethod
    def update_post(post: 'Posts', data):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
        db.posts.update_one({"_id": post['_id']}, data)
        db.posts.update_one({"_id": post['_id']}, {"$set": {"updated_at": date}})

        return post