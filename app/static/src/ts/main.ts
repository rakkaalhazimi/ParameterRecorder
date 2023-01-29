function elt(
        {type, attributes}: {type: string, attributes?: { [key: string]: string }}, 
        ...children: Node[] | string[]
    ): HTMLElement {
            
    let node = document.createElement(type)
    for (let key in attributes) {
        node.setAttribute(key, attributes[key])
    }

    for (let child of children) {
        if (typeof child != "string") node.appendChild(child)
        else node.appendChild(document.createTextNode(child))
    }
    return node
}

function createParameterInput(): HTMLElement {
    
    return elt({type: "tr"}, 
                elt({type: "td"}, 
                    elt({type: "input", attributes: {"name": "parameter_key", "required": ""}}),
                ),
                elt({type: "td"},
                    elt({type: "input", attributes: {"name": "parameter_value", "required": ""}}),
                ),
                elt({type: "td"},
                    elt({type: "button", attributes: {"onclick": "removeInput(event)"}}, "x"),
                ),
    )
}

function createResultInput(): HTMLElement {
    
    return elt({type: "tr"}, 
                elt({type: "td"}, 
                    elt({type: "input", attributes: {"name": "result_key", "required": ""}}),
                ),
                elt({type: "td"},
                    elt({type: "input", attributes: {"name": "result_value", "required": ""}}),
                ),
                elt({type: "td"},
                    elt({type: "button", attributes: {"onclick": "removeInput(event)"}}, "x"),
                ),
    )
}

function addParameterForm(event: Event): void {
    event.preventDefault()
    let currentObj: HTMLElement = event.target as HTMLElement
    while (currentObj.tagName.toLowerCase() != "tbody") {
        currentObj = currentObj.parentElement
    }
    currentObj.insertBefore(createParameterInput(), currentObj.children[currentObj.children.length - 1])
}

function addResultForm(event: Event): void {
    event.preventDefault()
    let currentObj: HTMLElement = event.target as HTMLElement
    while (currentObj.tagName.toLowerCase() != "tbody") {
        currentObj = currentObj.parentElement
    }
    currentObj.insertBefore(createResultInput(), currentObj.children[currentObj.children.length - 1])
}

function removeInput(event: Event): void {
    event.preventDefault()
    let currentObj: HTMLElement = event.target as HTMLElement
    while (currentObj.tagName.toLowerCase() != "tr") {
        currentObj = currentObj.parentElement
    }
    currentObj.remove()
}
