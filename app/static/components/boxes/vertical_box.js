export default {
    props: {
        height: String,
        width: String
    },

    setup(props) {
    },

    template: /*html*/`
        <div class="vertical-box" :style="{ height: height + 'rem', width: width + 'rem' }">
            <slot></slot>
        </div>
    `
}