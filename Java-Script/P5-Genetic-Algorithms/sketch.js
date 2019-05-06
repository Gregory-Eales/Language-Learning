// physics variables

var scale;
var char_x;
var char_y;
var char_vx;
var char_vy;
var char_ax;
var char_ay;
var ground_level;
var ceiling_x_array;
var ceiling_y_array;
var move_tracker = 0;
var last_length;
var score = 0;
var gif_loadImg = loadImage("assets⁩/⁨PNG⁩/⁨sprites⁩/⁨player⁩/idle/player-idle-1.png⁩");
var gif_createImg = createImg("assets⁩/⁨PNG⁩/⁨sprites⁩/⁨player⁩/idle/player-idle-1.png⁩");


function setup() {
    
    createCanvas(windowWidth, windowWidth*2/3);
    scale = windowWidth;
    char_x = 10;
    char_y = 10;
    char_vx = 0;
    char_vy = 0;
    char_ay = scale/3000;
    char_ax = 0;
    generate_ceiling();
    
    
    
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
    draw_ceiling();
    textSize(50);
    text(frameRate(), 50, 50);
    text("Score:", scale - scale/6, 50);
    text(score, scale - scale/10, 50);
}


function draw_ground(){
    fill(100, 100, 100);
    rect(0, scale/2, scale, scale/6);
}


function draw_character(x, y) {
    fill(255, 255, 255);
    rect(char_x, char_y, scale/60, scale/60);
    //image(gif_loadImg, 10, 10, 10, 10);
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
    
    if (char_x < scale/8){
        char_x = scale/8;
        
        
    }
    
    if (char_x > scale*(1-1/8)){
        char_x = scale*(1-1/8);
        move_tracker = move_tracker + 1;
        //update_ceiling_right();
        if (move_tracker > 0.1){
            move_tracker = 0;
            update_ceiling_right();
            score += 1;
        }
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


function generate_ceiling(){
    var ceiling_holder = [];
    var ceiling_holder_y = [];
    var ceiling_x = 0
    var condition = true
    while(condition){
        if (scale - ceiling_x < scale/90){
            ceiling_holder.push(scale - ceiling_x);
            condition = false;
        }
        
        else{
            var length = random(scale/100, scale/90)
            ceiling_holder.push(length)
            ceiling_x += length;
        }
    }
    var counter = 0;
    for(let i=0; i < ceiling_holder.length; i++){
        ceiling_holder_y.push(random(scale/10, scale/5))
        
    }
    ceiling_x_array = ceiling_holder;
    ceiling_y_array = ceiling_holder_y;
    
}


function draw_ceiling(){
    if (last_length != scale){
        generate_ceiling();
        last_length = scale;
        }
    
    var length = 0;
    for(let i=0; i < ceiling_x_array.length; i++){
        fill(100, 100, 100);
        noStroke();
        rect(length, 0, ceiling_x_array[i], ceiling_y_array[i]);
        fill(255, 255, 255);
        rect(length, scale*3/5 - ceiling_y_array[i]/3, 1, 30);
        length += ceiling_x_array[i];
    }
}


function update_ceiling_right(){
    x = ceiling_x_array[0]
    ceiling_x_array.shift()
    ceiling_y_array.shift()
    ceiling_x_array.push(x)
    ceiling_y_array.push(random(scale/10, scale/5))
    
    
}