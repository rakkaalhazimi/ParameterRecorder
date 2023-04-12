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
        <div class="field">
            <label class="field__label">{{ label }}</label>
            <br/>
            <div class="field__wrapper">
                <input :type="type" :value="value" :name="name" class="field__input" />
                <span class="field__icon-wrapper">
                    <slot name="icon"></slot>
                </span>
            </div>
        </div>
    `
}