import TrashSolid from "../icons/TrashSolid.js"

export default {
    props: {
        title: String,
        viewLink: String,
        deleteLink: String
    },

    components: {
        "TrashSolid": TrashSolid,
    },

    setup(props) {
    },

    template: /*html*/`
        <a :href="viewLink">
            <div class="project-card">
            <!-- Prevent anchor tag click -->
            <!-- ref: https://stackoverflow.com/questions/1369035/how-do-i-prevent-a-parents-onclick-event-from-firing-when-a-child-anchor-is-cli -->
            <div class="project-card__header" @click.prevent>
                <h3 class="project-card__title" contenteditable="true">{{ title }}</h3>
                <a :href="deleteLink">
                    <TrashSolid class="project-card__delete-icon"></TrashSolid>
                </a>
            </div>

                <p class="project-card__desc">There are 0 records</p>
            </div>
        </a>
    `
}