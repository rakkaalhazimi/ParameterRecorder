export default {
    props: {
        message: String
    },

    setup(props) {
    },

    template: /*html*/`
        <form class="glass-form">
            <slot></slot>
        </form>
    `
}