<?php 

	$array = [1,2,3]; 

	$map = array_map(function($element){return $element*2;}, $array); 

	print_r($map); 


?>
