window.addEventListener("load", () => {
    fetch("http://localhost:5000", () => {
        method: 'GET'
    })
    .then((res) => {
        console.log(res);
    });
});

document.getElementById("myBtn").addEventListener("click", () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            console.log(position);
            let long = position.coords.longitude;
            let lat = position.coords.latitude;

            alert("long is: " + long + "\nlat is: " + lat);
        });
    }
});

document.getElementById("req").addEventListener("click", () => {
    const serverURL = "http://localhost:5000/api/v1/handleRegistration";          // FIXME: replace w/ heroku server API

    fetch(serverURL, {
        method: 'POST',
        body: JSON.stringify("placeholder")
    })
/*
        .then(response => {
            return response.json();
        })
        .then(data => {
            console.log(data);
        });
*/
        .then(() => { console.log("posted!"); });
});
