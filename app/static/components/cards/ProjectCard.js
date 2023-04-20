import TrashSolid from "../icons/TrashSolid.js"

export default {
    props: {
        title: String,
        viewLink: String,
        editLink: String,
        deleteLink: String
    },

    components: {
        "TrashSolid": TrashSolid,
    },

    setup(props) {

        let title = props.title

        function updateTitle(event) {
            if (title !== event.target.innerText) {

                // Send POST request with fetch API
                // ref: https://stackoverflow.com/questions/46640024/how-do-i-post-form-data-with-fetch-api
                let formData = new FormData()
                formData.append("name", event.target.innerText)
                fetch(props.editLink, {
                    method: "POST",
                    body: formData
                })

                title = event.target.innerText
            }
        }

        return {updateTitle}
    },

    template: /*html*/`
        <a :href="viewLink">
            <div class="project-card">
            <!-- Prevent anchor tag click -->
            <!-- ref: https://stackoverflow.com/questions/1369035/how-do-i-prevent-a-parents-onclick-event-from-firing-when-a-child-anchor-is-cli -->
            <div class="project-card__header">
                <h3
                    class="project-card__title"
                    contenteditable="true"
                    @focusout="updateTitle"
                    @click.prevent
                >{{ title }}</h3>
                <a :href="deleteLink">
                    <TrashSolid class="project-card__delete-icon"></TrashSolid>
                </a>
            </div>

                <p class="project-card__desc">There are 0 records</p>
            </div>
        </a>
    `
}