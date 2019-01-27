var express = require('express')
const hbs = require('hbs');
var app = express();
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
mongoose.connect('mongodb://localhost:27017/reg');

// const {mongoose} = require('/db/mongoose.js');
//
var reg=mongoose.model('reg', {
  hostel:{
    type:String
  },
  lib:{
    type:Number
  },
  acd:{
    type:String
  },
  acdv:{
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
    hostel: req.body.Hostel
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
