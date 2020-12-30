window.onload = function(){
    let target_left = $(".left").children();
    console.log(target_left);
    let left = [];
    let target_right = $(".right").children();
    let right = [];
    for (let i=2;i<target_left.length-1;i++){
        left.push($(target_left[i]).text());
    }
    for (let i=2;i<target_right.length-1;i++){
        right.push($(target_right[i]).text());
    }
    console.log(left);
    console.log(right);

    let list1=left;
    let list2=right;

    let key=0;
    let max_len=list1.length-1;
    let randStart;
    let speed=20;


    let randShuffle=function(){
        if(key>max_len)key=0;
        $('.rand_name1').text(list1[key]);
        $('.rand_name2').text(list2[key]);
        key++;
    }

    randStart = setInterval(randShuffle, speed);


    //回転を止める（抽選結果1）
    $('.stop').click(function(){
        let random = Math.floor(Math.random() * (max_len + 1)); //ランダムで配列の数を取得
        $('.rand_name1').text(list1[random]); //対象の数値に該当する文字を表示
        clearInterval(randStart); //シャッフルストップ
        $(this).hide(); //止めるボタンの非表示
        $('.start').show(); //再開ボタンの表示
    });

    //回転を止める（抽選結果2）
    $('.stop').click(function(){
        let random = Math.floor(Math.random() * (max_len + 1)); //ランダムで配列の数を取得
        $('.rand_name2').text(list2[random]); //対象の数値に該当する文字を表示
        clearInterval(randStart); //シャッフルストップ
        $(this).hide(); //止めるボタンの非表示
        $('.start').show(); //再開ボタンの表示
    });

    //回転を再開する
    $('.start').click(function(){
        $(this).hide(); //再開ボタンの非表示
        $('.stop').show(); //止めるボタンの表示
        randStart = setInterval(randShuffle, speed); //シャッフル再開
    });

    //↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓以下変更
    $('.rand_name').text("ボタンを押してな！！");
    clearInterval(randStart); //シャッフルストップ
    $(".stop").hide(); //止めるボタンの非表示
    $('.start').show(); //再開ボタンの表示

    // ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑


///////////////////////////////////////////////////////////////////////////////////////////////
    let start_flag = false;
    let intervalid;
    let to_timeup =1200;
    let backstart = to_timeup;


 //console.log(start_flag);

    function count_start() {
      if (start_flag==false) {
          intervalid = setInterval(count_down, 1000);
          start_flag = true;
          $(this).hide(); //STARTボタンの非表示
          $('.stopbutton').show(); //止めるボタンの表示
      }
    }

    function count_down() {
      let timer = document.getElementById("timer");
      if (to_timeup===0) {
          $('#timer').html('Time up!');
          $('#timer').addClass('red');
         count_stop();
      } else {
          to_timeup--;
          padding();
      }
    }

    function count_stop() {
      clearInterval(intervalid);
      start_flag = false;
      $(this).hide(); //止めるボタンの非表示
      $('.startbutton').show(); //STARTボタンの表示
    }

    function count_reset() {
      let timer = document.getElementById("timer");
      to_timeup = backstart;
      padding();
      // timer.style.color="black";
      $('#timer').css('color','black');
      clearInterval(intervalid);
      start_flag = false;
    }

    function padding() {
      let min = 0;
      let sec = 0;
      let timer = document.getElementById("timer");
      min = Math.floor(to_timeup/60);
      sec = (to_timeup%60);
      min = ('0'+min).slice(-2);
      sec = ('0'+sec).slice(-2);
      timer.innerHTML = min+':'+sec;
    }

    $(function () {
      padding();
      $(".startbutton").click(count_start);
      $(".stopbutton").click(count_stop);
      $("#resetbutton").click(count_reset);
    })

};
