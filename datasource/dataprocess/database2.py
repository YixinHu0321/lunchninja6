import psycopg2
import csv
import math
import os
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


DATABASE_URL = os.environ['DATABASE_URL']

# Thanks to https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
def getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the earth in km
    dLat = deg2rad(lat2 - lat1)  # deg2rad below
    dLon = deg2rad(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(deg2rad(lat1)) * math.cos(
        deg2rad(lat2)
    ) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    # Distance in km
    return d


def deg2rad(deg):
    return deg * (math.pi / 180)





def importschool():
    # let postgres start: pg_ctl -D /usr/local/var/postgres start
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS homepage_school")
    cur.execute("CREATE TABLE homepage_school (name VARCHAR, id INTEGER)")
    filepath = "/../School.csv"
    with open(
        filepath, "r", encoding="UTF-8-sig"
    ) as fin:  # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        for i in dr:
            print(i)
            cur.execute(
                "INSERT INTO homepage_school (name, id) VALUES (%s, %s)", (i["Name"], i["id"])
            )

    conn.commit()
    conn.close()
    print("imported school data")
    return ()


def importdepartment():
    # let postgres start: pg_ctl -D /usr/local/var/postgres start
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS homepage_department")
    cur.execute(
        "CREATE TABLE homepage_department (name VARCHAR, school INTEGER, id INTEGER, description VARCHAR)"
    )
    filepath2 = "/../Department.csv"
    with open(
        filepath2, "r", encoding="UTF-8-SIG"
    ) as fin2:  # `with` statement available in 2.5+
        dr2 = csv.DictReader(fin2)  # comma is default delimiter
        for i in dr2:
            cur.execute(
                "INSERT INTO homepage_department (name, school, id, description) VALUES (%s, %s, %s, %s)",
                (i["Name"], i["School"], i["id"], i["Description"]),
            )

    conn.commit()
    conn.close()
    print("imported restaurant data")
    return ()


def importrestaurant():
    # let postgres start: pg_ctl -D /usr/local/var/postgres start
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS homepage_restaurant")
    cur.execute(
        "CREATE TABLE homepage_restaurant (id INTEGER, name VARCHAR, cuisine VARCHAR, score INTEGER, borough VARCHAR, building VARCHAR, street VARCHAR, zipcode VARCHAR, phone VARCHAR, latitude VARCHAR, longitude VARCHAR)"  # noqa: E501
    )
    filepath3 = "/../DOHMH_New_York_City_Restaurant_Inspection_Results.csv"
    with open(
        filepath3, "r", encoding="UTF-8"
    ) as fin3:  # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr3 = csv.DictReader(fin3)  # comma is default delimiter
        lat = [40.694340, 40.729010, 40.737570]
        log = [
            -73.986110,
            -73.996470,
            -73.978070,
        ]  # tandon, college of art and science , nursing
        for i in dr3:
            if (
                i["Latitude"] in ("", None)
                or i["Longitude"] in ("", None)
                or i["SCORE"] in ("", None)
            ):
                continue
            rid = int(i["CAMIS"])
            latitude = float(i["Latitude"])
            longitude = float(i["Longitude"])
            score = int(i["SCORE"])
            if score > 30:
                continue
            for j in range(3):
                distance = getDistanceFromLatLonInKm(
                    lat[j], log[j], latitude, longitude
                )
                if distance <= 1.5:
                    cur.execute(
                        "SELECT COUNT(*) FROM homepage_restaurant WHERE id == "
                        + str(rid)
                    )
                    count = cur.fetchone()
                    if int(count[0]) == 0:
                        cur.execute(
                            "INSERT INTO homepage_restaurant (id, name, cuisine, score, borough, building, street, zipcode, phone, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",  # noqa: E501
                        (
                            i["CAMIS"],
                            i["DBA"],
                            i["CUISINE DESCRIPTION"],
                            i["SCORE"],
                            i["BORO"],
                            i["BUILDING"],
                            i["STREET"],
                            i["ZIPCODE"],
                            i["PHONE"],
                            i["Latitude"],
                            i["Longitude"],
                        ),
                        
                    else:
                        cur.execute(
                            "SELECT score FROM homepage_restaurant WHERE id == "
                            + str(rid)
                        )
                        score = cur.fetchone()
                        if int(i["SCORE"]) < int(score[0]):
                            cur.execute(
                                "UPDATE homepage_restaurant SET score = "
                                + i["SCORE"]
                                + " WHERE id = "
                                + str(rid)
                            ))
    # cur.execute(
    #     "DELETE FROM homepage_restaurant a USING restaurant b WHERE a.score > b.score AND a.id = b.id"
    # )

    # cur.execute(
    #     "DELETE FROM homepage_restaurant a WHERE a.ctid <> (SELECT min(b.ctid) FROM   restaurant b WHERE  a.id = b.id)"
    # )

    conn.commit()
    conn.close()
    print("imported restaurant data")
    return ()


def importcuisine():
    # let postgres start: pg_ctl -D /usr/local/var/postgres start
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS cuisine")
    cur.execute("CREATE TABLE cuisine (name VARCHAR, id INTEGER)")
    cur.execute("SELECT DISTINCT cuisine FROM restaurant")
    count = cur.fetchall()
    id = 0
    for each in count:
        cur.execute("INSERT INTO cuisine (name, id) VALUES (%s, %s)", (each, id))
        id = id + 1

    conn.commit()
    conn.close()
    return ()


def main():
    importschool()
    importdepartment()
    importrestaurant()
    importcuisine()
    # retrieveschool()
    # retrievedepartment('Tandon School of Engineering')
    return ()


main()