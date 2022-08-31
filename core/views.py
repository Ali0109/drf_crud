import csv
import os

from django.db import connection

from crud.models import *
from core.settings import BASE_DIR


def check_foreign_key(check_num):
    cursor = connection.cursor()
    cursor.execute(f"SET FOREIGN_KEY_CHECKS = {check_num};")
    print(f"FOREIGN_KEY_CHECKS = {check_num}")


def truncate(table):
    cursor = connection.cursor()
    cursor.execute(f"TRUNCATE TABLE `crud_{table}`")
    print(f"crud_{table} truncated successfully")


def dataSeed():
    truncate('data')
    with open(os.path.join(BASE_DIR, 'media/csv/data.csv'), 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            Data.objects.create(
                name=line[0],
                phone=line[1],
                region=line[2],
                country=line[3],
            )
    print("Data import successfully!", end="\n\n")


def dbSeed():
    check_foreign_key(0)
    dataSeed()
    check_foreign_key(1)
    print("All data seeded successfully!")
