function func(event) {
    event.preventDefault();
    
    // calling the data of the form and set them to variables
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var country = document.getElementById("country").value;
    var gender = document.getElementById("gender");

    gender.checked ? gender = "Male" : gender = "Female";

    var age = document.getElementById("age").value;
    var weight = document.getElementById("weight").value;
    var height = document.getElementById("height").value;
    var illnesses = document.getElementById("illnesses").value;

    function goal()
    {
      var j1=document.getElementById("c1");
      var j2=document.getElementById("c2");
      var j3=document.getElementById("c3");
      var j4=document.getElementById("c4");
      var j5=document.getElementById("c5");
      var j6=document.getElementById("c6");
      
      if(j1.checked==true || j2.checked==true || j3.checked==true ||
        j4.checked==true || j5.checked==true || j6.checked==true)
        {
          if(j1.checked==true)
          {
            c1.value; 
          }
          if(j2.checked==true)
          {
            c2.value; 
          }
          if(j3.checked==true)
          {
            c3.value; 
          }
          if(j4.checked==true)
          {
            c4.value; 
          }
          if(j5.checked==true)
          {
            c5.value; 
          }
          if(j6.checked==true)
          {
            c6.value; 
          }function func(event) {
    event.preventDefault();
    
    // calling the data of the form and set them to variables
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var country = document.getElementById("country").value;
    var gender = document.getElementById("gender");

    gender.checked ? gender = "Male" : gender = "Female";

    var age = document.getElementById("age").value;
    var weight = document.getElementById("weight").value;
    var height = document.getElementById("height").value;
    var illnesses = document.getElementById("illnesses").value;

    function goal()
    {
      var j1=document.getElementById("c1");
      var j2=document.getElementById("c2");
      var j3=document.getElementById("c3");
      var j4=document.getElementById("c4");
      var j5=document.getElementById("c5");
      var j6=document.getElementById("c6");
      
      if(j1.checked==true || j2.checked==true || j3.checked==true ||
        j4.checked==true || j5.checked==true || j6.checked==true)
        {
          if(j1.checked==true)
          {
            c1.value; 
          }
          if(j2.checked==true)
          {
            c2.value; 
          }
          if(j3.checked==true)
          {
            c3.value; 
          }
          if(j4.checked==true)
          {
            c4.value; 
          }
          if(j5.checked==true)
          {
            c5.value; 
          }
          if(j6.checked==true)
          {
            c6.value; 
          }
        }
    }

}

        }
    }

}

// to call the id of the form and, link the data of the value of the form to the google sheet which we created
var form = document.getElementById('Pgform');
  form.addEventListener("submit", e => {    
    e.preventDefault();    
    fetch(form.action, {    
        method : "POST",
        body: new FormData(document.getElementById("Pgform")),
    }).then(    
        response => response.json()   
    ).then((html) => {    
      
      window.open('form-out.html', '_blank'),  
      alert('Signed Up Successfully✅')

    });
  });