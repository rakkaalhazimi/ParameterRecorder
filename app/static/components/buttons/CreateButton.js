export default {
    props: {
        value: String,
        createEndpoint: String,
    },

    setup(props) {
        console.log(props.createEndpoint)
    },

    template: /*html*/`
        <a :href="createEndpoint">
            <button class="btn create-btn">
                + {{ value }}
            </button>
        </a>
    `
}