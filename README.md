# develop
前回からの改修点
- Design
- JQueryの廃止とVueの導入
- REST API化

## ルーティング
WEB
- item
- roulette
- index

## 何か一言
とりあえず、順番的にはREST化が一番最初にやるべきところで、Vueの導入で最後にDesignかな？ということで、
今月（三月）にリプレイス完了目標でがんばるぞー

## 3/11
とりあえずREST API対応は完了したよ！

そんなわけで、Viewの受け取りの処理を作成していこうと思うで！

## 3/16
DELETEの部分がaxiosを使用してのjsonデータ送信がうまくいかないぞ！

JQueryからのVueの以降中　itemはDELETEが完成すると完成だと思う

## 3/17
DELETEの部分は完成した　 DELETE　PUT POSTでデータの受け取り形式が異なる点は納得がいかないけど

それ以外はまぁ十分にできているかな〜って感じ

[https://teratail.com/questions/296013](参考リンク)
↑axiosではbodyが送れない

## 3/18
Vue版のitemが完成しました！
そんな感じで全体デザインを作ろうかと思ってます！

## 3/19
VueとFlaskの相性がイマイチ感？？？
APIサーバーとしてFlaskを立てるイメージにしてしまって
axiosでそれを呼ぶように変更するべきかな？
Nginxでのルーティング書かないと！！！

## 3/20
追加GET APIの処理を足していく！
vue版のrouletteがパーツが完成した

## 3/24
デザインのプレ版をpush

## 3/25
デザインをpush
ひとまず完成してdevelopをpush しといた！！


