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

let hosts = [];

io.on("connection", (socket) => {
  console.log("a user connected");
  socket.on("chat message", (msg) => {
    console.log("message: " + msg);
  });

  socket.on("keyinput", (key) => {
    console.log("keyinput: " + key);
    io.emit("keyinput", key);
  });

  socket.on("keydown", (key) => {
    console.log("keydown: " + key);
    io.emit("keydown", key);
  });

  socket.on("keyup", (key) => {
    console.log("keyup: " + key);
    io.emit("keyup", key);
  });
  socket.on("mouse", (mouse) => {
    console.log("mouse: " + mouse);
    io.emit("mouse", mouse);
  });

  socket.on("host", (host) => {
    console.log("host: " + host.foo);
    // io.emit("host", host);
    hosts.push(socket);
    console.log(hosts);
  });
});

server.listen(3000, () => {
  console.log("listening on *:3000");
  console.log("http://localhost:3000");
});
