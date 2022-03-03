// アドレスバーの高さを除いたサイズを取得
$(function () {
    var winHeight = screen.height;
    var headerHeight = $('header').outerHeight();
    $('.fullscreen').height(winHeight-headerHeight);
});
$(window).resize(function () {
    var winHeight = screen.height;
    var headerHeight = $('header').outerHeight();
    $('.fullscreen').height(winHeight-headerHeight);
});

// スクロール
$(window).on('load resize', function() {
  //ウィンドウの高さを取得する
  var targetY = screen.height;
  //スクロールをクリックするとウィンドウの高さ分、下にスクロールする
  $('.ruleInduct__arrow').on('click', function() {
    $("html, body").stop().animate({
      scrollTop: targetY
    }, 500, 'swing');
    return false;
  });
});

// 記号の入力
function inputSymbol(word) {
  var txt = document.getElementsByName("word")

  var sentence = txt[0].value;
  var len = sentence.length;
  var pos = txt[0].selectionStart;

  var before = sentence.substr(0, pos);
  var after = sentence.substr(pos, len);

  sentence = before + word + after;

  txt[0].value = sentence;
}
