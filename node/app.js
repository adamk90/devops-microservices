var express = require("express");
var app = express();

app.listen(3000, () => {
 console.log("Server running on port 3000");
});

app.get("/techlist", (req, res, next) => {
 res.json(["docker","aws","consul","packer","vagrant"]);
});


app.get("/10pi", (req, res, next) => {
 const request = require('request');
 request('http://pi:8888/pi/10', function (error, response, body) {
        console.log(body);
        res.send(body.toString());
 });
});
