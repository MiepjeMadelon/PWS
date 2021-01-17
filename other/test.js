const express = require('express');
const app = express();
var html = require('http').createServer(app);
var io = require('socket.io')(html);
html.listen(3003);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/clienttest.html');
});

io.on('connection', function (socket) {
  socket.on('message',function(message){
    console.log(message);
  });
  socket.emit('message','Hello, my name is Server');
  if (false) socket.emit('send class', 'werewolf')
  socket.emit('become night', {})
});
