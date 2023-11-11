
    const spamContainer = document.querySelector(".spams");
    const spamButton = document.getElementById("spamButton");
    const smsList = document.querySelector(".smsList")
    const smsButton = document.getElementById("smsButton")
    const sms = document.querySelector(".sms")
    const convo = document.querySelector(".conversation")
    const container1 = document.querySelector(".mainContainer")
    const btnBack = document.getElementById("btnBack")
    


    // Add a click event listener to the button
    spamButton.addEventListener("click", function () {
        spamContainer.style.display = "block"  
        smsList.style.display = "none"
    });

    smsButton.addEventListener("click", function(){
        smsList.style.display = "block"
        spamContainer.style.display = "none"
    })

    sms.addEventListener("click", function(){
        convo.style.display = "block"
        container1.style.display = "none"
    })

    btnBack.addEventListener("click", function() {
        convo.style.display = "none"
        container1.style.display = "block"
    })


    var newDiv = document.createElement('div');
    newDiv.className = 'sms'; // Set the class attribute

    // Create and append <p> elements inside the div
    var p1 = document.createElement('p');
    p1.textContent = 'Tan';

    var p2 = document.createElement('p');
    p2.textContent = "Hello webview";
    p2.style.marginLeft = '20px'; // Set the style attribute

    var p3 = document.createElement('p');
    p3.textContent = '12:03';

    newDiv.appendChild(p1);
    newDiv.appendChild(p2);
    newDiv.appendChild(p3);

    // Append the new div to the body of the document
    smsList.appendChild(newDiv);


