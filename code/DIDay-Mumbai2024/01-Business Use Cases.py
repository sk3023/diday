# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC # Business Use Cases

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC # Use Case 1- BFSI
# MAGIC # Credit Decisioining
# MAGIC <br>
# MAGIC <img src="https://raw.githubusercontent.com/sk3023/diday/main/Images/credit-dec.png" width="700px" style="float:left; margin-left: 0px"/>
# MAGIC <br>
# MAGIC
# MAGIC
# MAGIC # Dataset: #
# MAGIC - ### <u> **Internal banking**</u> data *(KYC, accounts, collections, applications, relationship)* come from the bank's internal relational databases and is ingested *once a day* through a CDC pipeline, ###
# MAGIC - ### <u> **Credit Bureau**</u> data (usually in XML or CSV format and *accessed monthly* through API) comes from government agencies (such as a central banks) and contains a lot of valuable information for every customer. We also use this data to re-calculate whether a user has defaulted in the past 60 days, ###
# MAGIC - ### <u> **Partner** </u> data - used to augment the internal banking data and ingested *once a week*. In this case we use telco data in order to further evaluate the character and creditworthiness of banking customers,
# MAGIC - ### <u> **Fund transfer** </u> are the banking transactions (such as credit card transactions) and are *available real-time* through Kafka streams.###
# MAGIC

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC # Use Case 2- Manufacturing
# MAGIC # Wind Turbine Predictive Maintenance 
# MAGIC <br>
# MAGIC <img src="https://github.com/QuentinAmbard/databricks-demo/raw/main/manufacturing/wind_turbine/turbine-photo-open-license.jpg" width="800px" style="float:left; margin-right: 40px"/>
# MAGIC <br>
# MAGIC
# MAGIC ### <u> Predictive maintenance examples include:</u>
# MAGIC - ### Predict mechanical failure in an energy pipeline ###
# MAGIC - ### Detect abnormal behavior in a production line ###
# MAGIC - ### Optimize supply chain of parts and staging for scheduled maintenance and repairs ###
# MAGIC
# MAGIC ### <u> Dataset: </u>
# MAGIC - ### <strong>Turbine metadata</strong>: Turbine ID, location (1 row per turbine)
# MAGIC - ### <strong>Turbine sensor stream</strong>: Realtime streaming flow from wind turbine sensor (vibration, energy produced, speed etc)
# MAGIC - ### <strong>Turbine status</strong>: Historical turbine status based to analyse which part is faulty (used as label in our ML model)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC # Use case 3 - Retail
# MAGIC # Customer churn
# MAGIC <br>
# MAGIC <img src="https://raw.githubusercontent.com/sk3023/diday/main/Images/churn.png" width="700px" style="float:left; margin-right: 30px"/>
# MAGIC <br>
# MAGIC
# MAGIC ### <u> Dataset </u>
# MAGIC - ###Customer profile data *(name, age, address etc)*
# MAGIC - ###Orders history *(what our customer bought over time)*
# MAGIC - ###Events from our application *(when was the last time customers used the application, clicks, typically in streaming)*
# MAGIC

# COMMAND ----------


