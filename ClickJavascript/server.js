const http = require("http");
const url = require("url");
const cors = require("cors");

// Utiliser cors() pour toutes les routes
const corsOptions = {
  origin: "*", // Cela permet à toutes les origines d'accéder à votre serveur (à ajuster selon vos besoins)
  methods: "GET,HEAD,PUT,PATCH,POST,DELETE",
  credentials: true,
  optionsSuccessStatus: 204,
};

const server = http.createServer((req, res) => {
  // Activer CORS pour toutes les routes
  cors(corsOptions)(req, res, () => {
    // Parse the request URL
    const parsedUrl = url.parse(req.url, true);
    console.log(parsedUrl.path);
    if (parsedUrl.path === "/addUser") {
      console.log("addUser");
      res.statusCode = 200;
      res.setHeader("Content-Type", "text/plain");
      res.end("addUser");
    }
  });
});

const port = 3000;
const ip = "127.0.0.1";
server.listen(port, ip, () => {
  console.log(`Server running at http://${ip}:${port}/`);
});
