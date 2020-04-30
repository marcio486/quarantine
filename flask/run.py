from flaskblog import app

    
if __name__ == '__main__':
    app.run(debug = True)
    
    
#Terminal commands
#from flaskblog import db
#db.create_all() #in terminal creates site.db


#Tests on command line
#from flaskblog import User,Post
#user_1 = User(username='Marcio', email='test@gmail.com', password='password')

#from flaskblog import db
#db.session.add(user_1)
#user_2 = User(username='testes', email='falcatrua@gmail.com', password='password')
#db.session.add(user_2)
#db.session.commit()
#User.query.all()
#User.query.first()
#User.query.filter_by(username='Marcio').all()
#user = User.query.filter_by(username = 'Marcio').first()
#user.id
#user.posts
#post_1 = Post(title='Post 1', content='First post',user_id=user.id)
#post_2 = Post(title='Post 2', content='SecondDD post',user_id=user.id)
#db.session.add(post_1)
#db.session.add(post_2)
#db.session.commit()
#user.posts