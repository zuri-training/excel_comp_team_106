<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>


    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap" rel="stylesheet">

</head>


<style>
    * {
        margin: 0px;
        padding: 0px;
    }

    html,
    body {
        scroll-behavior: smooth;
        margin: 0;
        padding: 0;
        min-width: 100%;
        height: 100vh;
        max-height: 100vh;
        background-color: #fafafa;
        color: #001847;


    }


    #navbar {
        background-color: #fff;
        font-family: 'Raleway', sans-serif;
        display: flex;
        justify-content: space-between;
        padding: 2rem 3rem;
    }

    #xl-sweep-logo {
        display: flex;
        align-items: left;
        justify-content: left;
    }

    #xl-logo {
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        position: relative;
    }

    .green-logo {
        position: absolute;
        top: -35%;
        left: -6%;
    }

    .logo {
        height: 30px;
        margin-right: 10px;
    }

    .sweep {
        font-size: 20px;
        font-weight: 800;
        color: #003DB1;
        line-height: 23px;
    }

    ul {
        display: flex;
        list-style-type: none;
    }

    li a {
        margin-right: 20px;
        margin-left: 20px;
        text-decoration: none;
        color: #000;
        font-weight: 700;
        font-size: 16px;
        line-height: 24px;
    }

    .nav-btn button {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 400;
        font-size: 16px;
        line-height: 20px;
        letter-spacing: 0.1px;
        border-radius: 5px;
        margin-right: 15px;
    }

    .sign-in {
        background-color: #fff;
        color: #003DB1;
        border: 1px solid #003DB1;
    }

    .sign-up {
        background-color: #003DB1;
        color: #fff;
        border: 1px solid #003DB1;
    }

    header {
        background-color: #ffffff;
        box-sizing: border-box;
        border-bottom: 1px solid #B3B3B4;


    }


    .flexbox {

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
       
        width: 100%;


    }

    .first-box {

      
        



    }

    .filename {
        display: flex;
    font-family: 'Space Grotesk';
   width: 590px;
   height: 64px;
   background-color: #AAC2F1;
   align-items: center;
 position: relative;
 bottom: 5px;
 border-radius: 8px 8px 0px 0px;
 
 

    }

    .filename-img{
width: 15.5px;
height: 15.5px;
margin-left: 390px;

    }

.p{
    margin-left: 20px;
}

    .btn{
       
    }

   
   
    .second-box {

      

    }

    .second-line{
        width: 590px;
        height: 64px;
        background-color: #f5f5f5;
        display: flex;
        justify-content: center;
        align-items: center;

    }

.second{
    display: flex;
width: 18px;
height: 18px;

}

.right-topbox{
    
margin-left: 20px;

}


.middle-two{

margin-left: 20px;
}

.bottom-two{
   margin-left: 20px;
}


.zoom-minus{
    position: relative;
    right: 250px;
}

.btn{
      position: relative;
    right: 200px;

}

.zoom-plus{
[O    position: relative;
right: 160px;
}

.hand{
    position: relative;
   right: 70px;
}

.download{
[I    position: relative;
    left: 80px;
}

.middle{
    width: 590px;
    height: 714px;
    overflow: scroll;
    position: relative;
    margin-top: 5px;
    background-color: #f5f5f5;
}

.bottom{
    display: flex;
    justify-content: center;
    width: 590px;
    height: 66px;
    align-items: center;
    overflow: scroll;
    margin-top: 5px;
    border-radius: 0px 0px 8px 8px;
  background-color: #f5f5f5;

}

.left-arrow{
width: 18px;
height: 16px;
position: relative;
right: 30px;


}


.right-arrow{
    width: 18px;
height: 16px;
position: relative;
left: 30px;
}

.container{
        min-height: 100%;
        margin-top: 88px;
    }


    .main{
         
        padding-bottom: 100px;
    }

    .download-one{
        display: flex;
        flex-direction: row;
    }
    .image{
        width: 10px;
        height: 10px;
    }

   

   #download{
    margin-left: 170px;
    width: 254px;
    height: 52px;
    border-radius: 8px;
    border: none;
    background-color: rgba(31, 31, 31, 0.12);
    margin-top: 20px;
    font-family: 'Space Grotesk';
    color: #1C1B1F;
   

   }

  
   .duplicates{
    display: flex;
    flex-direction: column;
    font-family: 'Space Grotesk';
    margin-left: 50px;
    margin-top: 70px;
   }


</style>

<body>

    <header>
        <nav id="navbar">
            <div id="xl-sweep-logo">
                <div id="xl-logo">
                    <div class="green-logo">
                        <img class="logo" src="picss/Vector.png" class="vectorgreen" alt="">
                    </div>
                    <div class="blue-logo">
                        <img class="logo" src="picss/Vector-1.png" class="vectorblue" alt="">
                    </div>
                </div>
                <div class="sweep">
                    <h2>XL SWEEP</h2>
                </div>
            </div>

        </nav>
    </header>

    <main>

        
        <div class="container">

            <div class="main">


        <div class="flexbox">

            <div class="first-box">

                <div class="filename">
                    <p class="p">Filename 2015csv.</p>
                    <img src="picss/x.png" alt="x" class="filename-img" >
                </div>
                <div class="second-line">
                <div class="second">
                    <img src="picss/zoom.png" alt="zoom-" class="zoom-minus">
                    <button class="btn">100%</button>
                    <img src="picss/zoom +.png" alt="zoom+" class="zoom-plus">
                    <img src="picss/hand.png" alt="hand" class="hand">
                    <img src="picss/share.png" alt="share" class="share">
                    <img src="picss/download.png" alt="download" class="download">
                </div>
            </div>

                <div class="middle">

                </div>

                <div class="bottom">
                    <img src="picss/left arrow.png" alt="left-arrow" class="left-arrow">
                    <img src="picss/right arrow.png" alt="right-arrow" class="right-arrow">
                </div>

                <div class="download-one">
                
                <button id="download">Download</button>
                

            </div>

            <div class="duplicates">
                <p >Duplicates</p>&nbsp;&nbsp;&nbsp;
                <p >Differences</p>&nbsp;&nbsp;&nbsp;
            </div>


            </div>





            <div class="second-box">
                <div class="right-topbox">

                <div class="filename">
                    <p class="p">Filename 2015csv.</p>
                    <img src="picss/x.png" alt="x" class="filename-img">
                </div>
                <div class="second-line">
                <div class="second">
                    <img src="picss/zoom.png" alt="zoom-" class="zoom-minus">
                    <button class="btn">100%</button>
                    <img src="picss/zoom +.png" alt="zoom+" class="zoom-plus">
                    <img src="picss/hand.png" alt="hand" class="hand">
                    <img src="picss/share.png" alt="share" class="share">
                    <img src="picss/download.png" alt="download" class="download">
                </div>
            </div>
            </div>

            <div class="middle-two">

                <div class="middle">

                </div>
            </div>

                <div class="bottom-two">

                <div class="bottom">
                    <img src="picss/left arrow.png" alt="left-arrow" class="left-arrow">
                    <img src="picss/right arrow.png" alt="right-arrow" class="right-arrow">
                </div>

            </div>
            <div class="download-one">
                
                <button id="download">Download</button>
                
            </div>
            <div class="duplicates">

                <p >Duplicates</p>&nbsp;&nbsp;&nbsp;
                <p >Differences</p>&nbsp;&nbsp;&nbsp;


            </div>


            </div>




        </div>
        </div>
        </div>



    </main>

</body>

</html>
