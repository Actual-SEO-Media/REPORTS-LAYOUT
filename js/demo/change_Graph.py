import pandas as pd 
import ftplib
import asyncio
from pyodide import create_proxy, to_js
from js import updateBarChart
from pyodide import create_proxy

HOSTNAME = "ftp.actualseomedia.com"
USERNAME = "actual18"
PASSWORD = "Actualseo5150!"

ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

ftp_server.encoding = "utf-8"

filename = "public_html//reports//abba//data//ReportGraphC.csv"

file = "ReportGraphC.csv"

    # Command for Downloading the file "RETR filename"

async def FTP_RETRIEVE():
    
    ftp_server.login()                     # user anonymous, passwd anonymous@
    await ftp_server.retrbinary(f"RETR {filename}", open(file, "wb").write)
    await asyncio.Event().wait()

FTP_RETRIEVE()

file= open(file, "r")

DF_REPGRH = pd.DataFrame(data=file)

ARRAY_REPGRH = pd.array(DF_REPGRH[0][1:5])

ARRAY_GRHC = []

def JS_ARRAY():

    for i in range(len(ARRAY_REPGRH)):
        NEW_ELEMENT = ARRAY_REPGRH[i].replace("\n", "")

        ARRAY_GRHC.append(NEW_ELEMENT)

    updateBarChart(to_js(ARRAY_GRHC))

proxy = create_proxy(JS_ARRAY)

JS_ARRAY
