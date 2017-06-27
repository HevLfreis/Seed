/**
 * Created by hevlhayt@foxmail.com
 * Date: 2017/6/18
 * Time: 15:10
 */
$(function () {


    
    $.get('http://api.seeleit.com/dott', function(res) {

        var list = [];

        var min_distance = 0.001*0.001 + 0.001*0.001;

        var check = function(lat, lng) {
            $.each(list, function(i, v) {
                if((v.value[0]-lng)*(v.value[0]-lng)+(v.value[1]-lat)*(v.value[1]-lat) < min_distance) return false;
            });
            return true;
        };

        $.each(res.results, function(i, v) {
            var lat = v.location.coordinates[0];
            var lng = v.location.coordinates[1];
            list.push({"name": v.name, "value": [lng, lat]});
        });                
        console.log(list);

        $("#chart").height($("body").height());
        
        $.get('static/seed/json/shanghai.json', function (chinaJson) {

            echarts.registerMap('shanghai', chinaJson);
            var myChart = echarts.init(document.getElementById('chart'));

            var option = {
                backgroundColor: '#404a59',
                tooltip: {
                    trigger: 'item'
                },
                geo: {
                    map: 'shanghai',
                    label: {
                        emphasis: {
                            show: false
                        }
                    },
                    roam: true,
                    itemStyle: {
                        normal: {
                            areaColor: '#323c48',
                            borderColor: '#111'
                        },
                        emphasis: {
                            areaColor: '#2a333d'
                        }
                    }
                },
                series: [
                    {
                        name: '',
                        type: 'effectScatter',
                        showEffectOn: 'render',
                        rippleEffect: {
                            brushType: 'stroke'
                        },
                        hoverAnimation: true,
                        coordinateSystem: 'geo',
                        data: list,
                        symbolSize: function (val) {
                            return 10;
                        },
                        label: {
                            normal: {
                                formatter: '{b}',
                                position: 'right',
                                show: true
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#ddb926',
                                shadowBlur: 10,
                                shadowColor: '#333'
                            }
                        }
                    },
                ]
            };
            myChart.setOption(option);
        });

    });

});
