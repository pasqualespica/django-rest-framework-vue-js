
// instanze ROOT
var app = new Vue({ // option Object 

    // el sta per 'element' che si aspetta il selettore CSS
    el: "#myapp",
    data: {
        users : [ 
            {
                id: 1,
                name: "bob",
                professione: "gamer"
            },
            {
                id: 2,
                name: "alice",
                professione: "manager"
            }, 
            {
                id: 3,
                name: "marci",
                professione: "dajee"
            },
            {
                id: 4,
                name: "lcuai",
                professione: "LAVORO"
            },
            {
                id: 5,
                name: "forz",
                professione: "SPORT"
            },
        ]
    },
    methods: {

    },
})
