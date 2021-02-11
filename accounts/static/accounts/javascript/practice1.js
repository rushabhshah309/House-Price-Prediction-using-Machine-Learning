function validate() {
			var user=document.getElementById('yo');
			var pass=document.getElementById('yo1');
			if(user.value.trim()==""&&pass.value.trim()=="")
			{
				alert("Please enter username and password");
				pass.style.border="solid 3px red";
				user.style.border="solid 3px red";
				return false;
			}
			else if(pass.value.trim()=="")
			{
				alert("Please enter the password");
				pass.style.border="solid 3px red";
				return false;
			}
			else if(user.value.trim()=="")
			{
				alert("Please enter the username");
				user.style.border="solid 3px red";
				return false;
			}
			else if(pass.value.trim().length<5)
			{
				alert("Password too Short.Please enter atleast 5 characters");
				pass.style.border="solid 3px red";
				return false;
			}
			else
			{
				return true;
			}
		}