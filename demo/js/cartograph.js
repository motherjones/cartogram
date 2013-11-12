/*! Cartograph - v0.1.0 - 2013-11-12
* https://github.com/motherjones/cartograph
* Copyright (c) 2013 Mother Jones Data Desk; Licensed MIT */
"use strict";

if (!document.createElementNS) {
document.getElementsByTagName("form")[0].style.display = "none";
}

var percent = (function() {
    var fmt = d3.format(".2f");
    return function(n) { return fmt(n) + "%"; };
  })(),
  years = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
  fields = [
    {name: "UFO Sightings", id: "sightings", key: "sighting%d", years: years },
  ],
  fieldsById = d3.nest()
    .key(function(d) { return d.id; })
    .rollup(function(d) { return d[0]; })
    .map(fields),
  field = fields[0],
  year = years[0],
  colors = colorbrewer.RdYlBu[3]
    .reverse()
    .map(function(rgb) { return d3.hsl(rgb); });

var body = d3.select("body"),
  stat = d3.select("#status");

var fieldSelect = d3.select("#field")
.on("change", function(e) {
  field = fields[this.selectedIndex];
  location.hash = "#" + [field.id, year].join("/");
});

fieldSelect.selectAll("option")
.data(fields)
.enter()
.append("option")
  .attr("value", function(d) { return d.id; })
  .text(function(d) { return d.name; });

var yearSelect = d3.select("#year")
.on("change", function(e) {
  year = years[this.selectedIndex];
  location.hash = "#" + field.id + '/' +  year;
});

yearSelect.selectAll("option")
.data(years)
.enter()
.append("option")
  .attr("value", function(y) { return y; })
  .text(function(y) { return y; })

var map = d3.select("#map"),
  zoom = d3.behavior.zoom()
    .translate([-38, 32])
    .scale(.94)
    .scaleExtent([0.5, 10.0])
    .on("zoom", updateZoom),
  layer = map.append("g")
    .attr("id", "layer"),
  states = layer.append("g")
    .attr("id", "states")
    .selectAll("path");

// map.call(zoom);
updateZoom();

function updateZoom() {
var scale = zoom.scale();
layer.attr("transform",
  "translate(" + zoom.translate() + ") " +
  "scale(" + [scale, scale] + ")");
}

var proj = d3.geo.albersUsa(),
  topology,
  geometries,
  rawData,
  dataById = {},
  carto = d3.cartogram()
    .projection(proj)
    .properties(function(d) {
      return dataById[d.id];
    })
    .value(function(d) {
//FIXME
      return +d.properties[field];
    });

window.onhashchange = function() {
parseHash();
};

var segmentized = location.search === "?segmentized",
  url = ["data",
    segmentized ? "us-states-segmentized.topojson" : "us-states.topojson"
  ].join("/");
d3.json(url, function(topo) {
topology = topo;
geometries = topology.objects.states.geometries;
d3.csv("data/ufo_by_state.csv", function(data) {
  rawData = data;
  dataById = d3.nest()
    .key(function(d) { return d.Name; })
    .rollup(function(d) { return d[0]; })
    .map(data);
  init();
});
});

function init() {
var features = carto.features(topology, geometries),
    path = d3.geo.path()
      .projection(proj);

states = states.data(features)
  .enter()
  .append("path")
    .attr("class", "state")
    .attr("id", function(d) {
      return d.properties.Name;
    })
    .attr("fill", "#fafafa")
    .attr("d", path);

states.append("title");

parseHash();
}

function reset() {
stat.text("");
body.classed("updating", false);

var features = carto.features(topology, geometries),
    path = d3.geo.path()
      .projection(proj);

states.data(features)
  .transition()
    .duration(750)
    .ease("linear")
    .attr("fill", "#fafafa")
    .attr("d", path);


states.select("title")
  .text(function(d) {
    return d.properties.NAME;
  });
}

function update() {
var start = Date.now();
body.classed("updating", true);

var key = field.key.replace("%d", year),
    fmt = (typeof field.format === "function")
      ? field.format
      : d3.format(field.format || ","),
    value = function(d) {
      return +d.properties[key];
    },
    values = states.data()
      .map(value)
      .filter(function(n) {
        return !isNaN(n);
      })
      .sort(d3.ascending),
    lo = values[0],
    hi = values[values.length - 1];

var color = d3.scale.linear()
  .range(colors)
  .domain(lo < 0
    ? [lo, 0, hi]
    : [lo, d3.mean(values), hi]);

// normalize the scale to positive numbers
var scale = d3.scale.linear()
  .domain([lo, hi])
  .range([1, 1000]);

// tell the cartogram to use the scaled values
carto.value(function(d) {
  return scale(value(d));
});

// generate the new features, pre-projected
var features = carto(topology, geometries).features;

// update the data
states.data(features)
  .select("title")
    .text(function(d) {
      return [d.properties.NAME, fmt(value(d))].join(": ");
    });

states.transition()
  .duration(750)
  .ease("linear")
  .attr("fill", function(d) {
    return color(value(d));
  })
  .attr("d", carto.path);

var delta = (Date.now() - start) / 1000;
stat.text(["calculated in", delta.toFixed(1), "seconds"].join(" "));
body.classed("updating", false);
}

var deferredUpdate = (function() {
    var timeout;
    return function() {
        var args = arguments;
        clearTimeout(timeout);
        stat.text("calculating...");
        return timeout = setTimeout(function() {
            update.apply(null, arguments);
        }, 10);
    };
})();

var hashish = d3.selectAll("a.hashish")
.datum(function() {
  return this.href;
});

function parseHash() {
var parts = location.hash.substr(1).split("/"),
    desiredFieldId = parts[0],
    desiredYear = parseInt(parts[1]);

field = fieldsById[desiredFieldId] || fields[0];
console.log(desiredYear);
console.log(years);
year = (years.indexOf(desiredYear) > -1) ? desiredYear : years[0];
console.log(year);

fieldSelect.property("selectedIndex", fields.indexOf(field));

if (field.id === "none") {

  yearSelect.attr("disabled", "disabled");
  reset();

} else {

  if (field.years) {
    if (field.years.indexOf(year) === -1) {
      year = field.years[0];
    }
    yearSelect.selectAll("option")
      .attr("disabled", function(y) {
        return (field.years.indexOf(y) === -1) ? "disabled" : null;
      });
  } else {
    yearSelect.selectAll("option")
      .attr("disabled", null);
  }

  yearSelect
    .property("selectedIndex", years.indexOf(year))
    .attr("disabled", null);

  deferredUpdate();
  location.replace("#" + [field.id, year].join("/"));

  hashish.attr("href", function(href) {
    return href + location.hash;
  });
}
}

