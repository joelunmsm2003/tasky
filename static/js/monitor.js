function Todo($scope,$http,$cookies,$filter) {


	

	$scope.Equipo = function() 

    {        
        var todo={

            add: "equipo",
            dato: "2",
            done:false
        }

       $http({
        url: "/version/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {
        console.log(data);

        
        })

    
    };

    $scope.Login = function() 

    {        
        console.log('registro', $scope.registro)

        $http({ 
        url: "/login/",
        data: $scope.registro,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        $scope.nequipos= data

        })

    
    };


    $http({ 
        url: "/nequipos/",
        data: 'todo',
        method: 'GET',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {
        $scope.nequipos= data
        })


    $scope.equipos = function() 

    {        
        var todo={

            add: "equipo",
            dato: "2",
            done:false
        }

       $http({
        url: "/equipos/",
        data: todo,
        method: 'GET',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {
        $scope.datEquip= data
        console.log(data);
        
        })

    
    };



}
