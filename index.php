<?php
require 'vendor/autoload.php';

$app = new \Slim\Slim();
$app->POST('/foo', function() {
    echo "I respond to multiple HTTP methods!";
});
$app->run();
?>