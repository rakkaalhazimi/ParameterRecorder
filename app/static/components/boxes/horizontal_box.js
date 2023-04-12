export default {
    props: {
        value: String
    },

    setup(props) {
    },

    template: /*html*/`
        <div class="horizontal-box">
            <slot></slot>
        </div>
    `
}