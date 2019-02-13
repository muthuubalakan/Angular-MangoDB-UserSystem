var mainApp = angular.module("mainApp", ['ngRoute']);

mainApp.config(function($routeProvider) {
	$routeProvider
	.when('/', {
		templateUrl: 'static/templates/home.html'
	})
	.when('/login', {
		templateUrl: 'static/login.html'
	})
	.when('/signup', {
		templateUrl: 'static/signup.html'

	})
	.otherwise({
		redirectTo: '/'
	});
});
