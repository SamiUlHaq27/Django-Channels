function socket() {
    var ws = new WebSocket("ws://127.0.0.1:8000/ws/sc/");

    ws.onopen = function () {
        console.log("connection openned...");
    }

    ws.onmessage = function (event) {
        console.log("message recieved...");
    }

    ws.onerror = function (event) {
        console.log("error occured...");
    }

    ws.onclose = function (event) {
        console.log("connection closed...");
    }
}

socket();