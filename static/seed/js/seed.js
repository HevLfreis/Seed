/**
 * Created by hevlhayt@foxmail.com
 * Date: 2017/3/13
 * Time: 16:48
 */
$(function () {


    function memo() {
        console.log('bingo');

        sound.pause();

        $('#header').find('h1').text('5-3=2 & 8=3+5');

        $('#header').removeClass('normal').addClass('another');
        if (!mobileAndTabletcheck()) {
            $('#header.another').css('background-position', 'top left, -'+($('#header').width()-40).toString()+'px');
        }

        $.get('memo', function(res){
            $('#main').find('section').first().html(res);
            $('.memo').each(function(i, d) {
                setTimeout(function() {
                    $(d).css('visibility', 'visible').hide().fadeIn();
                }, 1800*(i))

            });
            var soundA = new Howl({
                src: ['static/files/A.mp3'],
                volume: 0.2,
                preload: true
            });
            soundA.play();
        });
    }

    if (mobileAndTabletcheck()) {
        var smobile = 0;

        var hammertime = new Hammer(document.body);
        hammertime.on('swipe', function(ev) {
            smobile ++;
            if (smobile > 2) memo();
        });
    }

    var special= '';
    $(document).keydown(function (event) {
        //console.log(event.keyCode);
        special += event.keyCode.toString();
        if (special === '575150565153') {
            memo();
        }
        else if (special.length > 12) { special = ''; }
    });


    var sound = new Howl({
        src: ['static/files/Vita.mp3'],
        volume: 0.2
    });

    var playText = $('#music').text();
    $('#music').click(function () {
        if (!sound.playing()) {
            sound.play();
            $(this).text(playText + ' PLAYING...');
        }
        else {
            sound.pause();
            $(this).text(playText + ' PAUSE...');
        }
    });

});

