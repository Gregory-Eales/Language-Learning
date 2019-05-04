// physics variables

var char_x = 5;
var char_y = 100;
var char_vx = 0;
var char_vy = 0;
var char_ax = 0;
var char_ay = 0.3;

var ground_level = 310

function setup() {
    createCanvas(600, 400);
    
    //back_img = loadImage('assets⁩/back.png');
}

function draw() {
    // draw background
    background(0);
    update_physics()
    get_key()
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


function update_physics(){
    
    // update location
    char_x = char_x + char_vx;
    char_y = char_y + char_vy;
    
    // update velocity
    char_vx = char_vx + char_ax;
    char_vy = char_vy + char_ay;
    
    if (char_y > 290){
        char_y = 290;
    }
    
    if (char_x > 600){
        char_x=0;
    }
    
    if (char_x < 0){
        char_x = 600;
    }
    
}


function get_key(){

  if (keyCode == DOWN_ARROW){
      
  }
  
  if ((keyIsDown(UP_ARROW)) && (char_y >= 290)){
    char_vy = - 5;
    keyCode = 0;
  }
  
  if (keyIsDown(LEFT_ARROW)){
    char_x -= 2;
    keyCode = 0;
  }
  
  if (keyIsDown(RIGHT_ARROW)){
    char_x += 2;
    keyCode = 0;
  }
    
    
}