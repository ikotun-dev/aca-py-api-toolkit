users = ('collins', 'emmanuel', 'samuel')
list_of_posts = ['The sky is blue', 'The House is big', 'Im learning backend Engineering', 'The car is white', 'The door is white']

#functions 
def get_post():
    for post in list_of_posts : print(post)

def add_post(post_content : str) : 
    list_of_posts[0] = post_content
