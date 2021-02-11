function validate()
{
	var flag1=document.getElementById('yo1');
	var flag2=document.getElementById('yo2');
	var flag3=document.getElementById('yo3');
	var flag4=document.getElementById('yo4');
	var flag5=document.getElementById('yo5');
	var flag6=document.getElementById('yo6');

	var flag8=document.getElementById('yo8');
	var flag9=document.getElementById('yo9');
	var flag10=document.getElementById('yo10');
	var flag11=document.getElementById('yo11');
	var flag12=document.getElementById('yo14');
	var flag13=document.getElementById('yo15');
	if(flag1.value.trim()=="")
	{
		alert("Please enter the no of bedrooms");
		return false;
	}
	else if(flag2.value.trim()=="")
	{
		alert("Please enter the no of bathrooms");
		return false;
	}
	else if(flag3.value.trim()=="")
	{
		alert("Please enter the area of square feet of living");
		return false;
	}
	else if(flag4.value.trim()=="")
	{
		alert("Please enter the area of square feet LOT");
		return false;
	}
	else if(flag5.value.trim()=="")
	{
		alert("Please enter the no of floors");
		return false;
	}
	else if(flag6.value.trim()=="")
	{
		alert("Please enter the area above in square feet");
		return false;
	}

	else if(flag8.value.trim()=="")
	{
		alert("Please enter the area of basement in square feet");
		return false;
	}
	else if(flag9.value.trim()=="")
	{
		alert("Please enter the zipcode");
		return false;
	}
	else if(flag10.value.trim()=="")
	{
		alert("Please enter the square feet living15");
		return false;
	}
	else if(flag11.value.trim()=="")
	{
		alert("Please enter the square feet LOT15");
		return false;
	}
	else if(flag12.value.trim()=="")
	{
		alert("Please enter the square feet LOT15");
		return false;
	}
	else if(flag13.value.trim()=="")
	{
		alert("Please enter the square feet LOT15");
		return false;
	}
	else if(flag1.value<0||flag1.value>50)
	{
		alert("Please enter an appropriate integer for bedrooms");
		return false;
	}
	else if(flag2.value<0||flag2.value>10)
	{
		alert("Please enter an appropriate integer for bathrooms");
		return false;
	}
	else if(flag3.value<290||flag3.value>20000)
	{
		alert("Please enter an appropriate value for square feet of living");
		return false;
	}
	else if(flag4.value<520||flag4.value>25000)
	{
		alert("Please enter an appropriate value for square feet of LOT");
		return false;
	}
	else if(flag5.value<1||flag5.value>7)
	{
		alert("Please enter a positive integer for the no of floors");
		return false;
	}
	else if(flag6.value<290||flag6.value>20000)
	{
		alert("Please enter an appropriate value for the area above land in square feet");
		return false;
	}

	else if(flag8.value<0||flag8.value>20000)
	{
		alert("Please enter an appropriate value for the area of basement in square feet");
		return false;
	}
	else if(flag10.value<399||flag10.value>30000)
	{
		alert("Please enter an appropriate value for sqft_living15");
		return false;
	}
	else if(flag11.value<651||flag11.value>100000)
	{
		alert("Please enter an appropriate value for sqft_LOT15");
		return false;
	}
	else if(flag4.value<flag3.value)
	{
		alert("sqft_living cannot be greater than sqft_LOT");
		return false;
	}
	/*else if(flag11.value<flag10.value)
	{
		alert("sqft_living15 cannot be greater than sqft_LOT15");
		return false;
	}*/
	else if(flag12.value>2020||flag13.value>2020)
	{
	    alert("please enter proper year");
	    return false;
	}
	else if(flag12.value!=0)
	{
	    if(flag13.value>flag12.value)
	    {
	        alert("Please enter proper year");
	        return false;
	     }
	}
	else
	{
		return true;
	}
}