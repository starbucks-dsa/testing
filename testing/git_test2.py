# Databricks notebook source
test_var = "This is a tester from git_test2"

# COMMAND ----------

test_branch = "This is a tester from dev branch"

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC create table temp_v as
# MAGIC select * from dsa_yanyan.temp_table_dev;
