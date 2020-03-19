
// instanze ROOT
var app = new Vue({ // option Object 

    // el sta per 'element' che si aspetta il selettore CSS
    el: "#myapp",
    data: {
        myflag : true,
        styleObject : {
            backgroundColor: 'green', 
            border: '5px solid orange'
        }
    },
    methods: {
        cambiaForma() {
            this.myflag = !this.myflag
        }
    },
})