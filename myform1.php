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

		header("Location: thankyou.html");
		exit;
	}
}
?>
<!DOCTYPE html>
<html lang="en">
	<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Internships, FUNternships</title>

	<!--Bootstrap-->
	<link href="css/bootstrap.min.css" rel="stylesheet">
	<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

    <link href= "main.css" rel="stylesheet">

	<meta name="description" content="DESCRIBE YOUR WEBSITE">
	<meta name="keywords" content="KEY, WORDS, HERE">
	</head>
	<body>
		<div class="container bg-1 text-center">
	  		<h1> Internships, FUNternships </h1>
	  		<div class="row">
		  		<div class="row-sm-height">
		    		<div class="col-sm-4 col-height col-sm-middle text-center" >
		    			<div class="inside bg-2">
		    			<br>
		      			<h4>Tired of searching endlessly for internships? This website
						makes it easy to read internships related to your interests!
						Enter the link below, and we'll return keywords from the posting.
						Type in the box below to get started. </h4>
						<br>
						</div>
		    		</div>
		    		<div class="col-sm-8 col-height ">
		    			<div class="inside bg-3">
		    			<div class="form-group">
		      				<form action="myform1.php" method="post">
		  					<br>Enter Link Here: <br><input type="text" name="fname"><br>
		  					<input type="submit" value="Search!">
							</form>
						</div>
						</div>
		    		</div>
	    		</div>
	    	</div>
		</div>


		<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    	<!-- Include all compiled plugins (below), or include individual files as needed -->
    	<script src="js/bootstrap.min.js"></script>
  	</body>
</html>
