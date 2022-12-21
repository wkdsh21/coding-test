// 1. 서버 사용을 위해서 http 모듈을 http 변수에 담는다. (모듈과 변수의 이름은 달라도 된다.)
const express = require("express");
const app = express();
app.use(express.static("front"));
var qr = require("querystring");
// 1. mongoose 모듈 가져오기
var mongoose = require("mongoose");
// 2. testDB 세팅
mongoose.connect(
  "mongodb+srv://sh1801202:0201@cluster0.gfai7ek.mongodb.net/test"
);
// 3. 연결된 testDB 사용
var db = mongoose.connection;
// 4. 연결 실패
db.on("error", function () {
  console.log("Connection Failed!");
});
// 5. 연결 성공
db.once("open", function () {
  console.log("Connected!");
});
function templateHTML(java, c, python) {
  return `
  <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SH's Portfolio</title>
    <meta name="description" content="Portfolio" />
    <meta name="author" content="SH" />
    <link rel="icon" type="image/png" href="imgs/favicon.png" />
    <script
      src="https://kit.fontawesome.com/9eb162ac0d.js"
      crossorigin="anonymous"
    ></script>
    <link
      href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="style.css" />
    <script src="test2.js" defer></script>
  </head>
  <body>
    <!-- title -->
    <nav id="nav">
      <a href="#">SH's portpolio</a>
      <ul>
        <li>
          <input type="button" name="nav" id="nav1" value="About Me" />
        </li>
        <li><input type="button" name="nav" id="nav2" value="skills" /></li>
        <li><input type="button" name="nav" id="nav3" value="project" /></li>
      </ul>
    </nav>
    <!-- Home -->
    <section id="home">
      <div class="home__container">
        <img src="imgs/profile.jpeg" alt="profile" class="home__photo" />
        <h1 class="home__title">
          안녕하세요 <br />군산대 재학중인 장승한 입니다.
        </h1>
      </div>
    </section>

     <!-- About -->
     <section id="about" class="section section__container">
        <h1>About me</h1>
        <p>
          군산대를 재학중인 장승한 입니다. 현재 목표를 향해 여러 분야들을 공부중입니다.
        </p>
        <div class="about__university">
          <div class="major">
            <img src="imgs/kunsan.jpg" alt="university" class="major__icon">
            <h2 class="major__title">Kunsan university</h2>
          </div>
          <div class="major">
            <h1 class="major__icon">CIE</h1>
            <h2 class="major__title">Computer Information <br>Engineering</h2>
          </div>
        </div>
            <div class="job__description">
              <p class="job__name">
                Kunsan university Computer Information Engineering Attending
              </p>
              <p class="job__period">2022 JUNE - Until now</p>
             </div>
        </div>
      </section>

      <!-- Skills -->
    <section id="skills" class="section">
        <div class="section__container">
          <h1>programming language</h1>
          <p>
            지금까지 배운 프로그래밍 언어들의 성취도
          </p>
          <div class="skillset">
              <h3 class="skillset__title">programming language</h3>
              <div class="skill">
                <div class="skill__description">
                  <span>C</span>
                  <span>70%</span>
                </div>
                <div class="skill__bar">
                  <div class="skill__value" style="width: 70%;"></div>
                </div>
              </div>
              <div class="skill">
                <div class="skill__description">
                  <span>C++</span>
                  <span>90%</span>
                </div>
                <div class="skill__bar">
                  <div class="skill__value" style="width: 90%;"></div>
                </div>
              </div>
              <div class="skill">
                <div class="skill__description">
                  <span>JavaScript</span>
                  <span>90%</span>
                </div>
                <div class="skill__bar">
                  <div class="skill__value" style="width: 90%;"></div>
                </div>
              </div>
              <div class="skill">
                <div class="skill__description">
                  <span>Java</span>
                  <span>80%</span>
                </div>
                <div class="skill__bar">
                  <div class="skill__value" style="width: 80%;"></div>
                </div>
              </div>
              <div class="skill">
                <div class="skill__description">
                  <span>Python</span>
                  <span>88%</span>
                </div>
                <div class="skill__bar">
                  <div class="skill__value" style="width: 88%;"></div>
                </div>
              </div>
            </div>
        </div>
      </section>
       <!-- project -->
    <section id="project">
        <h1 class="project__title">
            지금까지 해온 Project입니다.
        </h1>
        <div class="project__container">
            <div class="java__project">
                <h2 class="java__title">
                    java
                </h2>
                <h3 class="java__description">
                  ${java}
                  <form method="post"><input type="text" name="java" /></form>
                </h3>
            </div>
            <div class="cplus__project">
                <h2 class="title">
                    c++
                </h2>
                <h3 class="cplus__description">
                  ${c}
        <form method="post"><input type="text" name="c" /></form>
                </h3>
            </div>
            <div class="python__project">
                <h2 class="title">
                    python
                </h2>
                <h3 class="python__description">
                  ${python}
                  <form method="post"><input type="text" name="python" /></form>
                </h3>
            </div>
        </div>
      </section>
      <button id="up"><img src="imgs/up.png" alt="up" /></button>
  </body>
</html>
  `;
}
var javast = "";
var cst = "";
var pythonst = "";
function javafind() {
  java.find(function (error, javas) {
    var data = "";
    console.log("--- Read all ---");
    if (error) {
      console.log(error);
    } else {
      javas.forEach((element) => {
        data +=
          "<h3>" +
          element["data"] +
          "<h3>" +
          '<form action="/deletejava" method="post"><input type="hidden" name="_id" value="' +
          element["_id"] +
          '"/><input type="submit" value="삭제"/></form>';
      });
      javast = data;
    }
  });
  return javast;
}

