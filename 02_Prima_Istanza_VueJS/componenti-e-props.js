Vue.component("comment", {
  
    // Parleremo anche di Props, una speciale tipologia di attributi 
    // che utilizziamo per passare dati tra componenti genitore e figli; 
    // Quando un valore viene passato da un componente a un altro tramite 
    // Prop, questo diventa una proprietà dell’istanza del componente a
    //  cui è stato passato.
    props: {
        comment: {
            type: Object,
            required: true
        }
    },
    // utlizzarlo nei template ( ATTENZIONE SOLO UN ROOT ELEMENT )
    template: `
        <div class="comment">
            <div class="card-body">
                <p> {{ comment.username }} </p>
                <p> {{ comment.content }} </p>
                <hr>
            </div>
        </div>
    `
})

// instanze ROOT
var app = new Vue({ // option Object 

    // el sta per 'element' che si aspetta il selettore CSS
    el: "#myapp",
    data: {
        comments: [
            {username:"batman", content:"primo comment"},
            {username:"batman2", content:"primo comment2"},
            {username:"batman3", content:"primo comment3"},
            {username:"batman4", content:"primo comment4"},

        ]
        
    },
    methods: {

    },
})