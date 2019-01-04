/**
 * Created by Administrator on 2018/12/30 0030.
 */
function analys_generate_line()
{
    update_main_index_load_group('analys_generate_line.html');
}

function analys_export()
{
    update_main_index_load_group('analys_export.html');
}

  function updata_analys(result)
 {
   var myArray = new Array();
   var myChart = echarts.init(document.getElementById('analys_pig'));

   var data = result;
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
       	//     dataZoom : [
	    // 	{
         //        type: 'slider',
         //        show: true,
         //        start: 94,
         //        end: 100,
         //        handleSize: 8
         //    },
         //    {
         //        type: 'inside',
         //        start: 94,
         //        end: 100
         //    },
         //    {
         //        type: 'slider',
         //        show: true,
         //        yAxisIndex: 0,
         //        filterMode: 'empty',
         //        width: 12,
         //        height: '70%',
         //        handleSize: 8,
         //        showDataShadow: false,
         //        left: '93%'
         //    }
	    // ],
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