<?php
// Secure Local PDF Delivery Hook for PSA™ First Light Guide (Runs silently in background)
$file = 'downloads/PSA-First-Light-Guide.pdf';

if (file_exists($file)) {
    header('Content-Description: File Transfer');
    header('Content-Type: application/pdf');
    header('Content-Disposition: attachment; filename="' . basename($file) . '"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($file));
    readfile($file);
    exit;
} else {
    header("HTTP/1.0 404 Not Found");
    echo "Digital asset is currently synchronizing.";
}
?>
