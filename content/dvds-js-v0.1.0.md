Title: dvds-js version 0.1.0
Date: 2014-04-25
Category: Tech
Tags: dvds-js, JavaScript, d3.js, distributed, version control
Slug: dvds-js-v0.1.0
Status: draft
Summary: Distributed Versioned Data Structures in JavaScript. Like git in js.


<style>
/* graph styles */
      svg {
        border:1px solid #faa;
        background-color:#fee;
      }
      .link {
        stroke: #000;
        stroke-width: 1.5px;
      }
      .node circle {
        fill: #000;
        stroke: #fff;
        stroke-width: 1.5px;
      }
      .node text {
        text-anchor: middle;
      }
</style>

<script src="http://s3.amazonaws.com/flaskApp_static/static/d3/d3.v3.min.js" charset="utf-8"></script>
<script src="http://requirejs.org/docs/release/2.1.2/minified/require.js"></script>
<script>
require.config({
    paths: {
        'crypto-js.SHA3': 'http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/sha3',
        'dvds': 'http://svenkreiss.github.io/dvds-js/lib/dvds.min',
        'dvds.visualize': 'http://svenkreiss.github.io/dvds-js/lib/dvds.min',
    },
    shim: {
        'crypto-js.SHA3': {
            exports: 'CryptoJS'
        }
    }
});
</script>

> Distributed Versioned Data Structures in JavaScript. Like git in js.  
> Checkout the code on [github.com/svenkreiss/dvds-js](http://github.com/svenkreiss/dvds-js).


The aim of `dvds-js` is to have data structures in JavaScript that you can `fork()`, serialize and send over the wire, `commit()` to and then stream back and `merge()` with full conflict resolution. Here, _data structures_ means anything that can be serialized with JSON.

This post is about the first development release, version 0.1.0.



## Example

A repository `a` is created holding an array with the two names `Paul` and `Adam`. Then this repository is forked and the fork is called `b`. Both `a` and `b` are then modified. To demonstrate streaming capabilities, repository `b` is stringified before and after the manipulation. At the end `b` is merged into `a` and the result is shown below.

	:::JavaScript
	require(['dvds', 'dvds.visualize'], function() {
		var a = new dvds.Repository(['Paul','Adam']);
		var b = a.fork();
		var bString = JSON.stringify(b);

		// send bString to a different machine and make it a repository again
		var bStreamed = dvds.Repository.parseJSON( JSON.parse(bString) );
		bStreamed.data[0] = 'Karl';
		bStreamed.data[1] = 'Peter';
		// convert to a string again to send back
		var bStreamedString = JSON.stringify(bStreamed);

		// meanwhile on a
		a.data[0] = 'Paula';

		// receive the modified b repository
		var bReceived = dvds.Repository.parseJSON( JSON.parse(bStreamedString) );
		a.merge(bReceived);

	    // update html output
	    $("#test1Out").text(JSON.stringify(a.data));

	    // visualize
	    dvds.visualize.CommitGraph(d3.select('#test1Graph'))(a);
        dvds.visualize.CommitGraph(d3.select('#test2Graph'))(bReceived);
	});


__Live output__: <span id="test1Out">?</span>

Edit on [http://jsfiddle.net/svenkreiss/3Ruat/10/](http://jsfiddle.net/svenkreiss/3Ruat/10/).



### Graph of Commits

Repositories are created with commit 0 shown on the left and then develop towards the right with the last commit on the far right. The second graph shows a merge of `a` and `b` as the last commit. This is a live visualization of the two repositories in the example.

Repository `b`:

<svg height="150" width="600" id="test2Graph"></svg>


Repository `a` merged with `b`:

<svg height="150" width="600" id="test1Graph"></svg>





## Features

* special merge algorithms for nested arrays and objects (e.g. arrays inside of objects inside of arrays inside of an object)
* commit hash is built over the commit's data, but also over the entire parent-tree which means that the commit id can validate the entire parent-tree
* a repository exposes the `data` member that behaves like a normal js variable (e.g. can be used in `angular.js` directly)
* visualization (currently only `CommitGraph`) is factored into its own submodule `visualize`
* unit tests run with `Jasmine` and `Karma`, `jscs` is used to check code style, `uglify` is used to build min version and automation is done with `grunt`


## Setup

`dvds-js` is an [AMD library](http://requirejs.org/docs/whyamd.html#amd). You can load it using `require-js` in the browser as in the example above. The setup looks something like this:

    :::JavaScript 
    <script src="http://s3.amazonaws.com/flaskApp_static/static/d3/d3.v3.min.js" charset="utf-8"></script>
    <script src="http://requirejs.org/docs/release/2.1.2/minified/require.js"></script>
    <script>
    require.config({
        paths: {
            'crypto-js.SHA3': 'http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/sha3',
            'dvds': 'http://svenkreiss.github.io/dvds-js/lib/dvds.min',
            'dvds.visualize': 'http://svenkreiss.github.io/dvds-js/lib/dvds.min',
        },
        shim: {
            'crypto-js.SHA3': {
                exports: 'CryptoJS'
            }
        }
    });
    </script>

This includes `d3.js` for visualizations and `CryptoJS` is needed for calculating unique identifiers for commits.
In `node.js`, this setup is not necessary and you would simply use `require()`.




<script>
require(['dvds', 'dvds.visualize'], function() {
    
    var a = new dvds.Repository(['Paul', 'Adam']);
    var b = a.fork();
    var bString = JSON.stringify(b);
    
    // send bString to a different machine and make it a repository again
    var bStreamed = dvds.Repository.parseJSON(JSON.parse(bString));
    bStreamed.data[0] = 'Karl';
    bStreamed.data[1] = 'Peter';
    // convert to a string again to send back
    var bStreamedString = JSON.stringify(bStreamed);
    
    // meanwhile on a
    a.data[0] = 'Paula';
    
    // receive the modified b repository
    var bReceived = dvds.Repository.parseJSON(JSON.parse(bStreamedString));
    a.merge(bReceived);
    
    // update html output
    $("#test1Out").text(JSON.stringify(a.data));

    // visualize
    dvds.visualize.CommitGraph(d3.select('#test1Graph'))(a);
    dvds.visualize.CommitGraph(d3.select('#test2Graph'))(bReceived);
});
</script>