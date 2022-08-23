# Copyright 2021 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to export the results from a select statement into a csv file.

import csv
import os
import teradatasql

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        cur.execute ("create volatile table voltab (c1 integer, c2 varchar(100)) on commit preserve rows")

        print ("Inserting data")
        cur.execute ("insert into voltab values (?, ?)", [
            [1, ""],
            [2, "abc"],
            [3, "def"],
            [4, "mno"],
            [5, ""],
            [6, "pqr"],
            [7, "uvw"],
            [8, "xyz"],
            [9, ""],
        ])

        sFileName = "dataPy.csv"
        print ("Exporting table data to file", sFileName)
        cur.execute ("{fn teradata_write_csv(" + sFileName + ")}select * from voltab order by 1")

        try:
            print ("Reading file", sFileName)
            with open (sFileName, "rt", encoding="UTF8") as f:
                [ print (row) for row in csv.reader (f) ]

        finally:
            os.remove (sFileName)
