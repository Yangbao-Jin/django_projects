
/*$.ajax({
    url: 'https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
    type: 'GET',
    //dataType: 'html',

    success: function(data) {
        $('#output').html(data);
    
    },
    error: function(error) {
        console.error("Error occurred:", error);
    }
});*/

//$("#output").load("https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css");

var content = $('#output').html();
console.log(content);  

function initMap() {
    // 设置地图的中心点
    var center = {lat: -34.397, lng: 150.644};

    // 创建地图对象
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,
        center: center
    });

    // （可选）在地图上添加标记
    var marker = new google.maps.Marker({
        position: center,
        map: map
    });
}


$('#output').html('<strong>New content here</strong>'); 

navigator.geolocation.getCurrentPosition(function (position) {
    var latlng = new google.maps.LatLng(
      position.coords.latitude,
      position.coords.longitude,
    );
    var myOptions = {
      zoom: 16,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.TERRAIN,
      disableDefaultUI: true,
    };


    var map = new google.maps.Map(
      document.querySelector("#map_canvas"),
      myOptions,
    );
    var marker = new google.maps.Marker({
        position: latlng,  // 使用当前位置的经纬度
        map: map,          // 指定要在哪个地图上显示此标记
        title: "您的当前位置"  // （可选）鼠标悬停在标记上时显示的文本
    });
  });

const format = "PF";
const circuit = "National";
const year = "SY_20_21";

const contentNDSA = document.getElementById("contentNDSA");

fetch(`https://tournaments.tech/leaders?format=${format}&circuit=${circuit}&year=${year}`).then(response => {
  response.json().then(data => {
    contentNDSA.innerText = JSON.stringify(data);
  })
});