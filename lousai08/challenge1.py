#!/bin/python

from pyspark import SparkConf, SparkContext

if __name__ == "__main__":

	# 1. Correct some mistake(s) here.
	conf = SparkConf().setAppName("Challenge").setMaster("local")
	
	sc = SparkContext(conf = conf)

	sc.setLogLevel("ERROR")

	# 2. Edit the path to file(s).
	input = sc.textFile("/home/shiyanlou/data/*")

	words = input.flatMap(lambda line: line.split(' '))

	counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

	# 3. Edit the lambda expression to finish code.
	top5 = counts.sortBy(lambda x:(x[1],x[0]),ascending = False).take(5)

	for x in top5:
		print(x)

	sc.stop()
