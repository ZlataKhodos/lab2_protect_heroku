import os

username = 'itztxiljkesfln'
password = '96aa77c3f8d47eded34a0d51daa1078844af3440ff274c894501cfe2901b6898'
host = 'ec2-174-129-33-132.compute-1.amazonaws.com'
port = '5432'
database = 'deqc8q6p8enj73'
DATABASE_URI = os.getenv("DATABASE_URL",
                         'postgres://itztxiljkesfln:96aa77c3f8d47eded34a0d51daa1078844af3440ff274c894501cfe2901b6898@ec2-174-129-33-132.compute-1.amazonaws.com:5432/deqc8q6p8enj73')