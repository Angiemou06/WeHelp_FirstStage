function check() {
    let confirm = document.querySelector("#confirm");
    if (confirm.checked == false) {
        alert("Please check the checkbox first.");
        return false
    }
}


function checkNumber() {
    
    let number = document.getElementById("number").value;
    if (isNaN(number) || number <= 0) {
        alert("Please enter a valid positive number.");
        return false;
    }
    else{
        console.log(number);
        number = number.toString();
        window.location.href = `/square/${number}`;
        return false;
    }
}