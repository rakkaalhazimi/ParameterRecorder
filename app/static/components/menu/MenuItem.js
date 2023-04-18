export default {
    props: {
        value: String,
        link: String,
    },

    setup(props) {
    },

    template: /*html*/`
        <a :href="link">
            <li class="menu-item">
                <slot name="icon"></slot>
                <span class="menu-item__label">
                    {{ value }}
                </span>
            </li>
        </a>
    `
}