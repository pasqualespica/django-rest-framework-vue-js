
// instanze ROOT
var app = new Vue({ // option Object 

    // el sta per 'element' che si aspetta il selettore CSS
    el: "#myapp",
    // data object
    data: {
        // text: "",
        // checked: true,
        // city: null
        comment: null,
        comments: [],
        errors: null
    },
    methods: {
        onSubmit() {
            if (this.comment) {
                this.comments.push(this.comment);
                this.comment = null;
                if (this.errors) {
                    this.errors = null;
                }
            } else {
                this.errors = "Il campo commento non puo' essere vuoto";
            }

        }
    },
})