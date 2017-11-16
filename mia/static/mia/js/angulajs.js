var app = angular.module("MIA", []);

app.controller("search", function($scope, $http) {

    $scope.myquery = "";

    $scope.search = function(){

        $scope.searchResult = null;

        if($scope.myquery.length > 2 ){
        $http.get("http://127.0.0.1:8000/getallpatients/" + $scope.myquery)
            .then(function (response) {
                $scope.searchResult = response.data;
            });
        }
    };
});