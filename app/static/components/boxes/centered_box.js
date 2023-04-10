export default {
    props: {
        value: String
    },

    setup(props) {
    },

    template: /*html*/`
        <div class="center-box">
            <slot></slot>
        </div>
    `
}