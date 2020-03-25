
// instanze ROOT
var app = new Vue({ // option Object 

    // el sta per 'element' che si aspetta il selettore CSS
    el: "#myapp",
    data: {
        first_name: "mario",
        last_name: "rossi"
    },
    methods: {
        getRandomNumber() {
            return Math.random()
        }

    },
    // Simili ai methods che abbiamo già imparato ad utilizzare, 
    // si distinguono da questi per il fatto che i loro “risultati” 
    // vengono salvati in cache fino a che i valori da essi utilizzati non cambiano.

    // Chiamati talvolta anche computed values, possiamo pensare a 
    // questi come a un’estensione del nostro data model, utile a mostrare
    // valori risultanti da elaborazioni.

    // È bene evitare di modificare i valori del data model tramite le 
    //  computed properties, mantenendole leggere e “pure”
    computed: {
        getRandomComputed() {
            return Math.random()
        },
        getFullName() {
            return `${this.first_name} ${this.last_name}`
        },
        getReverseFullName() {
            first = this.last_name.split("").reverse().join("")
            last = this.first_name.split("").reverse().join("")
            return `${first} ${last}`
        }
    },
})