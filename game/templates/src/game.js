let cur_money = 0;
let playerInfo = document.getElementById("playerInfo");
let invest0_img = document.getElementById("invest0Img");
let invest0 = document.getElementById("invest0Bar");
let invest0_status = 1;  // 0: not usable, 1: usable, but not activated, 2: activated
let invest0_progess = 0;
let invest0_speed = 10;

var MyGame = function () {
    var lastTick = 0;
};
var update_invest_time_bar = function(){

    if (invest0_status === 2) {
        if (invest0_progess !== 100) {
            invest0_progess += invest0_speed;
        }
        else{
            invest0_progess = 0;
            invest0_status = 1;
            cur_money += 100
        }
    }
};
var start_investment = function(){
    console.log('in start investment function');
    invest0_status = 2;
};

invest0_img.onclick = function(){start_investment()};
function update(tick){
    console.log('in update, tick: ' + tick);
    update_invest_time_bar();
}
function render(tick){
    invest0.style.width = invest0_progess+"%";
    console.log('invest0_progess'+invest0_progess);
    playerInfo.textContent = "Money: " + cur_money;
};