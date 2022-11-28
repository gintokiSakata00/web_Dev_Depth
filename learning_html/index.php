<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="contain">
    <h1>FOR LOOP</h1>
    <?php for ($i=1; $i < 500; $i++) { 
        if($i%2==0){
            echo "<input type='radio' name='check$i' >";
        }else{
            echo "<input type='radio' name='check$i' checked>";
        }
        
    } ?>
    </div>
</body>
</html>