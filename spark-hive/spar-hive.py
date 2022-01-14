
from pyspark.sql import SparkSession


spark=SparkSession.builder.master("local[1]").appName("pysparkdf").enableHiveSupport().getOrCreate()


#dataframe using spark object by reading csv file
df = spark.read.option("header", "true").csv("/home/zeinab/cereal.csv")

df.show(5)

df.printSchema()

df.select('name', 'mfr', 'rating').show(10)

#These two functions are used to find out if there is any null value present in the DataFrame

#filter data by null values

from pyspark.sql.functions import *

df.filter(df.name.isNotNull()).show()

df.filter(df.name.isNull()).show()


#The withColumn function is used to manipulate a column or to create a new column with the existing column.

df.withColumn("Calories",df['calories'].cast("Integer")).printSchema()

#The groupBy function is used to collect the data into groups on DataFrame and allows us to perform aggregate functions on the grouped data.

df.groupBy("name", "calories").count().show()


#The split() is used to split a string column of the dataframe into multiple columns.

from pyspark.sql.functions import split

df1 = df.withColumn('Name1', split(df['name'], " ").getItem(0))
.withColumn('Name2', split(df['name'], " ").getItem(1))
df1.select("name", "Name1", "Name2").show()


#The lit function is used to add a new column to the dataframe that contains literals or some constant value.

from pyspark.sql.functions import lit
from pyspark.sql.functions import col

df2 = df.select(col("name"),lit("75 gm").alias("intake quantity"))

df2.show()

#The orderBy function is used to sort the entire dataframe based on the particular column of the dataframe

df3.orderBy("protein").show()

#The when the function is used to display the output based on the particular condition. It evaluates the condition provided and then returns the values accordingly.

from pyspark.sql.functions import when
df.select("name", when(df.vitamins >= "25", "rich in vitamins")).show()

#The filter function is used to filter data in rows based on the particular column values.

from pyspark.sql.functions import filter
df.filter(df.calories == "100").show()

#These two functions are used to find out if there is any null value present in the DataFrame

#filter data by null values

from pyspark.sql.functions import *

df.filter(df.name.isNotNull()).show()

df.filter(df.name.isNull()).show()

#Save to a Hive database

df.write.mode("overwrite").saveAsTable("cereal.test_table")
df_sql = spark.sql("select * from cereal.test_table")

df1.write.mode("overwrite").saveAsTable("cereal.test_table1")
df1_sql = spark.sql("select * from cereal.test_table1")

df2.write.mode("overwrite").saveAsTable("cereal.test_table2")
df2_sql = spark.sql("select * from cereal.test_table2")

df3.write.mode("overwrite").saveAsTable("cereal.test_table2")
df3_sql = spark.sql("select * from cereal.test_table2")

#Show query result

df_sql.show()
df1_sql.show()
df2_sql.show()
df3_sql.show()
