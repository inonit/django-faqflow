var faqflow = angular.module('faqflow', ['ngResource']);

faqflow.conf = {
    baseUrl: '/api/faqflow/',
};

faqflow.config(['$httpProvider', function(httpProvider) {
    httpProvider.defaults.xsrfCookieName = 'csrftoken';
    httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

faqflow.service('backend', ['$resource', function(resource) {
    return resource(faqflow.conf.baseUrl + ':res/:pid/:sub/:cid', {res: 'questions'}, {

        user: { method: 'GET', params: {res: 'user'} },
        query: { method: 'GET', isArray: true },
        get: { method: 'GET', },
        post: { method: 'POST', },

    });
}]);

faqflow.run(['$rootScope', 'backend', function(scope, backend) {

    scope.tab = 1;
    scope.user = backend.user();
    scope.questions = backend.query();

}]);

faqflow.controller('faqflowController', ['$scope', 'backend', function(scope, backend) {

    scope.ask = {
        author_id: scope.user.id,
    };
    scope.reply = {};
    scope.question = {};
    scope.answers = {};

    scope.showQuestion = function(index) {
        scope.question = scope.questions[index];
        scope.answers = backend.query({
            res: 'questions',
            pid: scope.question.id,
            sub: 'answers',
        });
        scope.reply = {
            parent_id: scope.question.id,
            author_id: scope.user.id,
        };
        scope.tab = 2;
    };

    scope.postQuestion = function() {
        scope.questions.push(scope.ask);
        backend.post(scope.ask);
        scope.ask = {
            author_id: scope.user.id,
        };
    };

    scope.postAnswer = function() {
        scope.answers.push(scope.reply);
        backend.post({
            res: 'questions',
            pid: scope.question.id,
            sub: 'answers',
            data: scope.reply,
        });
        scope.reply = {
            parent_id: scope.question.id,
            author_id: scope.user.id,
        };
    };

}]);

faqflow.directive('search', function() {
    return {
        restrict: 'C',
        link: function(scope, element, attrs) {
            element.on('focus', function(e) {
                scope.tab = 1;
            });
        }
    };
});
