# Databricks notebook source
import random


# COMMAND ----------

print('this is the utils notebook!')

# COMMAND ----------

def get_random_number():
    return random.random()

# COMMAND ----------

def get_param(param_name, default):
    try:
        p = dbutils.widgets.get(param_name)
    except:
        p = default
    print(f"param {param_name} run with value {p}")
    return p