function cfind() {
  c.find(function (error, javas) {
    var data = "";
    console.log("--- Read all ---");
    if (error) {
      console.log(error);
    } else {
      javas.forEach((element) => {
        data +=
          "<h3>" +
          element["data"] +
          "<h3>" +
          '<form action="/deletec" method="post"><input type="hidden" name="_id" value="' +
          element["_id"] +
          '"/><input type="submit" value="삭제"/></form>';
      });
      cst = data;
    }
  });
  return cst;
}

function pythonfind() {
  python.find(function (error, javas) {
    var data = "";
    console.log("--- Read all ---");
    if (error) {
      console.log(error);
    } else {
      javas.forEach((element) => {
        data +=
          "<h3>" +
          element["data"] +
          "<h3>" +
          '<form action="/deletepython" method="post"><input type="hidden" name="_id" value="' +
          element["_id"] +
          '"/><input type="submit" value="삭제"/></form>';
      });
      pythonst = data;
    }
  });
  return pythonst;
}

app.get("/", (req, res) => {
  res.end(templateHTML(javafind(), cfind(), pythonfind()));
});

app.post("/", function (request, response) {
  var postdata = "";
  request.on("data", function (data) {
    postdata += data;
  });

  request.on("end", function () {
    var parsedQuery = qr.parse(postdata);
    console.log(parsedQuery);
    insert(
      Object.keys(parsedQuery)[0],
      parsedQuery[Object.keys(parsedQuery)[0]]
    );
  });
});

app.post("/deletejava", function (request, response) {
  var postdata = "";
  request.on("data", function (data) {
    postdata += data;
  });

  request.on("end", function () {
    var parsedQuery = qr.parse(postdata);
    java.remove(parsedQuery, function (error, output) {
      console.log("--- Delete ---");
      if (error) {
        console.log(error);
      }
    });
  });
});

app.post("/deletec", function (request, response) {
  var postdata = "";
  request.on("data", function (data) {
    postdata += data;
  });

  request.on("end", function () {
    var parsedQuery = qr.parse(postdata);
    c.remove(parsedQuery, function (error, output) {
      console.log("--- Delete ---");
      if (error) {
        console.log(error);
      }
    });
  });
});

app.post("/deletepython", function (request, response) {
  var postdata = "";
  request.on("data", function (data) {
    postdata += data;
  });

  request.on("end", function () {
    var parsedQuery = qr.parse(postdata);
    python.remove(parsedQuery, function (error, output) {
      console.log("--- Delete ---");
      if (error) {
        console.log(error);
      }
    });
  });
});

app.listen(8080, () => {
  console.log("listening on *:3000");
});

// 6. Schema 생성. (혹시 스키마에 대한 개념이 없다면, 입력될 데이터의 타입이 정의된 DB 설계도 라고 생각하면 됩니다.)
var project = mongoose.Schema({
  data: "string",
});

// 7. 정의된 스키마를 객체처럼 사용할 수 있도록 model() 함수로 컴파일
var java = mongoose.model("java", project);
var c = mongoose.model("c", project);
var python = mongoose.model("python", project);
// 8. Student 객체를 new 로 생성해서 값을 입력
function insert(project, Data) {
  if (project == "java") {
    var Java = new java({
      data: Data,
    });
    Java.save(function (error, data) {
      if (error) {
        console.log(error);
      } else {
        console.log("Saved!");
      }
    });
  } else if (project == "c") {
    var C = new c({
      data: Data,
    });
    C.save(function (error, data) {
      if (error) {
        console.log(error);
      } else {
        console.log("Saved!");
      }
    });
  } else if (project == "python") {
    var Python = new python({
      data: Data,
    });
    Python.save(function (error, data) {
      if (error) {
        console.log(error);
      } else {
        console.log("Saved!");
      }
    });
  }
}
