let start_flag = false;
let intervalid;
let to_timeup = 10;
let backstart = to_timeup;


function count_down() {
  let timer = document.getElementById("timer");
  if (to_timeup === 0) {
    $('#timer').html('Time up!');
    $('#timer').addClass('red');
    count_stop();
  } else {
    to_timeup--;
    padding();
  }
}

function padding() {
  let min = 0;
  let sec = 0;
  let timer = document.getElementById("timer");
  min = Math.floor(to_timeup / 60);
  sec = (to_timeup % 60);
  min = ('0' + min).slice(-2);
  sec = ('0' + sec).slice(-2);
  timer.innerHTML = min + ':' + sec;
}

window.onload = function (){
  let list1 = ['red', 'blue', 'yellow', 'black', 'white', 'skyblue'];
  let list2 = ['rion', 'tiger', 'horse', 'mouse', 'dog', 'cat'];

  let key = 0;
  let max_len = list1.length - 1;
  let randStart;
  let speed = 20;

  $(".stop").hide();
  $('.start').show();

  padding();


  let randShuffle = function() {
    if (key > max_len) key = 0;
    $('.rand_name1').text(list1[key]);
    $('.rand_name2').text(list2[key]);
    key++;
  }


  $('.stop').click(function() {
    let random_1 = Math.floor(Math.random() * (max_len + 1));
    let random_2 = Math.floor(Math.random() * (max_len + 1));

    $('.rand_name1').text(list1[random_1]);
    $('.rand_name2').text(list1[random_2]);

    clearInterval(randStart);
    $(this).hide();
    $('.start').show();
  });

  $('.start').click(function() {
    $(this).hide();
    $('.stop').show();
    randStart = setInterval(randShuffle, speed);
  });

  $(".startbutton").click(function(event){
    if (start_flag == false) {
      intervalid = setInterval(count_down, 1000);
      start_flag = true;
      $(this).hide();
      $('.stopbutton').show();
    }
  });

  $(".stopbutton").click(function(evnet){
    clearInterval(intervalid);
    start_flag = false;
    $(this).hide(); //止めるボタンの非表示
    $('.startbutton').show(); //STARTボタンの表示
  });

  $("#resetbutton").click(function(event){
    let timer = document.getElementById("timer");
    to_timeup = backstart;
    padding();
    // timer.style.color="black";
    $('#timer').css('color', 'black');
    clearInterval(intervalid);
    start_flag = false;

    $('.startbutton').show(); //STARTボタンの表示
    $('.stopbutton').hide();
  });

  $(".select_timer li").click(function(event) {
    console.log($($(this).children('input')[0]).val());
    to_timeup = parseInt($($(this).children('input')[0]).val()) * 60;
    backstart = to_timeup;

    let timer = document.getElementById("timer");
    min = Math.floor(to_timeup / 60);
    sec = (to_timeup % 60);
    min = ('0' + min).slice(-2);
    sec = ('0' + sec).slice(-2);
    timer.innerHTML = min + ':' + sec;
  });
}
