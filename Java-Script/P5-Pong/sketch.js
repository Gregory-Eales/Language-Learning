var ballx = 50;
var bally = 200;
var changeX = -5;
var changeY = 0;
var paddleX = 20;
var paddleY = 0;

function setup() {
  createCanvas(800, 600); 
}

function draw() {
    background(0);
    if (ballx > 780 || ballx < 10 ){
        changeX = -changeX;
        changeY = -changeY;
    }
    if (ballx < paddleX+20 && ballx > paddleX){
        if (bally < paddleY+80 && bally > paddleY){
            changeX = -changeX;
            changeY = -changeY;
        }
    }
  ballx = ballx - changeX;
  bally = bally - changeY;
  draw_ball(ballx, bally);
  get_key();
  draw_paddle();
}

function draw_ball(ballx, bally){
  rect(ballx, bally, 20, 10);
}

function draw_paddle(){
  rect(paddleX, paddleY, 20, 80);
}

function get_key(){
  if (keyCode == DOWN_ARROW){
    paddleY += 10;
  }
  
  if (keyCode == UP_ARROW){
    paddleY -= 10;
  }
  
  if (keyCode == LEFT_ARROW){
    paddleX -= 10;
  }
  
  if (keyCode == RIGHT_ARROW){
    paddleX += 10;
  }
    
    
  keyCode = 0;
}

function check_paddle_collision(){
    
    
}


