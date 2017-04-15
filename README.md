# udacity_hadoop_mapreduce
Udacity - Intro to Hadoop and MapReduce by Cloudera

This repository contains source codes to the course available on Udacity - <a href="https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617">Intro to Hadoop and MapReduce by Cloudera</a>

Command to run scripts:
sudo -u hdfs hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.8.0.jar -mapper 'python mapper_file.py' -reducer 'python reducer_file.py' -file mapper_file.py -file reducer_file.py -input path_to_input_file -output path_to_output_directory
