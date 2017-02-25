<?php
if($_POST['formSubmit'] == "Submit")
{
	$errorMessage = "";

	if(empty($_POST['formSubmit']))
	{
		$errorMessage .= "<li>You forgot to enter a website!</li>";
	}

	$varLink = $_POST['fname'];

	if(empty($errorMessage))
	{
		$fs = fopen("mydata.csv","a");
		fwrite($fs,$varName . ", " . $varMovie . "\n");
		fclose($fs);

		header("Location: thankyou.html");
		exit;
	}

}
