const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

app.get("/client", (req, res) => {
  res.sendFile(__dirname + "/main.py");
});

io.on("connection", (socket) => {
  socket.on("joinRoom", (room) => {
    socket.join(room);
    console.log("joined room: " + room);
    socket.emit("joinedRoom", room);
    socket.room = room;
  });

  socket.on("keydown", (key) => {
    console.log("keydown: " + key);
    io.in(socket.room).emit("keydown", key);
  });

  socket.on("keyup", (key) => {
    console.log("keyup: " + key);
    io.in(socket.room).emit("keyup", key);
  });

  socket.to("some room").emit("some event");
});

server.listen(3000, () => {
  console.log("listening on *:3000");
  console.log("http://localhost:3000");
});
