class User:
    def __init__(self,u_id,u_name,u_followers,u_following):
        self.id = u_id
        self.username = u_name
        self.followers = u_followers
        self.following = u_following
    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("001","dave",3,4)
user_2 = User("002","john",4,5)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)