from django.shortcuts import render
import pandas as pd
import pyodbc
from apps.analysis_rb.config_db import DB_CONFIG

def fatch_and_analysis_data(request):
    # conn_str = (
    #     f"DRIVER={DB_CONFIG['DRIVER']};"
    #     f"SERVER={DB_CONFIG['SERVER']};"
    #     f"DATABASE={DB_CONFIG['DATABASE']};"
    #     f"Trusted_Connection={DB_CONFIG['Trusted_Connection']};"
    # )

    conn_str = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-R7KSJK2\\SQLEXPRESS;'
            'DATABASE=CSE_82;'
            'Trusted_Connection=yes;'
        )

    query = "SELECT * FROM google_salaries"
    df = pd.read_sql(query, conn_str)
    print(df)

    return render(request,'analysis_rb/analysis.html')


