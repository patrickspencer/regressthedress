var lyticsControllers = angular.module('lyticsControllers', []);

lyticsControllers.controller('CreateExpenditure', function($scope, $http) {

    $scope.fetchExpenditures = function () {
      $http.get("/api/expenditures/")
        .success(function (response) {
            $scope.expenditures = response.json_list;
      });
    };

    $scope.createExpenditure = function () {
        var data = {date: $scope.date, time: $scope.time,
          description: $scope.description, cost: $scope.cost, category_id: ""};
        $scope.data = data;

        $http.post("/api/expenditures/", data)
            .success(function (data, status, headers) {
                $scope.fetchExpenditures();
        });

    }; // end createExpenditure callback

    // callback for ng-click 'deleteUser':
    $scope.delete = function (expenditure_id) {
        $http.delete("/api/expenditure/" + expenditure_id + "/")
            .success(function (data, status, headers) {
                $scope.fetchExpenditures();
        });
    };

});

lyticsControllers.controller('ShowCategories', function($scope, $http) {

    $scope.foo = 'bar';

});

