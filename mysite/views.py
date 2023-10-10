#This file is creadted by me
from django.http import  HttpResponse
def index(request):
    return HttpResponse(''''"<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maharashatra Bank</title>
    <link rel="stylesheet" href="Css/style.css">

</head>
<style>
    body {
        background: url('bank.jpeg');
        background-size: 100%;
        height: 2000px;

    }

    /* .left {
        border: 2px solid black;
        display: inline-block;
        left: 30px;
        /* margin: 1px auto; */
    /* color: black; */
    /* top: 9px; */





    .right img {

        border: 1px solid black;
        border-radius: 83px;

        margin: -1px 22px;

        width: 136px;
    }



    .mid {
        border: 2px solid #151414;
        margin: 25px -5px;
        display: block;
        width: 82%;
        padding: 4px -5px;
        display: block;
        border-radius: 37px;
        font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;

    }

    .right {
        /* border: 2px solid purple; */
        display: inline-block;

        /* padding: 2px 38px; */
        position: fixed;
        /* text-align: right; */
        /* margin: 4px -4px; */
        right: 30px;
        margin: 1px auto;
        color: black;
        top: 9px;


    }

    .right h1 {
        text-align: center;
        font-size: 20px;

        position: relative;

    }

    .bk li {
        display: inline-block;
    }


    .bk li a {
        text-decoration: none;
        display: inline-block;
        /* margin: 10px 10px;*/
        padding: 19px 20px;
        color: black;
        font-size: 18px;

    }

    .bk li a:hover,
    .bk li a:active {
        text-decoration: underline;
        color: white
    }

    a:-webkit-any-Link {
        cursor: pointer;
    }

    .form {
        /* background-color: bisque; */
        width: 21%;
        text-align: center;
        margin: 48px;
        padding: 46px auto;
        border: 2px solid grey;
        border-radius: 24px;
        height: 23%;
    }

    .form input {
        background-color: black;
        margin: 16px 14px;
        border: 2px solid grey;
        border-radius: 6px;
        font-size: 15px;
        /* font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif; */
        color: solid white;
    }

    .form-group input {
        color: white;
    }

    .form button {
        background-color: #151414;
        color: white;
        margin: 34px auto;
        padding: 8px 10px;
        font-size: 12px;
        border: #975454;
        border: 2px solid rgb(250, 213, 213);
        border-radius: 8px;
        width: 82px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }
    .form button:hover{
        background-color: #968c8c;
    }

    .container input {
        color: black;
        border: 2px solid #968c8c;
        display: inline-block;
        float: right;
        margin: -49px 38px;
        font-size: 18px;
        border: none;
        padding: 1px 23px;
        border-radius: 12px;
    }
</style>

<body>

    <header>
        <div class="container">
            <!-- <div class="left">
                <button class="btn">Login</button>
                <button class="btn">Logout</button>
               
            </div> -->
            <div class="mid">
                <ul class="bk">

                    <li><a href="#">Home</a></li>
                    <li><a href="#">Status</a></li>
                    <li><a href="#">Update</a></li>
                    <li><a href="#">About us</a></li>
                    <li><a href="#">Contact us</a></li>
                    <li><a href="#">info</a></li>

                </ul>
                <input type="search" name="search" id="search" placeholder="Search">




            </div>
            <div class="right">
                <img src="banl_logo.jpg.png" alt="" class="jpg">
                <h1>Bank of Maharashatra</h1>

            </div>
        </div>
    </header>
    <div class="form">
        <h1>Login</h1>
        <form action="noacation.php">
            <div class="form-group">
                <input type="text" placeholder="Enter your name">
            </div>
            <div class="form-group">
                <input type="text" placeholder="Account number">
            </div>
            <div class="form-group">
                <input type="text" placeholder="Date of birth">
            </div>
            <div class="form-group">
                <input type="text" placeholder="Password">
            </div>
            <button class="submit">Submit</button>
        </form>
    </div>

</body>

</html>"''')
def about(request):
    return HttpResponse("Good morning!")