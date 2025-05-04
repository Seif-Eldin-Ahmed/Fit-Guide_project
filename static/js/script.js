document.getElementById('upload-form').addEventListener('submit',function (e) {

    // Stop the form from submitting when reloading the page
    e.preventDefault(); 

    // Get the form data
    let fdata= new FormData(this);

    // Send the form data to the server through a post request in this route /upload
    fetch('/upload', {
        method: 'POST',
        body: fdata
    })
    .then(response => response.json() ) 
    .then (data => {
        document.getElementById('result').innerText = "" + data.result;
        document.getElementById('header1').innerText = "" + data.header1;
        document.getElementById('p1').innerText = "" + data.p1;
        document.getElementById('header2').innerText = "" + data.header2;
        document.getElementById('p2').innerText = "" + data.p2;
        document.getElementById('p2sub').innerText = "" + data.p2sub;
        document.getElementById('p3').innerText = "" + data.p3;
        document.getElementById('p3sub').innerText = "" + data.p3sub;
        document.getElementById('p4').innerText = "" + data.p4;
        document.getElementById('p5').innerText = "" + data.p5;
        document.getElementById('sep1').innerText = "" + data.sep1;
        document.getElementById('sep2').innerText = "" + data.sep2;
        document.getElementById('sep3').innerText = "" + data.sep3;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}); 
