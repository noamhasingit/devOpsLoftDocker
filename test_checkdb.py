import unittest
import csv
import config  # noqa: F401


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
            Reader = csv.reader(open('data/mailingList.csv'), delimiter=',')
            for row in Reader:
                print(row)
            inFile.close()


if __name__ == "__main__":
    unittest.main()
