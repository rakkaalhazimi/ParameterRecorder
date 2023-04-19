import Field from "../fields/levitate_field.js"
import Button from "../buttons/submit_button.js"
import EnvelopeSolid from "../icons/EnvelopeSolid.js"
import KeySolid from "../icons/KeySolid.js"


export default {

    props: {
        loginEndpoint: String,
        registrationEndpoint: String
    },

    setup(props) {

    },

    components: {
        "Button": Button,
        "Field": Field,
        "EnvelopeSolid": EnvelopeSolid,
        "KeySolid": KeySolid,
    },

    template: /*html*/`
        <form class="form glass-form" :action="registrationEndpoint" method="post">
            <h2 class="form__header-text">Register</h2>

            <div class="form__field-wrapper">
                <Field type="text" name="email" label="Email">
                    <template v-slot:icon>
                        <EnvelopeSolid class="field__icon"></EnvelopeSolid>
                    </template>
                </Field>

                <Field type="password" name="password" label="Password">
                    <template v-slot:icon>
                        <KeySolid class="field__icon"></KeySolid>
                    </template>
                </Field>

                <Field type="password" name="confirm_password" label="Confirm Password">
                    <template v-slot:icon>
                        <KeySolid class="field__icon"></KeySolid>
                    </template>
                </Field>
            </div>

            <Button value="Login"></Button>
            <p class="form__register-text">
                Already have an account?
                <a class="form__register-text-link" :href="loginEndpoint">
                    <strong>Sign In</strong>
                </a>
            </p>
        </form>
    `
}