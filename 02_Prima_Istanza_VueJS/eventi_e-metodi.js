
// instanze ROOT
var app = new Vue({ // option Object 

    // el sta per 'element' che si aspetta il selettore CSS
    el: "#myapp",
    data: {
        lezione: "Eventi e metodi in Vue",
        counter: 0
    },
    methods: {
        incrementaContatore() {
            this.counter += 1;
            console.log ("Ecco il contatore", this.counter)
            if (this.counter === 10 ) {
                alert("Counter a " + this.counter)
            }
        },
        
        overTheBox() {
            console.log("Mouse sopra il box verde !!!")
        }
    },
})