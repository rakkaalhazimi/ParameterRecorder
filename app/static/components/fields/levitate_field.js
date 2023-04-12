const {ref, reactive} = Vue

export default {
    props: {
        type: String,
        value: String,
        name: String,
        label: String,
    },

    setup(props) {

        let state = reactive({isFocus: false})

        function fieldFocusIn(event) {
            state.isFocus = true
        }

        function fieldFocusOut(event) {
            state.isFocus = false
        }

        return {fieldFocusIn, fieldFocusOut, state}
    },

    template: /*html*/`
        <div class="field">
            <label class="field__label" :class="{'field__label--focus': state.isFocus}">
                {{ label }}
            </label>
            <br/>
            <div class="field__wrapper" :class="{'field__wrapper--focus': state.isFocus}">
                <input
                    @focusin="fieldFocusIn"
                    @focusout="fieldFocusOut"
                    :type="type"
                    :value="value"
                    :name="name"
                    class="field__input"
                />
                <span
                    class="field__icon-wrapper"
                    :class="{'field__icon-wrapper--focus': state.isFocus}">
                    <slot name="icon"></slot>
                </span>
            </div>
        </div>
    `
}