const mongoose = require("mongoose");
const express = require("express");
const cors = require("cors");
const app = express();

const { spawn } = require("child_process");
//middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cors());

//mongo db connection
const url = `mongodb+srv://yas:yas@cluster0.wdszhtf.mongodb.net/?retryWrites=true&w=majority`;

const connectionParams = {
  useNewUrlParser: true,

  useUnifiedTopology: true,
};
mongoose
  .connect(url, connectionParams)
  .then(() => {
    console.log("Connected to database ");
  })
  .catch((err) => {
    console.error(`Error connecting to the database. \n${err}`);
  });

//server running
const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log("server started at PORT ", PORT);
});

//post request to mongoose

app.post("/", async (req, res) => {
  const { data } = req.body;
  //console.log(data);
  const process = await spawn("python3", ["./sample2.py", data]);
  process.stdout.on("data", function (data) {
    let result = data.toString();
    result = JSON.stringify(result);
    // console.log(result);
    res.send(result);
  });
});
