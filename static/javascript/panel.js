/**
 * Created by Trase on 2/27/2016.
 */










$(document).ready(function() {


    new Vue({
        el: '#elements',
        data: {
            pageItems: [
                {title: 'title', content: 'content'},
                {title: 'testes', content: 'testers'}
            ]

        },
        methods: {
            dropdown: function (event) {
                this.next().focus();
            }
        }


    });


});