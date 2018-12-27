<!DOCTYPE html>
<html>
<head>
    <?php include './includes/config.php'?>
</head>
<body style="background-color:grey">
    <?php include './includes/header.php'?>

<div class="jumbotron"style="margin-left:200px; margin-right:200px;">
<div class="container">

<!-- main content -->
<h1>--pics<h1>

<span class="ddh_imgs">
<?php
$dir = new DirectoryIterator(dirname('./img'));
foreach($dir as $fileinfo){
    if (!$fileinfo->isDot()){
        print($fileinfo->getFilename() );
    }
}
?>
</span>

</div>
</div>


</body>
</html>