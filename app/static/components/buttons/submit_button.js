export default {
    props: {
        value: String
    },

    setup(props) {
    },

    template: /*html*/`
        <button class="btn submit-btn">
            {{ value }}
        </button>
    `
}