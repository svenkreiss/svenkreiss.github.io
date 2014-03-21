Title: dvds-js
Date: 2014-03-12
Category: Tech
Tags: open source, JavaScript, internet, data structures
Slug: dvds-js
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
> Checkout out the code on [github/svenkreiss/dvds-js](http://github.com/svenkreiss/dvds-js).


The aim of `dvds-js` is to have data structures in JavaScript that you can `fork()`, serialize and send over the wire, `commit()` to and then stream back and `merge()` with full conflict resolution.


## Loading the Library

`dvds-js` is an [AMD library](http://requirejs.org/docs/whyamd.html#amd). You can load it using `require-js` in the browser:

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

In `node.js` you would simply use `require`.



## Basic Example

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
	});


__Output__: <span id="test1Out">?</span>

Edit on [http://jsfiddle.net/svenkreiss/3Ruat/10/](http://jsfiddle.net/svenkreiss/3Ruat/10/).



### Graph of Commits

<svg height="150" width="600" id="test1Graph"></svg>




## 





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
});
</script>