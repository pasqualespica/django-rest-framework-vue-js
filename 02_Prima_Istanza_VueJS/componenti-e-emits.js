// comment list component
Vue.component("comment-list", {

    // mentre il nostro componente `single-comment` accetta una singolo oggetto
    // `comment` , qui accettera' una lista
    props: {
        comments: {
            type: Array,
            required: true
        }
    },

    // data nei componenti e' una FUNZIONE
    data: function() {
        return {
            new_comment: null,
            comment_author: null,
            error: null
        }
    },

    methods: {
        submitComment() {
            // emettere un evento tramite EMIT
            if (this.new_comment && this.comment_author) {
                this.$emit('submit-comment', {  username : this.comment_author,
                                                content : this.new_comment });
                this.comment_author = null;
                this.new_comment = null;

                if (this.error) {
                    this.error - null;
                }
            } else {
                this.error = "assicurati di compilare tutti i dati del form"
            }
        }
    },

    template:`
        <div class="comment mb-2">

            <div class="container">

                <single-comment
                    v-for="(comment, indice) in comments"
                    :comment="comment"
                    :key="indice"
                ></single-comment>
                <hr>
                <h3> {{ error}} </h3>

                <form @submit.prevent="submitComment">

                    <div class="form-group">
                        <label for="commentoautore">
                            Il tuo UserName : 
                        </label>

                        <input 
                            class="form-control" 
                            id="commentoautore"
                            type="text" 
                            v-model="comment_author">
                    </div>        

                    <div class="form-group">
                        <label for="commentotesto">
                            Inserisci un commento : 
                        </label>

                        <textarea
                            class="form-control"
                            id="commentotesto"
                            rows="3"
                            cols="40"
                            v-model="new_comment"
                        ></textarea>
                    </div>   
                    
                    <button 
                        class="btn btn-sm btn-primary"
                        type="submit">
                        Pubblica Commento
                    </button>
                    
                </form>
                <br>
            </div>

        </div>
    `

})

// single comment component
Vue.component("single-comment", {
  
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
        <div class="comment mb-2">
            <div class="card">

                <div class="card-header">
                    <p>Pubblicato da : {{ comment.username }} </p>
                </div>

                <div class="card-body">
                    <p> {{ comment.content }} </p>
                </div>

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

        addNewComment(newComment) {
            this.comments.push(newComment)
        }

    },
})