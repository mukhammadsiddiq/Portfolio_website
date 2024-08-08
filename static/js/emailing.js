function sendMail(){
    let parms = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value,
    }

    emailjs.send("service_j84k1q9","template_ivmybyt",parms).then(alert("Email was sent successfully"))
}