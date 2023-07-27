
document.getElementById("checkButton").addEventListener("click", check)

function check() {
    let confirm = document.querySelector("#confirm");
    if (confirm.checked == false) {
        alert("Please check the checkbox first.");
    }
}

document.getElementById("calButton").addEventListener("click", checkNumber)

function checkNumber() {
    
    let number = document.getElementById("number").value;
    number = parseInt(number);
    if (isNaN(number) || number <= 0) {
        alert("Please enter a valid positive number.");
        window.location.href = `/`;
    }
    else{
        number = number.toString();
        window.location.href = `/square/${number}`;

    }
}