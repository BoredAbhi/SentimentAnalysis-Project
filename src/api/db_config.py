# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 08:43:24 2020

@author: teeji
"""


import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
DEBUG = ENVIRONMENT == "dev"
HOST = '0.0.0.0' if ENVIRONMENT == "prod" else 'localhost'
POSTGRES_DB = os.environ.get("POSTGRES_DB", "postgres_db")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres_user")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password123")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)

