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
            <label class="field-label">{{ label }}</label>
            <br/>
            <div class="field-container">
                <input :type="type" :value="value" :name="name" class="field" />
                <span class="icon-container">
                    <slot name="icon"></slot>
                </span>
            </div>
        </div>
    `
}