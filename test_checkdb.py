import unittest 
import csv
import config  # noqa: F401
import models
from flask import Flask, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, \
    logout_user, current_user


class TestDbExist(unittest.TestCase):
    def test_db(self):
            first_name = "Noam"
            last_name = "Hasin"
            email = "Noamhasin@g.com"
            expertise = "yes"

            fieldnames = ['first_name', 'last_name', 'email', 'expertise']
            with open('data/mailingList.csv', 'a+') as inFile:
                writer = csv.DictWriter(inFile, fieldnames=fieldnames)
                writer.writerow({
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'expertise': expertise
                })
                
            # inFile.close()

            spamReader = csv.reader(open('data/mailingList.csv'), delimiter=',')
            # inFile.close()
            for row in spamReader:
                print(row)
           
            inFile.close()

if __name__ == "__main__":
    unittest.main()
