google.charts.load('current', {packages: ['corechart']});

function drawChart(json) {
  // var json = {'a': 3, 'b':2, 'c': 3, 'd': 18};
  console.log(json);
  // Define the chart to be drawn.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Char');
  data.addColumn('number', 'Frequency');
  
  for (var key in json) {
    if (json.hasOwnProperty(key)) {
      data.addRow([key, json[key]]);
    }
  }

  var options = {
    width: 1000,
    height: 200,
    bar: {groupWidth: "95%"},
    legend: { position: "none" },
  };
  // Instantiate and draw the chart.
  var chart = new google.visualization.ColumnChart(document.getElementById('chart'));
  chart.draw(data, options);
}