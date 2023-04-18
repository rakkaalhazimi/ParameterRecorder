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
                <span class="menu-item__icon-wrapper">
                    <slot name="icon"></slot>
                </span>

                <span class="menu-item__label">
                    {{ value }}
                </span>
            </li>
        </a>
    `
}