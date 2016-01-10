var engines = require('consolidate');
var express = require('express');
var path=require('path');

var app = express();

app.engine('hjs',engines.hogan);

app.set('view engine', 'hjs');
app.set('views',path.join(__dirname,'views/'));

app.get('/', function(req,res){
    res.render('index',{a:'apple',b:'bird'});
});

app.listen(3000);
