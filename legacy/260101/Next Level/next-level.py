class userID():
    def __init__(self, ID = "None", Lv = 0):
        self.ID = ID
        self.Lv = Lv

user1_id, user1_lv = input().split()

user1 = userID(user1_id, user1_lv)
user2 = userID("codetree", 10)

print(f"user {user2.ID} lv {user2.Lv}")
print(f"user {user1.ID} lv {user1.Lv}")