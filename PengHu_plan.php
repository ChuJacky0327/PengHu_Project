<?php
  $DB_HOST = '127.0.0.1'; // 主機
  $DB_USER = 'root';  // 登入 MySQL server 的帳號
  $DB_PASS = '0327'; // 密碼
  $DB_NAME = 'penghu'; // 要登入的資料庫名稱
  $DB_PAGE = "SELECT * FROM realtimeplan";
  
  $conn = mysqli_connect($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
  $i= 0;
  $number=array();
  $Time=array();
  $place=array();
  $latitude=array();
  $longitude=array();
  if (!mysqli_select_db($conn, $DB_NAME)) {
    die("連接失敗" );
  }
  $result = mysqli_query($conn, $DB_PAGE);
  //MYSQLI_NUM(顯示資料表是用index),MYSQLI_ASSOC(顯示資料表是用id),MYSQLI_BOTH(顯示資料表index,id皆可)
  while ($row = mysqli_fetch_array($result, MYSQLI_BOTH)) {
    $number[$i]=$row['no'];
    $Time[$i]=$row['Time'];
    $place[$i]=$row['設置點'];
    $latitude[$i]=$row['緯度'];
    $longitude[$i]=$row['經度'];
    $i++;
  }
  //printf("%s,%s,%s,%s,%s,%s",$number[1],$Time[1],$UserID[1],$place[1],$latitude[1],$longitude[1]);

?>

<!DOCTYPE html>
<html>
    
    <style>
        html, body{
            width: 100%;
            height: 100%;
        }
        #map{
            width: 100%;
            height: 100%;
        }
    </style>

    
    <div id="map"></div>

    <script type="text/JavaScript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js" ></script>
    
    <script>

        var JS_number = ["<?php echo join("\", \"", $number); ?>"];//PHP array to JS array
        var JS_Time = ["<?php echo join("\", \"", $Time); ?>"];
        var JS_place = ["<?php echo join("\", \"", $place); ?>"];
        var JS_latitude = ["<?php echo join("\", \"", $latitude); ?>"];
        var JS_longitude = ["<?php echo join("\", \"", $longitude); ?>"];
        console.log(JS_longitude[0])
        var map;
        function initMap(){


            map = new google.maps.Map(document.getElementById('map'), {
                center: {lat: 23.57226, lng: 119.57102},
                zoom: 17,
                mapId: "5cb7f499bf3d65",
                
            });
           
            var marker, i, Date, CSVtime;
            var count = 0;


            for (i = 0; i < JS_number.length; i++) {//130275
                var measle = new google.maps.Marker({
                    position: new google.maps.LatLng(JS_latitude[i],JS_longitude[i]),
                    map: map,
                    icon: {
                        url: "https://i.imgur.com/iM0IY7A.jpg",//https://i.imgur.com/RcsQXFc.png -> redcircle 
                        scaledSize: new google.maps.Size(25, 25),
                        anchor: new google.maps.Point(4, 4),
                        
                    },
                    opacity: 0.5
                });
                var contentString = JS_Time[i] +"\n"+ JS_place[i];
                var infowindow = new google.maps.InfoWindow({
                    position: new google.maps.LatLng(JS_latitude[i],JS_longitude[i]),
                    map: map,
                    content: contentString,
                    maxWidth: 400
                });
            }
            console.log(count);        
        }

       
       
    </script>
    
    <script
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAgEx2LBAiVmEEmFPFfalI0sAZ-niR_UUg&callback=initMap"
      async
    ></script>

</html>

<!--
<!DOCTYPE html>
<html>
    
    <style>
        html, body{
            width: 100%;
            height: 100%;
        }
        #map{
            width: 100%;
            height: 100%;
        }
    </style>


    <input type="text" placeholder="input Time" id ="TIME"/>
    <input type="text" placeholder="input AM or PM" id ="AMorPM"/>
    <button class="submitBtn">SUBMIT</button>
    


    <div id="map"></div>

    <script type="text/JavaScript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js" ></script>
    <script src="D:\中央通訊碩士\合盟澎湖\Beacon\node_modules\jquery-csv\src\jquery.csv.js"></script>
    <script>
        
        $.ajax({
            //url: "Beacon20220519-DeleteSpace.csv",
            url: "Beacon20220519-DeleteRepeat.csv",
            async: false,
            success: function (csvd) {
                data = $.csv.toArrays(csvd);
                console.log(data)
            },
            
            dataType: "text",
            complete: function () {
                console.log("1233")
                
                // call a function on complete 
            }       
        });

    </script>

    

    
    
    <script>
        var TIME = document.getElementById("TIME");
        var AMorPM = document.getElementById("AMorPM");
        var submitBtn = document.querySelector(".submitBtn");
        var str = "";
        var str2 = "";
        function FsubmitBtn() {
            
            var submitValue = TIME.value;
            var submitValue2 = AMorPM.value;
            str = submitValue;
            str2 = submitValue2;
            //console.log(str);
            initMap();
            return str,str2;

        }
        submitBtn.addEventListener("click", FsubmitBtn);
        //console.log(str2);


        var map;
        function initMap(){
            console.log(str2);

            map = new google.maps.Map(document.getElementById('map'), {
                center: {lat: 23.57226, lng: 119.57102},
                zoom: 17,
                mapId: "5cb7f499bf3d65",
                
            });
           
            var marker, i, Date, CSVtime;
            var count = 0;


            for (i = 1; i < 5100; i++) {//130275
                Date = data[i][0].split(/\s+/);
                //console.log(Date[2]);
                CSVtime = Date[1].split(':');
                //console.log(CSVtime[0]);

                if (CSVtime[0] == str && Date[2] == str2 ){
                    //console.log(data[i][2]);
                    count = count + 1;
                    var measle = new google.maps.Marker({
                        position: new google.maps.LatLng(data[i][4],data[i][5]),
                        map: map,
                        icon: {
                            url: "redpeople.png",//red.png
                            scaledSize: new google.maps.Size(20, 20),
                            anchor: new google.maps.Point(4, 4),
                            
                        },
                        opacity: 0.5
                    });
                    /*var contentString = data[i][0]
                    var infowindow = new google.maps.InfoWindow({
                        position: new google.maps.LatLng(data[i][4],data[i][5]),
                        map: map,
                        content: contentString,
                        maxWidth: 400
                    });*/
                }
            }
            console.log(count);        
            //console.log(data[i][4]);
            //console.log(data[i][5]);
        }

       
       
    </script>
    
    <script
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAgEx2LBAiVmEEmFPFfalI0sAZ-niR_UUg&callback=initMap"
      async
    ></script>

</html>
-->