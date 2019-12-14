import os

username = 'fmasjvreysufdc'
password = '412d682250ed844e5870ac10bef7d4e1df78cb0a5a22c20b9e396b496c51efb0'
host = 'ec2-107-21-108-37.compute-1.amazonaws.com'
port = '5432'
database = 'daocv3uoo1ckhc'
DATABASE_URI = os.getenv("DATABASE_URL",
                         'postgres://itztxiljkesfln:96aa77c3f8d47eded34a0d51daa1078844af3440ff274c894501cfe2901b6898@ec2-174-129-33-132.compute-1.amazonaws.com:5432/deqc8q6p8enj73')