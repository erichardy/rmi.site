
/*
http://stackoverflow.com/questions/9765098/plone-and-twitter-bootstrap
http://stackoverflow.com/questions/8878033/how-to-make-twitter-bootstrap-menu-dropdown-on-hover-rather-than-click
https://github.com/CWSpear/bootstrap-hover-dropdown
*/

$(document).ready(function() {
    $("body").addClass("rmi");
    $("ul#nav .dropdown").hover(
            function(){ $(this).addClass('open') },
            function(){ $(this).removeClass('open') }
        );
     $("li a.hasDropDown").hover(
            function(){ $(this).addClass('open') },
            function(){ $(this).removeClass('open') }
        );
    var url = window.location.href;
    // console.log(url);
    /*
    $("ul#nav li.dropdown a").each(function(){
        if (url == $(this).attr("href")) {
                headMenu.addClass("active");
            };
    });
    */
    $("ul#nav .dropdown").each(function(){
        var headMenu = $(this);
        $(this).find("a").each(function(){
            if (url == $(this).attr("href")) {
                $(this).parent().addClass("active");
                headMenu.addClass("nav-active");
            };
        });
    });
});