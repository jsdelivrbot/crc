function popup(mylink, windowname) { 
    if (! window.focus)return true;
    var href;
    if (typeof(mylink) == 'string') href=mylink;
    else href=mylink.href; 
    page = window.open(href, windowname, 'width=600,height=400,scrollbars=yes'); 
    //page.document.write("<input type='button' value='accept' onclick='gotoreserve()'>");
    return false; 
}

function sendMail(){
    alert(ROOT);
    alert($("#email").val());
    alert($("#subject").val());
    var link = "mailto:"+$("#email").val()
             + "?cc=''"
             + "&subject=" + escape($("#subject").val())
             + "&body=" + escape($("#textarea").val())
    ;
    

    window.location.href = link;
    location.href = ROOT;
    
}
