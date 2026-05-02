class boom:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = input().split()
boom1 = boom(code, color, sec)

print(f'''code : {boom1.code}
color : {boom1.color}
second : {boom1.sec}
''')