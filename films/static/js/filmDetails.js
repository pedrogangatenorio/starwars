$(document).ready(function(){
	updateSession()
});

function updateSession(){
	var session = sessionStorage.getItem('pages') != null ? JSON.parse(sessionStorage.getItem('pages')) : [];
    let element = {'id':session.length +1, 'page': 'List Details from ' + $("#filmId").val(), 'url': '', 'param':$("#filmId").val()}
    session.push(element)
    sessionStorage.setItem("pages", JSON.stringify(session));  
    updateDiv(element)
}

function updateDiv(element){
    let last = document.getElementById("lastvisits")
    let current = JSON.parse(sessionStorage.getItem('pages'))
    let l = current.length
    for(let i=1; i< (l > 5 ? 6 : l); i++){
        var a2 = document.createElement("a");
        a2.setAttribute('class','dropdown-item');
        a2.setAttribute('href', current[l - i]['url'] + (current[l - i]['param'] ? current[l - i]['param'] : ''));
        a2.appendChild(document.createTextNode( current[l - i]['page']))
        document.getElementById("lastvisits").appendChild(a2);
    }    
}