function check() {
    let nameInput = document.getElementById("name");
    let accountInput = document.getElementById("account");
    let passwordInput = document.getElementById("password");
    if (nameInput.value === "" || accountInput.value === "" || passwordInput.value === "") {
        alert("請輸入完整註冊資訊！");
        return false
    }
    return true
}

function check2() {
    let accountInput = document.getElementById("account_signin");
    let passwordInput = document.getElementById("password_signin");
    if ( accountInput.value === "" || passwordInput.value === "") {
        alert("請輸入完整登入資訊！");
        return false
    }
    return true
}

function confirmDelete(){
    confirm("確認是否刪除留言");
}