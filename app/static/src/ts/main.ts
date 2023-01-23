function incrementInputName(inputParent: HTMLElement): HTMLElement {
    let inputCollection = inputParent.getElementsByTagName("input")

    for (let i: number = 0; i < inputCollection.length; i++) {
        let currentName: string = inputCollection[i].getAttribute("name")
        let splittedName: string[] = currentName.split("_")
        let index: number = parseInt(splittedName.pop()) + 1
        splittedName.push(index.toString())
        inputCollection[i].setAttribute("name", splittedName.join("_"))
    }

    return inputParent
}

function addForm(event: Event): void {
    event.preventDefault()
    let currentObj: HTMLElement = event.target as HTMLElement
    while (currentObj.tagName.toLowerCase() != "tbody") {
        currentObj = currentObj.parentElement
    }
    let lastInputRow: HTMLElement = currentObj.querySelector("tr:nth-last-child(2)").cloneNode(true) as HTMLElement
    let incrementedInputRow: HTMLElement = incrementInputName(lastInputRow)
    currentObj.insertBefore(incrementedInputRow, currentObj.children[currentObj.children.length - 1])
}
