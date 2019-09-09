'use strict'

// Don't write all controllers in one file like the follwing code.
// Write as components. recommended.
var aioApp = angular.module("mainApp");

aioApp.controller('LoginController', function($scope, $http, $location, LoggedUser){
    $scope.user = {};
    $scope.error_message = undefined;
    $scope.success = undefined;
    $scope.submit = function(){
    var req = {
            method: 'POST',
            url: '/login',
            headers: {
              'Content-Type': 'application/json'
            },
            data: $scope.user
           }
        
        $http(req)
        .then(
            function(response){
                if(response.status == 200){
                    $scope.success = 'Login Succesful'
                    LoggedUser.setLoggedUser($scope.user.username);
                    $location.url('/')
                }
            },

            function(errres){
                if(errres.status == 401){
                    $scope.error_message = "Invalid username and password";
                }
                else if (errres.status == 500){
                    $scope.error_message = 'Server error! Try later.';
                }
            }
        )
        
    }
});


aioApp.controller('SignupController', function($scope, $http, $location){
    $scope.user = {};
    $scope.error_message = undefined;
    $scope.success = undefined;
    $scope.submit = function(){
    var req = {
            method: 'POST',
            url: '/signup',
            headers: {
              'Content-Type': 'text/json'
            },
            data: $scope.user
           };
        
        $http(req)
        .then(
            function(response){
                if(response.status == 201){
                    $scope.success = 'Login Succesful'
                    $location.url('/login')
                }
            },
            function(errres){
                if(errres.status == 401){
                    $scope.error_message = "Invalid username and password";
                }
                else if (errres.status == 500){
                    $scope.error_message = 'Server error! Try later.';
                }else{
                    console.log("This si err", errres)
                }
            }
        )
        .catch(function(err){
            console.log(err, "eo")
        });
    }
});


aioApp.controller('HomeController', function($scope, LoggedUser){
    $scope.$watch('loggedUser', function(){
        $scope.loggedUser = LoggedUser.getLoggedUser();
    })
});