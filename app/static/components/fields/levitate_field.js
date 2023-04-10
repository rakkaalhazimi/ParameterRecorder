export default {
    props: {
        type: String,
        value: String,
        name: String,
        label: String,
    },

    setup(props) {
    },

    template: /*html*/`
        <div>
            <label>{{ label }}</label>
            <br/>
            <input :type="type" :value="value" :name="name" />
        </div>
    `
}