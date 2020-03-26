Vue.component("to-do", {

    props: {
        tasks: {
                type: Array,
                required: true
        },
        amount: {
                type: Number,
                required: true
        }
    },

    // Vedi - template - dove sono utlizzati
    data() {
        return {
            new_task: null,
            error: null,

        }

    },

    methods: {
        submitTask() {
            if (this.new_task) {
                this.$emit("add-task", this.new_task);
                this.new_task = null;
                if (this.error) {
                    this.error = null;
                }
            } else {
                this.error = "Il campo non puo' essere vuoto"
            }
        },
        removeTask(task_2_del) {
            this.$emit("del-task", task_2_del); // ricordarsi di mettersi in ascolo nel app ( html )
        }
    },

    // evento ENTER ( e non tasto ) per inserimento task a cui 
    // assegnamo la funzione definita `submitTask`

    // su onclick di alert-success eliminiamo il task
    template: `
        <div class="container mt-2">
            <p><strong>Task rimanenti : {{ amount }} </strong></p>
            <input type="text"
                    class="form-control"
                    placeholder="aggiungi un nuovo task"
                    v-model="new_task"
                    @keyup.enter="submitTask"
                    >


            <br>

            <div
                v-for="(task, index) in tasks"
                :task="task"
                :key="index" 
                class="single-task"
            >
            
                <div class="alert alert-success" >
                    {{ task }}
                    <button 
                        type="button" 
                        class="close no-outline"
                        @click="removeTask(task)"
                        >
                    <span>&times;</span>
                    </button>
                </div>

            
            </div>

            <em v-if="error"> {{ error }} DAJE !!! </em>
            <p v-if="amount===0"> Per aggiungere un nuovo task scrivere e premere invio</p>
        </div>
    `
})

// instanze ROOT
var app = new Vue({ // option Object 

    // el sta per 'element' che si aspetta il selettore CSS
    el: "#myapp",
    data: {
        tasks: [],

    },

    // computed properties
    computed: {
        taskCount() {
            return this.tasks.length;
        }
    },

    methods: {
        addNewTask(nuovo_task) {
            this.tasks.push(nuovo_task);
        },
        rimuoviTask(task_da_cancellare){
            this.tasks.splice(this.tasks.indexOf(task_da_cancellare), 1);
        }


    },
})