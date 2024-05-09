# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC ## <img src="https://raw.githubusercontent.com/sk3023/diday/main/Images/Intro.png" style="float:left; margin: -35px 0px 0px 0px" width="1100px">
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %md-sandbox
# MAGIC ## <img src="https://raw.githubusercontent.com/sk3023/diday/main/Images/DataChal.png" style="float:left; margin: -35px 0px 0px 0px" width="1100px">

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC # Data engineering with Databricks - Commonly faced Challenges
# MAGIC
# MAGIC Building an Data platform requires to ingest multiple datasources.  
# MAGIC
# MAGIC It's a complex process requiring batch loads and streaming ingestion to support real-time insights, used for real-time monitoring among others.
# MAGIC
# MAGIC Ingesting, transforming and cleaning data to create clean SQL tables for our downstream user (Data Analysts and Data Scientists) is complex.
# MAGIC
# MAGIC <link href="https://fonts.googleapis.com/css?family=DM Sans" rel="stylesheet"/>
# MAGIC <div style="width:300px; text-align: center; float: right; margin: 30px 60px 10px 10px;  font-family: 'DM Sans'">
# MAGIC   <div style="height: 300px; width: 300px;  display: table-cell; vertical-align: middle; border-radius: 50%; border: 25px solid #fcba33ff;">
# MAGIC     <div style="font-size: 70px;  color: #70c4ab; font-weight: bold">
# MAGIC       73%
# MAGIC     </div>
# MAGIC     <div style="color: #1b5162;padding: 0px 30px 0px 30px;">of enterprise data goes unused for analytics and decision making</div>
# MAGIC   </div>
# MAGIC   <div style="color: #bfbfbf; padding-top: 5px">Source: Forrester</div>
# MAGIC </div>
# MAGIC
# MAGIC <br>
# MAGIC
# MAGIC ## <img src="https://github.com/databricks-demos/dbdemos-resources/raw/main/images/de.png" style="float:left; margin: -35px 0px 0px 0px" width="80px"> John, as Data engineer, spends immense time….
# MAGIC
# MAGIC
# MAGIC * Hand-coding data ingestion & transformations and dealing with technical challenges:<br>
# MAGIC   *Supporting streaming and batch, handling concurrent operations, small files issues, GDPR requirements, complex DAG dependencies...*<br><br>
# MAGIC * Building custom frameworks to enforce quality and tests<br><br>
# MAGIC * Building and maintaining scalable infrastructure, with observability and monitoring<br><br>
# MAGIC * Managing incompatible governance models from different systems
# MAGIC <br style="clear: both">
# MAGIC
# MAGIC This results in **operational complexity** and overhead, requiring expert profile and ultimatly **putting data projects at risk**.
