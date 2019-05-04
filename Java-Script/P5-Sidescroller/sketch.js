// physics variables

var char_x = 5;
var char_y = 100;
var char_vx = 0;
var char_vy = 0;
var char_ax = 0;
var char_ay = 0;

var ground_level = 310

function setup() {
    createCanvas(600, 400);
    
    //back_img = loadImage('assets⁩/back.png');
}

function draw() {
    // draw background
    background(0);
    draw_character(char_x, char_y);
    draw_ground();
    
}


function draw_ground(){
    fill(100, 100, 100);
    rect(0, 300, 600, 100);
}


function draw_character(x, y) {
    fill(255, 255, 255)
    rect(x, y, 10, 10);   
}


function get_key(){
  if (keyCode == DOWN_ARROW){
      1+1;
  }
  
  if (keyCode == UP_ARROW){
    paddleY -= 20;
  }
  
  if (keyCode == LEFT_ARROW){
    //paddleX -= 10;
  }
  
  if (keyCode == RIGHT_ARROW){
    //paddleX += 10;
  }
}