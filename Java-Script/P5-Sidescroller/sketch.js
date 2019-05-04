// physics variables

var scale;
var char_x;
var char_y;
var char_vx;
var char_vy;
var char_ax;
var char_ay;
var ground_level;

function setup() {
    
    createCanvas(windowWidth, windowWidth*2/3);
    scale = windowWidth;
    char_x = 10;
    char_y = 10;
    char_vx = 0;
    char_vy = 0;
    char_ay = scale/3000;
    char_ax = 0;
    
    
    //back_img = loadImage('assets⁩/back.png');
}

function draw() {
    // draw background
    createCanvas(windowWidth, windowWidth*2/3)
    scale = windowWidth;
    background(0);
    update_physics();
    get_key();
    draw_character(char_x, char_y);
    draw_ground();
}


function draw_ground(){
    fill(100, 100, 100);
    rect(0, scale/2, scale, scale/6);
}


function draw_character(x, y) {
    fill(255, 255, 255);
    rect(char_x, char_y, scale/60, scale/60);   
}


function update_physics(){
    
    char_ay = scale/3000;
    
    
    // update location
    char_x = char_x + char_vx;
    char_y = char_y + char_vy;
    
    // update velocity
    char_vx = char_vx + char_ax;
    char_vy = char_vy + char_ay;
    
    if (char_y > scale/2 - scale/60){
        char_y = scale/2 - scale/60;
    }
    
    if (char_x > scale){
        char_x = 0;
    }
    
    if (char_x < 0){
        char_x = scale;
    }
    
}


function get_key(){

  if (keyCode == DOWN_ARROW){
      
  }
  
  if ((keyIsDown(UP_ARROW)) && (char_y >= scale*2/4 - scale/50)){
    char_vy =  -scale/120;
    keyCode = 0;
  }
  
  if (keyIsDown(LEFT_ARROW)){
    char_x -= scale/300;
    keyCode = 0;
  }
  
  if (keyIsDown(RIGHT_ARROW)){
    char_x += scale/300;
    keyCode = 0;
  }
    
    
}