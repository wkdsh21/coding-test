nav1.addEventListener("click", function () {
  scrollMove("about");
});
nav2.addEventListener("click", function () {
  scrollMove("skills");
});
nav3.addEventListener("click", function () {
  scrollMove("project");
});
up.addEventListener("click", function () {
  scrollMove("home");
});

function scrollMove(id) {
  let location = document.querySelector(`#${id}`).offsetTop;
  window.scrollTo({ top: location, behavior: "smooth" });
}
