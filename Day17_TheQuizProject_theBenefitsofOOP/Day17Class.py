class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        # set default attribute
        self.follower = 0
        self.following = 0

    def follow(self,user):
        user.follower +=1
        self.following +=1


    def __str__(self):
        return "ID:" + self.id + "," + self.username+" followers :"+str(self.follower)



user1 = User("0001", "Jinx")
user2 = User("0002", "Jinx")
user2.follow(user1)
print(user1.follower)
print(user1.following)
print()
print(user2.follower)
print(user2.following)
