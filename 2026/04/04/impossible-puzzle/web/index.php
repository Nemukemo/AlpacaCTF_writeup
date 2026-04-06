<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $A = $_POST['A'] ?? '';
    $B = $_POST['B'] ?? '';

    // type check
    if (!is_string($A) || !is_string($B)) {
        die('Invalid input');
    }
    // check
    if (strlen($A) != strlen($B) && $A == $B){
        echo "<blockquote>Congratulations! Here is your flag:\n" . getenv('FLAG') . "</blockquote>";
    }
    else {
        echo "<blockquote>Try again!</blockquote>";
    }
}

?>

<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <title>Impossible Puzzle</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css" />
    <script src="https://cdn.jsdelivr.net/npm/dompurify@3.3.1/dist/purify.min.js"></script>
</head>

<body>
    <h1>Impossible Puzzle</h1>
    <p>Enter two strings A and B. If they are equal in content but different in length, you will get the flag!</p>
    <form method="post">
        <label for="A">A:</label>
        <input type="text" id="A" name="A" required>
        <label for="B">B:</label>
        <input type="text" id="B" name="B" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>