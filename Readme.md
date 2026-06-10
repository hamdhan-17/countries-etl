# Countries ETL Pipeline

## Overview

This project extracts country data from the Rest Countries API, transforms the data, and loads it into PostgreSQL.

## Technologies Used

* Python
* Requests
* PostgreSQL
* Psycopg2
* Apache Airflow

## ETL Workflow

Rest Countries API

↓

Extract

↓

Transform

↓

Load

↓

PostgreSQL

## Data Collected

* Country Name
* Capital
* Region
* Population

## Files

* countries_etl.py - Main ETL script
* test_api.py - API testing script

## Future Improvements

* Schedule using Apache Airflow
* Add data quality checks
* Create dashboards
