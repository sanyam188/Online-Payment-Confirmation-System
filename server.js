var express = require('express')
const hbs = require('hbs');
var app = express();
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
mongoose.connect('mongodb://Sanyam:abcd123@cluster0-shard-00-00-tctra.mongodb.net:27017,cluster0-shard-00-01-tctra.mongodb.net:27017,cluster0-shard-00-02-tctra.mongodb.net:27017/reg?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true');

// const {mongoose} = require('/db/mongoose.js');
//
var reg=mongoose.model('reg', {
  hostel:{
    type:String
  },
  lib:{
    type:Number
  },
  acad:{
    type:String
  },
  acadv:{
    type:Boolean
  },
  hostelv:{
    type:Boolean
  }
})
//app.use(bodyParser.json());
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));
app.set('view engine','hbs')
var myLogger = function (req, res, next) {
  console.log('LOGGED');
  next();
}

app.use(myLogger);

app.get('/', function (req, res) {
  res.render('form.hbs');
});

app.post('/t',(req,res)=>{
  console.log('success, post req created');
  var regn = new reg({
    hostel: req.body.Hostel,
    acad:req.body.Acadmic,acadv:false,hostelv:false
  });
  regn.save().then((doc) => {
    res.send(doc);
  }, (e) => {
    res.status(400).send(e);
  });
  console.log(req.body);
  console.log(req.body.Hostel);
  console.log(req.body.Acadmic);
});

app.listen(3000);
