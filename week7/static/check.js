function getData(){
    let searchInput = document.getElementById("search").value;
    let result = document.getElementById("result");
    let url="http://127.0.0.1:3000/api/member?username="+searchInput;
    fetch(url).then(function(response){
        return response.json();
    }).then(function(data){
        if (data.data !== null){
            result.innerHTML = data.data["name"]+" ("+data.data["username"]+")";
        }
    })
};

function updateData(){
    let newName = document.getElementById("update").value;
    let result = document.getElementById("result2");
    let requestOptions = {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: newName })
    };
    let url="http://127.0.0.1:3000/api/member";
    fetch(url, requestOptions).then(function(response){
        return response.json()
    }).then(function(data){
        result.innerHTML = "更新成功"
    });
};