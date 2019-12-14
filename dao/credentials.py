import os

username = 'fmasjvreysufdc'
password = '412d682250ed844e5870ac10bef7d4e1df78cb0a5a22c20b9e396b496c51efb0'
host = 'ec2-107-21-108-37.compute-1.amazonaws.com'
port = '5432'
database = 'daocv3uoo1ckhc'
DATABASE_URI = os.getenv("DATABASE_URL",
                         'postgres://fmasjvreysufdc:412d682250ed844e5870ac10bef7d4e1df78cb0a5a22c20b9e396b496c51efb0@ec2-107-21-108-37.compute-1.amazonaws.com:5432/daocv3uoo1ckhc')
