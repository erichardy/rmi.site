
/*
http://stackoverflow.com/questions/9765098/plone-and-twitter-bootstrap
https://github.com/CWSpear/bootstrap-hover-dropdown
*/

$(document).ready(function() {
    $("body").addClass("rmi");
    $(".dropdown").hover(
            function(){ $(this).addClass('open') },
            function(){ $(this).removeClass('open') }
        );
});