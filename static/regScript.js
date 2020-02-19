/**
 * Author: Jake Wachs
 * JS for registration page
 * Date: 17 Feb 2020
 */

document.getElementById("submitBtn").addEventListener("click", () => {
    //const proxy = "https://cors-anywhere.herokuapp.com/";
    const serverURL = "http://localhost:5000/api/v1/users";

    /* Crafting body of JSON */
    var payload = {
        "username": document.getElementById("name").value,
        "email": document.getElementById("email").value,
        "password": document.getElementById("password").value
    };
    var body = JSON.stringify(payload);

    fetch(serverURL, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: body
    })
    .catch((e) => {
        console.log(e);
    });
});
