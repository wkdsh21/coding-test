nav1.addEventListener('click', function(){scrollMove("presentation")});
nav2.addEventListener('click', function(){scrollMove("algorithm")});
nav3.addEventListener('click', function(){scrollMove("project")});
function scrollMove(id){
    let location = document.querySelector(`#${id}`).offsetTop;
    window.scrollTo({ top: location, behavior: "smooth" });
}
