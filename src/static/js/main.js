document.getElementById("toggle").onclick = function(){toggle()};
let xz = 1

function toggle(){
    let toggle = document.getElementById('toggle')
    let navigation = document.querySelector('.navigation')
    navigation.classList.toggle('active')
    if(xz === 1){
        toggle.innerHTML = `<i class="fa fa-times"></i>`
        xz = 0
    }else{
        toggle.innerHTML = `<i class="fas fa-bars"></i>`
        xz = 1
    }
}

// element = document.getElementById('btn')

// element.onmouseover = function(){
//     element.innerHTML = `<button id="btn" type="button" class="btn btn-danger">Register</button>`
// }