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
                <div class="project-card__header">
                    <h3 class="project-card__title">{{ title }}</h3>
                    <a :href="deleteLink">
                        <TrashSolid class="project-card__delete-icon"></TrashSolid>
                    </a>
                </div>

                <p class="project-card__desc">There are 0 records</p>
            </div>
        </a>
    `
}