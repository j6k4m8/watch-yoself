<!DOCTYPE html>
<html>
<head>
	<script	src="//cdnjs.cloudflare.com/ajax/libs/d3/3.4.6/d3.min.js"></script>
	<script	src="rickshaw.js"></script>

	<title>watch</title>
</head>
<body>
	<div id="chart"></div>

	<script src="out.watch"></script>
	<script>
	data = {};
	var i = 0;
	for (var date in _d) {
		for (var filename in _d[date]) {
			if (!data[filename]) {
				data[filename] = {
					'color': 'steelblue',
					'data': []
				};
			}
			data[filename].data.push({
				'x': i,
				'y': (_d[date][filename])
			});
		}
		i++;
	}
	var displayData = [];
	for (var datum in data) {
		displayData.push(data[datum]);
	}

	var graph = new Rickshaw.Graph( {
	    element: document.querySelector("#chart"),
	    width: 900,
	    height: 400,
	    stroke: true,
	    renderer: 'area',
	    series: displayData
	});

	graph.renderer.unstack = true;
	graph.render();

	window.setTimeout(function(){window.location = window.location.toString()}, 5000);

	</script>
</body>
</html>
