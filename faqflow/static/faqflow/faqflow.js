var faqflow = angular.module('faqflow', ['ngResource']);

faqflow.conf = {
    baseUrl: '/api/faqflow/',
};

faqflow.service('backend', ['$resource', function(resource) {
    return resource(faqflow.conf.baseUrl + ':type/:qid', {type: 'question'}, {
        auth: { method: 'GET', params: {type: 'auth'} },
        queryQ: { method: 'GET', isArray: true },
        getQ: { method: 'GET', },
        postQ: { method: 'POST', },
        postA: { method: 'POST', params: {type: 'answer'} },
    });
}]);

faqflow.run(['$rootScope', 'backend', function(scope, backend) {
    scope.questions = backend.queryQ();
}]);

faqflow.controller('faqflowController', ['$scope', function(scope) {

}]);
