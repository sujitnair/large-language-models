# Databricks notebook source

# COMMAND ----------

import os

# Setup UC Volume
catalog = 'llmmoocs'
schema = 'default'
hf_volume = "huggingface"
data_volume = "data"

query = f"""
    CREATE CATALOG IF NOT EXISTS %s
    """ % catalog
spark.sql(query)

query = f"""
    CREATE VOLUME IF NOT EXISTS %s.%s.%s
    """ % (catalog, schema, hf_volume)
spark.sql(query)

query = f"""
    CREATE VOLUME IF NOT EXISTS %s.%s.%s
    """ % (catalog, schema, data_volume)
spark.sql(query)


hf_home = "/Volumes/"+catalog+"/" + schema + "/huggingface"
# Set environment variables
os.environ["HF_HOME"] = hf_home
os.environ["HF_DATASETS_CACHE"] = hf_home + "/datasets"
os.environ["TRANSFORMERS_CACHE"] = hf_home + "/models"

# Assuming DA is a module or an existing object, set its attributes
# If DA isn't yet defined, you can define it as a class or a simple object first

# For instance, if you don't have DA defined yet, you can do:
class DataAttributes:
    paths = None
    username = None

DA = DataAttributes()
DA.paths = DataAttributes()  # set up the paths sub-object

DA.paths.datasets = "/Volumes/" + catalog + "/" + schema + "/data"
DA.paths.working_dir = DA.paths.datasets + "/working_dir"

# Assuming you're in a Databricks environment, figure out username using dbutils:
# Please replace the placeholder below with the actual method to retrieve the username in your Databricks environment
# ChatGPT messed up!
# DA.username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get("user")

DA.username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()
print(DA.username)  # to verify the value of username


# COMMAND ----------

