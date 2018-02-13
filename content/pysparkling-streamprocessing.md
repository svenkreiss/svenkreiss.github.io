Title: Stream Processing in pysparkling
Date: 2017-03-11
Category: Tech
Tags: data, Python, distributed
Slug: streamprocessing-in-pysparkling
Summary: pysparkling now supports stream processing with discrete streams, called DStream. This post shows a simple example that uses this new API.
Status: published

`pysparkling` is a native Python implementation of PySpark. Stream processing
is considered to be one of the most important features of Spark. PySpark
provides a Python interface to Spark’s
[StreamingContext](http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html)
and supports consuming from updating HDFS folders and TCP sockets and provides
interfaces to Kafka, Kinesis, Flume and MQTT. Initial support for stream
processing from folders and TCP sockets is in `pysparkling 0.4.0` which you can
now install with:

```sh
pip install --upgrade pysparkling
```

## Counting Example

In the normal batch processing way, you can count elements with:

```python
>>> from pysparkling import Context
>>> Context().parallelize([1, 2, 3]).count()
3
```

This is similar for stream processing. Incoming data is batched every
0.1 seconds (the batch interval — the second parameter to `StreamContext`) and
elements are counted in 0.2 second windows, i.e. two batch intervals, which
returns the count of the first batch, the count of the first and second batch
and the count of the second and third batch:

```python
>>> import pysparkling
>>> sc = pysparkling.Context()
>>> ssc = pysparkling.streaming.StreamingContext(sc, 0.1)
>>> (
...     ssc
...     .queueStream([[1, 1, 5], [5, 5, 2, 4], [1, 2]])
...     .countByWindow(0.2)
...     .foreachRDD(lambda rdd: print(rdd.collect()))
... )
>>> ssc.start()
>>> ssc.awaitTermination(0.35)
[3]
[7]
[6]
```

Other new features apart from the `pysparkling.streaming` module are an
improved `pysparkling.fileio` module, methods for reading binary files
([binaryFiles()](http://pysparkling.trivial.io/en/latest/api_context.html#pysparkling.Context.binaryFiles) and
[binaryRecords()](http://pysparkling.trivial.io/en/latest/api_context.html#pysparkling.Context.binaryRecords))
and more inline examples in the documentation.

Head over to the [RDD (batch datasets)](http://pysparkling.trivial.io/en/latest/api_rdd.html) and
[DStream (discrete stream)](http://pysparkling.trivial.io/en/latest/api_streaming.html#dstream)
documentations to learn more!

[![API documentation at pysparkling.trivial.io](/images/pysparkling_streaming_doc.png)](http://pysparkling.trivial.io)
