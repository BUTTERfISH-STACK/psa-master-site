<?php
// Yoco Webhook Handler (Runs silently in background without altering frontend UI)
$input = file_get_contents('php://input');
$data = json_decode($input, true);

if (isset($data['type']) && $data['type'] === 'payment.succeeded') {
    $customerEmail = $data['payload']['customer']['email'] ?? '';
    
    if (!empty($customerEmail)) {
        $downloadLink = "https://" . $_SERVER['HTTP_HOST'] . "/download.php?token=" . hash('sha256', $customerEmail . 'PSA_SECURE_KEY');
        $subject = "Your PSA™ First Light Guide is Ready";
        $message = "Thank you for your purchase!\n\nDownload your guide instantly here: " . $downloadLink . "\n\nPowered by Pocket State Architecture.";
        $headers = "From: no-reply@" . $_SERVER['HTTP_HOST'];
        
        @mail($customerEmail, $subject, $message, $headers);
    }
}
http_response_code(200);
?>
