import os


class Config:
    SECRET_KEY = ${{ secrets.SECRET_KEY }}
    SQLALCHEMY_DATABASE_URI = ${{ secrets.SQLALCHEMY_DATABASE_URI }}
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ${{ secrets.EMAIL_USER }}
    MAIL_PASSWORD = ${{ secrets.EMAIL_PASS }}
