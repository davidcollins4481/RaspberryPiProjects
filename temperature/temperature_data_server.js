var sqlite3 = require('sqlite3').verbose();
var garageDB = new sqlite3.Database("/tmp/garage.db");
var http = require('http');

http.createServer(function(req, res) {
    res.writeHead(200, { 'content-type': 'text/json' });    

    garageDB.parallelize(function() {
        garageDB.all('select * from temperature;', function(err, rows) {
            console.log("query temperature");            
            res.end(JSON.stringify(rows));
        });
    });

}).listen(4481);

console.log("Listening on port 4481");

