'use strict'

var AioApp = angular.module("mainApp");

AioApp.factory('LoggedUser', function(){
    var loggedUser = 'to AioApp';
    return {
        getLoggedUser: function(){
            return loggedUser;
        },
        setLoggedUser: function(user){
            loggedUser = user;
        }
    };
});