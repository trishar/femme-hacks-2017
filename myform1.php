<?php
if($_POST['formSubmit'] == "Submit")
{
	$errorMessage = "";

	if(empty($_POST['formSubmit']))
	{
		$errorMessage .= "<li>You forgot to enter a link!</li>";
	}

	$varLink = $_POST['fname'];

	if(empty($errorMessage))
	{
		$fs = fopen("mydata.csv","a");
		fwrite($fs,$varLink . "\n");
		fclose($fs);

		header("Location: index.html");
		exit;
	}
}
?>
