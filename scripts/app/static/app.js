var aioApp = angular.module("mainApp", [ 'ngRoute' ]);


aioApp.config(function($routeProvider) {
	$routeProvider
	.when('/', {
		templateUrl: 'static/templates/home.html',
		controller: 'HomeController',
	})
	.when('/login', {
		templateUrl: 'static/templates/login.html',
		controller: 'LoginController',
	})
	.when('/signup', {
		templateUrl: 'static/templates/signup.html',
		controller: 'SignupController',

	})
	.otherwise({
		redirectTo: '/'
	});
});
