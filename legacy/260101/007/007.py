class struct:
    def __init__(self, code, spot, time):
        self.code = code
        self.spot = spot
        self.time = time


one, two, three = input().split()
secret = struct(one, two, three)

print("secret code : " + secret.code)
print("meeting point : " + secret.spot)
print("time : " + secret.time)