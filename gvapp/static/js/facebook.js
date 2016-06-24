
var fb_appId = '1003684733014635';
var fb_appSecret = 'miuNQ7RzuHruulnUczx5pcvHa2I';
var fb_appAccessToken = fb_appId+'|'+fb_appSecret;
var fb_permissions = 'public_profile,email,user_birthday,user_location';

function fb_init() {
	FB.init({
        appId      : fb_appId,
        cookie     : true,  // enable cookies to allow the server to access the session
        xfbml      : true,  // parse social plugins on this page
        version    : 'v2.6' // use graph api version 2.5
    });
}

function fb_loadSDK() {
	(function(d, s, id) {
	    var js, fjs = d.getElementsByTagName(s)[0];
	    if (d.getElementById(id)) return;
	    js = d.createElement(s); js.id = id;
	    js.src = "//connect.facebook.net/en_US/sdk.js";
	    fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));
}

function fb_sendNotification(userId, message, url) {
    FB.api("/"+userId+"/notifications", 'post', {access_token : appAccessToken, template : message, href : url}, function(data) {
        console.log(data);
    });
}

function fb_checkLoginState(statusChangeCallback) {
    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
}

function fb_login(statusChangeCallback) {
    FB.login(function(response) {
        if(response.authResponse) {
            fb_checkLoginState(statusChangeCallback);
        }

    }, {scope: fb_permissions});
}