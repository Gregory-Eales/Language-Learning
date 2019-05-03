var back_img;
var char_x = 5;
var char_y = 300;

function setup() {
    createCanvas(600, 600);
    
    //back_img = loadImage('assets⁩/back.png');
}

function draw() {
    // draw background
    background(0);
    draw_character(char_x, char_y);
    
    
    x = x + x_speed;
    
    if (x > 580){
        x_speed = -x_speed;
    }
    
    if (x < 3){
        x_speed = -x_speed;
    }
    
}


function draw_character(x, y) {
    rect(x, y, 10, 10);
    
}


function get_key(){
  if (keyCode == DOWN_ARROW){
    paddleY += 20;
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