import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://cloud-admin:#Security-2030@localhost/issue_tracker_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
