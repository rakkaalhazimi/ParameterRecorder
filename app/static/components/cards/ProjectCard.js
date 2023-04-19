export default {
    props: {
        title: String,
    },

    components: {
    },

    setup(props) {
    },

    template: /*html*/`
        <div class="project-card">
            <h3 class="project-card__title">{{ title }}</h3>
            <p class="project-card__desc">There are 0 records</p>
        </div>
    `
}