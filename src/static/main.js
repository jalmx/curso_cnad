function sendData({ key, value }) {
    // console.log(`/?key=${key}&value=${value}`);
    window.location.href = `/?key=${key}&value=${value}`
}


function led(ledName) {

    const checkValue = document.getElementById(`${ledName}_check`).dataset.value

    sendData({ "key": ledName, "value": parseInt(checkValue) ? 0 : 1 })
}

function btn(btnName) {
    sendData({ "key": btnName, "value": 1 })
}
function action(elementName) {
    if (elementName.startsWith("led")) {
        led(elementName)
    } else if (elementName.startsWith("btn")) {
        btn(elementName)
    }
}


function checkElement(element) {

    if (element) {
        action(element)
    }
}


(function () {
    document.body.addEventListener("click", function (event) {

        const element = event.target.dataset.element
        checkElement(element)
    })

    document.body.addEventListener("change", function (event) {
        const element = event.target.dataset.element
        checkElement(element)
    })
})();