function formValidation()
{
var uname = document.registration.firstname;
var ulname = document.registration.lastname;
var uemail = document.registration.email;
var umobile = document.registration.mobilenumber;
var upass=document.registration.password;
var urpass = document.registration.repassword;
if(userid_validation(uname,5,40)) {
    if(lname_validation(ulname,5,40)) {
        if(ValidateEmail(uemail)) {
            if(ValidateMobile(umobile)) {
                if(CheckPassword(upass)) {
                    if(ConfirmPassword(upass,urpass)) {
                        return true;
                    }
                }
            }
        } 
    }
}

return false;

} 
function userid_validation(uid,mx,my) { 
    var letters = /^[A-Za-z]+$/;
    var uid_len = uid.value.length;
    if (uid_len == 0 || uid_len >= my || uid_len < mx )
    {
    alert("User Id should not be empty / length be between "+mx+" to "+my);
    uid.focus();
    return false;
    }
    if(uid.value.match(letters))
    {
    return true;
    }
    else
    {
    alert('Username must have alphabet characters only');
    uid.focus();
    return false;
    }
    return true;
}
function lname_validation(uid,mx,my) { 
    var letters = /^[A-Za-z]+$/;
    var uid_len = uid.value.length;
    if (uid_len == 0 || uid_len >= my || uid_len < mx )
    {
    alert("lastname should not be empty / length be between "+mx+" to "+my);
    uid.focus();
    return false;
    }
    if(uid.value.match(letters))
    {
    return true;
    }
    else
    {
    alert('User last name must have alphabet characters only');
    uid.focus();
    return false;
    }
    return true;
}

function ValidateEmail(uemail)
{
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
if(uemail.value.match(mailformat))
{
return true;
}
else
{
alert("You have entered an invalid email address!");
uemail.focus();
return false;
}
}

function ValidateMobile(umobile) {
  var l = /^[0123456789]+$/;
  var umobile_len = umobile.value.length;
  if (umobile_len != 10) {
    alert("enter valid phone number");
     umobile.focus();
    return false;
  }
  if (umobile.value.match(l))
  {
    return true
  }
  else
  {
    alert("enter valid phone number");
    umobile.focus();
    return false;
  }

}
function CheckPassword(inputtxt) 
{ 
var paswd=  /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;
if(inputtxt.value.match(paswd)) 
{ 
return true;
}
else
{ 
alert('password should have atleast 5 characters, one special character and a number');
inputtxt.focus();
return false;
}
}  
function ConfirmPassword(password,repassword) {
    var pass1 = password.value;
    var pass2 = repassword.value;
    var ok = true;
    if (pass1 != pass2) {
        alert("Passwords Do not match");
        repassword.focus();
        ok = false;
    }
    else {
        alert("form submitted successfully");
        window.location.reload();
        return ok;
    }
    
}
