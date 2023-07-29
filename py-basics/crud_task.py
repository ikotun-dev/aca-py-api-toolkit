
#BASIC IMPLEMENTATION OF HOW A VER BASIC API WORKS - (CRUD FUNCTIONALITY)

users = ('collins', 'emmanuel', 'samuel')

list_of_posts = ['The sky is blue', 'The House is big', 'Im learning backend Engineering', 'The car is white', 'The door is white']

username_request = str(input("Enter your username for validation : "))
if username_request not in users :  #AUTHENTICATION IMPLEMENTATION
    print("user is not in the system")
else : 
    print("Welcome" + " " + username_request + ", " + "what do you want to do\n")
    print("1. Create Post")
    print("2. Read Post")
    print("3. Delete Post")
    print("4. Update Post\n")
    choice = int(input("Enter yout choice  (the id eg : 4) : "))
    
    #C - IMPLEMENTATION (CREATING A POST) [POST REQUEST]
    if choice == 1 :
        print("-----Create Post-----")
        content = str(input("Enter your new post content : "))
        list_of_posts[0] = content
        print(" -- Your post has been added --  ")
        for post in list_of_posts : print(post)

    #R - READING POST [GET REQUEST]
    if choice == 2:
        print("----Latest Posts-----")
        for post in list_of_posts : print(post)
    
    #D - DELETE REQUEST 
    if choice == 3:
        print("----Available Posts-----")
        i = 0
        while i < len(list_of_posts) : 
             for post in list_of_posts :
                    i+=1
                    print(str(i) + ".  " + post)
             
        post_to_delete = int(input("Enter ID of post to delete  : "))
        try : 
            list_of_posts.pop(post_to_delete-1)
            print("Post has been deleted successfully")
            
        except Exception as e: 
            print(str(e))

    #U - update request
    if choice == 4 : 
        print("----Available Posts-----")
        i = 0
        while i < len(list_of_posts) : 
             for post in list_of_posts :
                    i+=1
                    print(str(i) + ".  " + post)
        post_to_update = int(input("Enter the ID of post to update : "))
        post_new_version = str(input("Enter the new version of the post : "))

        list_of_posts.pop(post_to_update-1)
        list_of_posts.insert(post_to_update-1, post_new_version) #UPDATE LIST
        for post in list_of_posts: print(post)
