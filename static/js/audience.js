

function Todo($scope,$http,$cookies,$filter) {

    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;


    
    $http.get("/audiences").success(function(response) {$scope.clientes = response;

        $scope.search();
  
        x=$scope.clientes[0]['costumer_id']

        //setInterval(function(){ alertFunc; }, 3000);

        

                 $('#container').highcharts({


                        
                        series: [{
                            type: 'pie',
                            name: 'Browser share',
                            data: [
                                ['Firefox',   45.0],
                                ['IE',       26.8],
                                {
                                    name: 'Chrome',
                                    y: 12.8,
                                    sliced: true,
                                    selected: true
                                },
                                ['Safari',    8.5],
                                ['Opera',     6.2],
                                ['Others',   x*8]
                            ]
                        }]
                    });
                
       

                        
           
       
    });

    $http.get("/costumers").success(function(response) {$scope.costumers = response;
 
    });


    $scope.numberOfPages = function() 
    {

    return Math.ceil($scope.clientes.length / $scope.pageSize);
    
    };

    

    $scope.addNew=function(currentPage){

         $('#Agregar').modal('hide')
         $('.modal-backdrop').remove();


        console.log($scope.agregar)
        
        var todo={

            add: "New",
            dato: $scope.agregar,
            done:false
        }

        $scope.pagedItems[currentPage].push($scope.agregar);
        $scope.clientes.push($scope.agregar);

        console.log("push"),

        $http({
        url: "/audiences/",
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

    $scope.saveContact = function (idx,currentPage) {


        $scope.pagedItems[currentPage][idx] = angular.copy($scope.model);
       

        var todo={

            add: "Edit",
            dato: $scope.model,
            done:false
        }


        $http({
        url: "/audiences/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        console.log(data);

        })


        $('#Edit').modal('hide')
        $('.modal-backdrop').remove();
    };


    $scope.eliminarContact = function (idx,currentPage) {


        $('#Eliminar').modal('hide')
        $('.modal-backdrop').remove();

        console.log($scope.pagedItems[currentPage])

        $scope.pagedItems[currentPage].splice(idx,1);

        var todo={

            dato: $scope.model,

            add: "Eliminar",

            done:false
        }


        $http({
        url: "/audiences/",
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

    $scope.editContact = function (contact,index,currentPage) {

        $scope.index = index;
        $scope.numberPage =currentPage;
        $scope.model = angular.copy(contact);   
        console.log($scope.model);

    };


    $scope.sort_by = function(newSortingOrder) {

        if ($scope.sortingOrder == newSortingOrder)
            $scope.reverse = !$scope.reverse;

        $scope.sortingOrder = newSortingOrder;

        // icon setup
        $('th i').each(function(){
            // icon reset
            $(this).removeClass().addClass('icon-sort');
        });
        if ($scope.reverse)
            $('th.'+newSortingOrder+' i').removeClass().addClass('icon-chevron-up');
        else
            $('th.'+newSortingOrder+' i').removeClass().addClass('icon-chevron-down');
    
    };


     $scope.search = function () {

        console.log($scope.tipo)



        console.log($filter('filter')($scope.clientes,$scope.tipo))

        $scope.filteredItems = $filter('filter')($scope.clientes,$scope.tipo);
        $scope.currentPage = 0;
        // now group by pages

        console.log($scope.filteredItems)

        $scope.groupToPages();
    };


    $scope.groupToPages = function () {

        console.log('Grupo')
        $scope.pagedItems = [];
        
        for (var i = 0; i < $scope.filteredItems.length; i++) {
            if (i % $scope.itemsPerPage === 0) {
                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)] = [ $scope.filteredItems[i] ];
            } else {
                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)].push($scope.filteredItems[i]);
            }
        }
    };


    $scope.prevPage = function () {
        if ($scope.currentPage > 0) {
            $scope.currentPage--;
        }
    };
    
    $scope.nextPage = function () {
        if ($scope.currentPage < $scope.pagedItems.length - 1) {
            $scope.currentPage++;
        }
    };
    
    $scope.setPage = function () {
        $scope.currentPage = this.n;
    };

    
    Todo.$inject = ['$scope', '$filter'];

}

