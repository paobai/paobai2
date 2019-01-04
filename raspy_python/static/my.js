 // 基于准备好的dom，初始化echarts实例
        
 function genxing_wendu24(result)
 {
  var myArray = new Array();
  var myChart = echarts.init(document.getElementById('wendu_pig'));

  var data = JSON.parse(result);
  var title = data['title'];
    if (title == null)
        title = "None";
  var count = data['count'];
  var interval = count/12;
  if(interval<1.5)
      interval=0;
    else
      interval = Math.floor(interval);
  var time_list = data['time_list'];
  var data_list = data['data_list'];
  // 指定图表的配置项和数据
  var option = {
      title: {
          text: title
      },
      tooltip: {},
      legend: {
          data:['销量']
      },
      xAxis: {
          data: time_list,
          axisLabel: {
           interval:interval,
           rotate:-70
        },

      },
      grid: {
               left: '10%',
               bottom:'23%'
               },
      yAxis: {
       type: 'value'
      },
      series: [{
          name: '时间',
          type: 'line',
          data: data_list
      }]};
      //return xmlhttp.responseText;
    myChart.setOption(option);
}


 function genxing_shidu24(result)
 {
  var myArray = new Array();
  var myChart = echarts.init(document.getElementById('shidu_pig'));

  var data = JSON.parse(result);
  var title = data['title'];
    if (title == null)
        title = "None";
  var count = data['count'];
  var interval = count/12;
  if(interval<1.5)
      interval=0;
    else
      interval = Math.floor(interval);
  var time_list = data['time_list'];
  var data_list = data['data_list'];
  // 指定图表的配置项和数据
  var option = {
      title: {
          text: title
      },
      tooltip: {},
      legend: {
          data:['销量']
      },
      xAxis: {
          data: time_list,
          axisLabel: {
           interval:interval,
           rotate:-70
        },

      },
      grid: {
               left: '10%',
               bottom:'23%'
               },
      yAxis: {
       type: 'value'
      },
      series: [{
          name: '时间',
          type: 'line',
          data: data_list
      }]};
      //return xmlhttp.responseText;
    myChart.setOption(option);
    }



 function wendu24_start()
 { 
     var xmlhttp;
    if (window.XMLHttpRequest)
      {// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
      }
    else
      {// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
      }
    xmlhttp.onreadystatechange=function()
      {
      if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
          genxing_wendu24(xmlhttp.responseText);
         }
      };
      

    var url = "/watch/wendu/24hour";
    var wendu_select = document.getElementById("wendu_select").value;
    url = url + '?value=' +wendu_select ;
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
    /*
    setInterval(function(){
		xmlhttp.open("GET",url,true);
		xmlhttp.send();
  },3600000)
  */
}



function shidu24_start()
{ 
    var xmlhttp;
   if (window.XMLHttpRequest)
     {// code for IE7+, Firefox, Chrome, Opera, Safari
     xmlhttp=new XMLHttpRequest();
     }
   else
     {// code for IE6, IE5
     xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
     }
   xmlhttp.onreadystatechange=function()
     {
     if (xmlhttp.readyState==4 && xmlhttp.status==200)
       {
         genxing_shidu24(xmlhttp.responseText);
        }
     };
     var url = "/watch/shidu/24hour";
     var wendu_select = document.getElementById("shidu_select").value;
     url = url + '?value=' +wendu_select ;
     xmlhttp.open("GET",url,true);
     xmlhttp.send();
   /*
   setInterval(function(){
   xmlhttp.open("GET","/watch/shidu/24hour",true);
   xmlhttp.send();
 },3600000)*/
}



function farm_state_now()
{ 
    var xmlhttp;
   if (window.XMLHttpRequest)
     {// code for IE7+, Firefox, Chrome, Opera, Safari
     xmlhttp=new XMLHttpRequest();
     }
   else
     {// code for IE6, IE5
     xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
     }
   xmlhttp.onreadystatechange=function()
     {
     if (xmlhttp.readyState==4 && xmlhttp.status==200)
       {
          result = JSON.parse(xmlhttp.responseText)
          document.getElementById("wendu_now").innerHTML = "现在温度：" +result['wendu']+"℃";
          document.getElementById("shidu_now").innerHTML = "现在温度：" +result['shidu'] +"%RH";
           document.getElementById("frequency_now").innerHTML = "现在声频频率为：" +result['frequency'];
           document.getElementById("size_now").innerHTML = "现在声频大小为：" +result['size'] + "%";
        }
     };

   var url = "/watch/state_now";
   xmlhttp.open("GET",url,true);
   xmlhttp.send();
   setInterval(function(){
   xmlhttp.open("GET",url,true);
   xmlhttp.send();
 },10000)
}
//
 //wendu24_start();
 //shidu24_start();
 //farm_state_now();


 function chooseProvince(){
    var obj = document.getElementById("wendu_select");
    var sele = obj.options;
    obj.onchange = function(){
        wendu24_start();
    }
    var obj2 = document.getElementById("shidu_select");
    var sele2 = obj2.options;
    obj2.onchange = function(){
        shidu24_start();
    }
}

function update_farm_now_pig(){
  setInterval(function(){
    $("#farm_pig").attr("src","static/farm_now.jpg?"+ Math.random());
  },10000)
  // document.getElementById("farm_pig").src="/static/farm_now.jpg?" +  Math.random();
  $("#farm_pig").attr("src","static/farm_now.jpg?"+ Math.random());
}

//废弃了。采用下面update_main_index_load的方法。
function update_main_index_text(text)
{
    document.getElementById("main_index").innerHTML = text;
}


 function update_main_index_load(file_name)
{
     $('#main_index').load('/templates/'+ file_name);
}

  function update_main_index_load_group(file_name)
{
     $('#main_index').load('/templates_group/'+ file_name);
}

 
   function update_main_index_load_settings(file_name)
{
     $('#main_index').load('/templates_settings/'+ file_name);
}


function watch_state()
{
  update_main_index_load("watch_text.html");
}
function load_message()
{
    update_main_index_load('load_index.html');
}
 function set_frequency()
{
    update_main_index_load('set_index.html');
}
 function analys()
{
    update_main_index_load('analys_index.html')
}

