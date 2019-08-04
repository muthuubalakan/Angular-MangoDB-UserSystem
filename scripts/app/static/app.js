var mainApp = angular.module("mainApp", ['ngRoute']);

mainApp.config(function($routeProvider) {
	$routeProvider
	.when('/', {
		templateUrl: 'static/templates/home.html'
	})
	.when('/login', {
		templateUrl: 'static/templates/login.html'
	})
	.when('/signup', {
		templateUrl: 'static/templates/signup.html'

	})
	.otherwise({
		redirectTo: '/'
	});
});
