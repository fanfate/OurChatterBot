$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});


// 为防止CSRF（Cross-site request forgery）跨站请求伪造，发post请求时需要在cookie中创建随机码
function getCookie(name)
{
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
    /*
        上面这句话相当于：
    var arr;
    var reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
        */
    if(arr=document.cookie.match(reg))
        return decodeURI(arr[2]);    //ECMAScript v3 已从标准中删除了 unescape() 函数，并反对使用它，
                                    // 因此应该用 decodeURI() 和 decodeURIComponent() 取而代之。
    else
        return null;
}