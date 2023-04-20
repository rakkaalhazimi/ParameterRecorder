import MenuItem from "../menu/MenuItem.js"
import EnvelopeSolid from "../icons/EnvelopeSolid.js"
import FolderSolid from "../icons/FolderSolid.js"
import HouseSolid from "../icons/HouseSolid.js"
import PowerOffSolid from "../icons/PowerOffSolid.js"

export default {
    props: {
        value: String
    },

    components: {
        "MenuItem": MenuItem,
        "EnvelopeSolid": EnvelopeSolid,
        "FolderSolid": FolderSolid,
        "HouseSolid": HouseSolid,
        "PowerOffSolid": PowerOffSolid
    },

    setup(props) {
    },

    template: /*html*/`
        <nav class="side-bar">

            <div class="side-bar__logo">
                <h3 class="side-bar__header">Parameter Recorder</h3>
            </div>

            <ul class="side-bar__menu-list">
                <MenuItem value="Home" link="#">
                    <template v-slot:icon>
                        <HouseSolid class="menu-item__icon"></HouseSolid>
                    </template>
                </MenuItem>
                <MenuItem value="Projects" link="#">
                    <template v-slot:icon>
                        <FolderSolid class="menu-item__icon"></FolderSolid>
                    </template>
                </MenuItem>
                <MenuItem value="Logout" link="#">
                    <template v-slot:icon>
                        <PowerOffSolid class="menu-item__icon"></PowerOffSolid>
                    </template>
                </MenuItem>
            </ul>

        </nav>
    `
}