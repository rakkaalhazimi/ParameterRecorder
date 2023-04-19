import TrashSolid from "../icons/TrashSolid.js"

export default {
    props: {
        title: String,
    },

    components: {
        "TrashSolid": TrashSolid,
    },

    setup(props) {
    },

    template: /*html*/`
        <div class="project-card">
            <div class="project-card__header">
                <h3 class="project-card__title">{{ title }}</h3>
                <TrashSolid class="project-card__delete-icon"></TrashSolid>
            </div>

            <p class="project-card__desc">There are 0 records</p>
        </div>
    `
}