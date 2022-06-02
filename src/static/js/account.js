// 
let accountManagement = document.getElementsByClassName('account-management');
let button = document.getElementById('btn');
button.onclick = function(){
    accountManagement.innerHTML = `Lol`;
}

/// Animatie la "forgot password"
forgot_password_background = document.getElementById('forgot_password_background');
forgot_password = document.getElementById('forgot_password_text');
forgot_password.onmouseover = function(){
    // console.log("onhover")
    forgot_password_background.classList.toggle('active');
}
forgot_password.onmouseout = function(){
    // console.log("nu mai e hover")
    forgot_password_background.classList.toggle('active');
}


/// Animatie dropdown la login
function dropdown(){
    console.log("tetsa")
    ClassList = document.getElementsByClassName("account-management");
    ClassList[0].classList.add("account-management-active")
}