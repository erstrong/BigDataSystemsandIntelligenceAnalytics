import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import SQLContext
import os

# Start Spark

sc = pyspark.SparkContext(appName="graph")

sqlContext = SQLContext(sc)

# Import CSVs to DataFrames

inputPath1 = "graphdata/people_images.csv"
vertices = sqlContext.read.options(header='true', inferSchema='true').csv(inputPath1)

print('Vertices:')
vertices.show(5)

inputPath2 = "graphdata/imagelabels.csv"
edges = sqlContext.read.options(header='true', inferSchema='true').csv(inputPath2)
print('Edges:')
edges.show(5)

print('Schemas:')
vertices.printSchema()
edges.printSchema()

# Start GraphFrames

sc.addPyFile(os.path.expanduser('~/.ivy2/jars/graphframes_graphframes-0.5.0-spark2.1-s_2.11.jar'))

from graphframes import *

g = GraphFrame(vertices, edges)
print('Graph:')
print(g)


print('In Degrees:')
g.inDegrees.show()

print('Label Edges')
g.edges.filter("relationship = 'label'").count()

print('Errata Edges')
g.edges.filter("relationship = 'errata'").count()

sc.setCheckpointDir("checkpoints")
print('Connected Components')
g.connectedComponents().show()

print('Strongly Connected Components')
g.stronglyConnectedComponents(maxIter=10).show()

results = g.pageRank(resetProbability=0.15, tol=0.01)
print('Page Rank Vertices')
results.vertices.show()

print('Page Rank Edges')
results.edges.show()

print('Centrality analysis:')
print('George W Bush')
g.edges.filter("dst = 'George_W_Bush'").count()
print('Most connected')
t = g.edges.groupby("dst").count().orderBy("count", ascending=False)
t.show()

sc.stop()