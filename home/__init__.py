<html lang = "en">
<head>
<meta charset = "UTF-8">    
<meta name="viewport" content="width=device-width, initial-scale=0.1">
<title>Contact Us - Delicious Bites </title>
<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #fff8f0;
    color: #333;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
}
header {
    background-color: #d35400
    padding: 15px 20px;
}
header a {
    color: White;
    text-decoration: none;
    font-size:18px;
    margin-right: 15px;
}
.container {
    padding: 20px;
    margin: auto;
    max-width:800px;
}
</style>
</head>
<body>
    <header>
    <a href="index.html">Home</a>
    <a href="/menu"> Menu</a>
    </header>
<div class="container">
    <h1>{{ restaurent_name}}</h1>
    <p class="phone"> Call us: {{9999999999}} </p>
</div>
</body>
</html>