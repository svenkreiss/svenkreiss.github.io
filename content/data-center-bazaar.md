Title: The Data Center and the Bazaar
Date: 2014-08-14
Category: Tech
Tags: Docker, Go, HPC, peer-to-peer, distributed
Slug: data-center-bazaar
Summary: Concept for peer-to-peer computing.
Status: draft


{% img img-thumbnail float-right /images/bazaar.png 150 dockbroker icon %}
This is a concept for peer-to-peer computing. The goal is to use a heterogeneous set of computers to run analyses on data. The computers might be the local machine, a remote desktop, an AWS EC2 instance, an [AWS Elastic Beanstalk app](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.html), a node on the [Google Compute Engine](https://developers.google.com/compute/docs/containers) or some other real or virtual machine. All these machines have access to data in the form of `s3://*`, `hdfs://*`, `file://*`, `ssh://*`, `http://*` or some other means which might be slow or fast and cheap or expensive.


## Flow

Assigning priorities to jobs or setting up priority queues on clusters is tedious and usually not very effective. Simple `PBS queue` systems don't even have priorities, but all users just submit all their jobs to the same queue. Jobs are submitted to a central manager and get executed on the next available compute node. The data then has to be copied to that node.

The idea behind this post is more similar to a bazaar where there is no central manager. Every _client_ knows at least one _broker_ which is a manager of a single compute node. Brokers know each other and can refer clients. To submit a job, the client asks a subset of the brokers that it knows for an _offer_ based on a description of the job. The offer is made in US$ and comes with an expected completion time. The broker makes that offer based on the prices that are given by the cloud provider or (partially) free for local machines. The client picks the cheapest offer taking the estimated completion time into account.

Clients can build reputation in brokers when they deliver on time and still prefer more expensive brokers. Brokers can also build reputation of clients when their estimated run times and required resources match the job description the offer was based on. If that is not the case and a client repeatedly underestimates job processing times, the broker could add extra fees.

At this point, the offers are only used to find the best place to run the job. No money is actually transfered and that is just fine. However, one could go one step further and have digital coins (something like Bitcoin) just for this set of machines. People in an organization can be given a monthly amount of coins and then pay for their compute jobs. This would make users more conscious of the resources they are using and would limit a combined "cpu+memory+data" quota. At the same time, it would act as a security measure as people without this coin would not be able to use the resources. (For the cryptocurrency experts: one could use [smart contracts](http://en.wikipedia.org/wiki/Smart_contract) and maybe [colored coins](https://docs.google.com/document/d/1AnkP_cVZTCMLIzw4DvsW6M8Q2JC0lIzrTLuoWu2z1BE).)



## Technical Suggestion: `dockbroker`

To make things a bit more concrete, here is an example interface. It uses [Docker](https://www.docker.com/) which is advertised with _"Build, Ship and Run Any App, Anywhere"_ and _"An open platform for distributed applications for developers and sysadmins"_. It is a little bit like a virtual machine, but uses the same kernel as the host and therefore it is fast. You can run a JVM inside it, but you can also run plain C.

### Job

A job is defined by a `Dockerfile` and a `manifest` either in a local directory or inside a remote repository (for example on GitHub). The broker will use the Dockerfile to see which slices of the Docker image it has cached (and reduce the price). The manifest is used to quantify the price of resources.

Example of a simple `manifest` file:

    {
        "Name": "Test job 1",
        "Submitter": "Sven Kreiss <me@svenkreiss.com>",
        "MaxDuration": "24h",
        "EstDuration": "12h",
    }

This job has access to unspecified `InputResources` and `OutputResources` (see advanced example below) but brokers who have easy access to those resources wont be able to make better offers than any other broker. Large files should always be specified because neglecting to specify expensive resources could lead to bad reputation.

Example of an advanced `manifest` file:

    {
        "Name": "Test job 2",
        "Submitter": "Sven Kreiss <me@svenkreiss.com>",
        "MaxDuration": "24h",
        "EstDuration": "12h",
        "RAM": "4GB",
        "GPU": "nvidia",
        "JobArray": 64,
        "RequireParallelExecution": true,
        "InputResources": [
            {
                "CacheLifeTime": "1h",
                "Size": "1MB",
                "Md5": "12345678901234567890",
                "Locations": [
                    "file://home/svenkreiss/data/some_data.csv",
                    "s3://testbucket/some_data.csv",
                ],
            },
            {
                "JobArray": "0-31",
                "CacheLifeTime": "forever",
                "Size": "500MB",
                "Md5": "12345678901234567891",
                "Locations": [
                    "hdfs://some_path/some_file_0.tar.gz"
                ],
            },
            {
                "JobArray": "32-63",
                "CacheLifeTime": "forever",
                "Size": "500MB",
                "Md5": "12345678901234567892",
                "Locations": [
                    "hdfs://some_path/some_file_1.tar.gz"
                ],
            },
        ],
        "OutputResources": [
            {"Size": "1MB", "Location": "file://home/svenkreiss/job/test_job_1.csv"},
            {"Size": "1KB", "Location": "file://home/svenkreiss/job/test_job_1.log"},
        ],
    }

Parallel jobs that are communicating are created by setting `"RequireParallelExecution": true` which will tell the broker to take only as many jobs as can be run in parallel. Other jobs have to be left to other brokers. The estimated time for completion will have to take into account that all jobs have to run in parallel.

### Nodes running `dockbroker`

Every compute node runs a `dockbroker`. `dockbroker`s advertise their existence to other `dockbroker`s. Clients can ask "Who else do you know?" to discover other brokers to get alternative offers. Brokers create offers and handle the scheduling of jobs.
Nodes that have data locally available or already cached part of the Docker image (a `slice`) are cheaper and therefore preferred. When data has to be downloaded to and uploaded from the node, the price for the bandwidth as well as the extra time are taken into account in the offer. Bandwidth price and download times depend on the location of the source (e.g. it is cheaper to download data from [AWS S3](http://aws.amazon.com/s3/) when the job is run on [AWS EC2](http://aws.amazon.com/ec2/); see [AWS S3 pricing](http://aws.amazon.com/s3/pricing/)). This gives the system _data locality_. The estimated time to completion includes the estimated run times for jobs already in the queue.

### Clients pick Brokers

Generally, clients pick the cheapest broker. However, the estimated time for completion might be valuable. For a compute node, the value of time is linear as the price of keeping the machine running on a cloud provider is a fixed cost by the hour. The "pain" of waiting for a job to complete could increase quadratic or exponentially which will define a sweet spot for when it is appropriate to pay more for a faster compute node.

## Use Cases

`dockbroker` just sets up environments. The actual parallelized execution, collection of results, data management, etc. has to be handled separately. You could imagine running an [ipcluster](http://ipython.org/ipython-doc/dev/parallel/parallel_intro.html) with it (popular in the `IPython` community) or running an [Apache Spark](https://spark.apache.org/) cluster. Sometimes you just need different software versions in your cluster (like different versions of [R](http://www.r-project.org/) or [ROOT](http://root.cern.ch)) or different resources (e.g. a GPU) and `dockbroker` can find the best place for the job and create the virtual environment.


## Why?

Because I need it. However, it is not like I am creating distributed computing environments every day. I am more a user of HPC, but it sounds like an interesting project to implement in [Go](http://golang.org/) (Docker is written in [Go](http://golang.org/)). Contributions to [dockbroker on github](https://github.com/svenkreiss/dockbroker) are very welcome.
