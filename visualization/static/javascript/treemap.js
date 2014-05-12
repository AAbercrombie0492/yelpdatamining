// Generated by CoffeeScript 1.7.1
(function() {
  var dataColumns, dataTable;

  dataTable = null;

  dataColumns = {};

  google.load("visualization", "1", {
    packages: ["treemap"]
  });

  google.setOnLoadCallback(function() {
    var treemap, treemap_view;
    dataTable = google.visualization.arrayToDataTable(data);
    data[0].forEach(function(value, index) {
      return dataColumns[value] = index;
    });
    treemap_view = new google.visualization.DataView(dataTable);
    treemap_view.setColumns([dataColumns.category_title, dataColumns.parent_category, dataColumns.business_count, dataColumns.avg_review_count]);
    treemap = new google.visualization.TreeMap(document.getElementById('treemap-chart'));
    treemap.draw(treemap_view, {
      fontColor: '#000000',
      fontSize: 16,
      maxColorValue: 100,
      minColorValue: 0,
      showScale: true
    });
    return google.visualization.events.addListener(treemap, 'select', function() {
      var row, selection;
      selection = treemap.getSelection();
      row = selection[0].row;
      return console.log({
        id: dataTable.getValue(row, dataColumns.category_id),
        title: dataTable.getValue(row, dataColumns.category_title)
      });
    });
  });

}).call(this);
