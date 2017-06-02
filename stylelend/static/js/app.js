var lyticsApp = angular.module('lyticsApp', [
  'ngRoute',
  'lyticsControllers'
]);

lyticsApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/expenditures', {
        templateUrl: 'static/angular_templates/create.html',
        controller: 'CreateExpenditure'
      }).
      when('/cats/', {
        templateUrl: 'static/angular_templates/categories.html',
        controller: 'ShowCategories'
      }).
      otherwise({
        redirectTo: '/expenditures'
      });
  }]);
