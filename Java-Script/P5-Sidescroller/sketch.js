var back_img;
var x = 5;
var y = 300;
var x_speed = 2;
var y_speed = 1;

function setup() {
    createCanvas(600, 600);
    
    //back_img = loadImage('assets⁩/back.png');
}

function draw() {
    
    if (1==1) {
        background(0);
        draw_ball(x, y)
    }
    
    x = x + x_speed;
    
    if (x > 580){
        x_speed = -x_speed;
    }
    
    if (x < 3){
        x_speed = -x_speed;
    }
    
}


function draw_ball(x, y) {
    rect(x, y, 10, 10);
    
}