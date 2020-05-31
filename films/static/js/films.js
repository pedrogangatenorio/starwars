$(document).ready(function(){
    var maxLength = 110;
    $(".show-read-more").each(function(){
        var myStr = $(this).text();
        if($.trim(myStr).length > maxLength){
            var newStr = myStr.substring(0, maxLength);
            var removedStr = myStr.substring(maxLength, $.trim(myStr).length);
            $(this).empty().html(newStr);
            $(this).append(' <a href="javascript:void(0);" class="read-more">read more...</a>');
            $(this).append('<span class="more-text">' + removedStr + '</span>');
        }
    });

    $(".read-more").click(function(){
        $(this).siblings(".more-text").contents().unwrap();
        $(this).remove();
    });

    updateSession();
    updateSessionSuggest();
});

function updateSession(){
    let session = sessionStorage.getItem('pages') != null ? JSON.parse(sessionStorage.getItem('pages')) : [];
    let detail = $("#filmId").val()==undefined ? false:true;
    let element = detail ? {'id':session.length +1, 'page': 'List Details from ' + $("#filmId").val(), 'url': '', 'param':$("#filmId").val()} : {'id':session.length +1, 'page': 'List films', 'url': '/'}
    session.push(element);
    sessionStorage.setItem("pages", JSON.stringify(session));    
    updateDiv(element);
}

function updateDiv(element){
    let last = document.getElementById("lastvisits");
    let current = JSON.parse(sessionStorage.getItem('pages'));
    let l = current.length;
    for(let i=1; i< (l > 5 ? 6 : l); i++){
        var a2 = document.createElement("a");
        a2.setAttribute('class','dropdown-item');
        a2.setAttribute('href', current[l - i]['url'] + (current[l - i]['param'] ? current[l - i]['param'] : ''));
        a2.appendChild(document.createTextNode( current[l - i]['page']));
        document.getElementById("lastvisits").appendChild(a2);
    }    
}

function updateSessionSuggest(){
    let session = sessionStorage.getItem('title') != null ? JSON.parse(sessionStorage.getItem('title')) : [];

    if (session === undefined || session.length == 0) {
        request_url = '/films/getSession'
        $.ajax({
            url: request_url,
            success: function(data){
                sessionStorage.setItem("title", JSON.stringify(data['title']));  
                sessionStorage.setItem("director", JSON.stringify(data['director']));           
                sessionStorage.setItem("producer", JSON.stringify(data['producer']));
            },
            error: function (request, status, error) {
                alert(error);
            }
        });  
    }
}