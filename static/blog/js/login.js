function to_sign_up(){
    $("form input[name=password1]").show(300);
    var span = '<span>Have an account? <a href="javascript:void(0);" onclick="to_sign_in();">Sign in</a></span>';
    $("form span:eq(0)").text("Sign up your accuont");
    $("form span:eq(1)").remove();
    $("form").append(span);
    $(".status").hide(300);
    $("form button").text("Register");
}

function to_sign_in(){
    $("form input[name=password1]").hide(300);
    var span = '<span>Don\'t have an account? <a href="javascript:void(0);" onclick="to_sign_up();">Sign up</a></span>';
    $("form span:eq(1)").remove();
    $("form span:eq(0)").text("Sign in your accuont");
    $("form").append(span);
    $(".status").show(300);
    $("form button").text("Login");
}


function login(){
    var text = $("form button").text();
    var url = '';
    if(text == "Login"){
        url = 'login';
    }else{
        url = 'sign';
    }
    $.ajax({
        url: url,
        type: 'POST',
        data: $('form').serialize(),
        success: function(result){
            
            if(result == 0){
                window.location = 'blog';
            }else{
                $("form").css({"height":"330px"},500);
                $("form p").fadeIn(500).text(result).delay(5000).fadeOut('normal','linear',function(){$("form").css({"height":"310px"},500);});
            }
        }
    });
}
