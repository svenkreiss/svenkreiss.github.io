Title: pysparkling
Date: 2015-05-29
Category: Tech
Tags: data, distributed, Python
Slug: pysparkling-initial
Summary: A pure Python implementation of Apache Spark's RDD interfaces.
Status: published


`pysparkling` is a native Python implementation of the interface provided by
Spark’s RDDs. In Spark, RDDs are Resilient Distributed Datasets. An RDD
instance provides convenient access to the partitions of data that are
distributed on a cluster. New RDDs are created by applying transformations
like `map()` and `reduce()` to existing RDDs.

`pysparkling` provides the same functionality, but without the dependency on
the Java Virtual Machine, Spark and Hadoop. The original motivation came from
implementing a processing pipeline that is common for machine learning: process
a large number of documents in parallel for training a classification algorithm
(using Apache Spark) and using that trained classification algorithm in an
API endpoint where it is applied to a single document at a time. That single
document has to be preprocessed however with the same transformations that were
also applied during training. This is the task for pysparkling.

Removing the dependency on the JVM, Spark and Hadoop comes at a cost:

* Hadoop file io is gone, but its core functionality is reimplemented in
  `pysparkling.fileio`. This by itself is very handy as you can read the
  contents of files on `s3://`, `http://` and `file://` and optionally with
  gzip and bz2 compression just by specifying a file name. The name can
  include multiple comma separated files and the wildcards `?` and `*`.
* Managed resource allocation on clusters is gone (no YARN). Parallel
  execution with `multiprocessing` is supported though.

It also comes with some advanced features:

* Parallelization with any object that has a map() method. That includes
  `multiprocessing.Pool` and `concurrent.futures.ProcessPoolExecutor`.
* It does provide lazy and distributed execution. For example, when creating
  an RDD from 50,000 text files with
  `myrdd = Context().textFile('s3://mybucket/alldata/*.gz')` and only accessing
  one record with `myrdd.takeSample(1)`, `pysparkling` will only download a
  single file from S3 and not all 50,000.

## Quickstart

Install pysparkling with `pip install pysparkling`. As a first example,
count the number of occurrences of every word in `README.rst`:

```python
from pysparkling import Context
counts = (
    Context().textFile('README.rst')
    .flatMap(lambda line: line.split(' '))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)
print(counts.collect())
```

More examples including how to explore the Common Crawl dataset and the dataset
of the Human Biome Project are in this
[IPython Notebook](https://github.com/svenkreiss/pysparkling/blob/master/docs/demo.ipynb).

## Further Reading

Get an overview of the API and more details from
[pysparkling's documentation](http://pysparkling.trivial.io).
If you like this project, [star it on Github](https://github.com/svenkreiss/pysparkling),
tweet about it and follow me, @svenkreiss, on Twitter.
