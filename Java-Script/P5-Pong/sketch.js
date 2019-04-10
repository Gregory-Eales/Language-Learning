var ballx = 50;
var bally = 200;
var changeX = -11;
var changeY = -1;
var paddleX = 20;
var paddleY = 0;
var score = 0;

function setup() {
  createCanvas(800, 600); 
}

function draw() {
    background(0);
    fill(255);
    textSize(50);
    text("Score: ", 10, 10, 100, 100);
    text(score, 160, 53);
    if (ballx > 780 || ballx < 10 ){
        changeX = -changeX;
    
    }
    
    if (bally > 550 || bally < 10 ){
        changeY = -changeY;
    }
    
    if (ballx < paddleX+20 && ballx > paddleX){
        if (bally < paddleY+80 && bally > paddleY){
            changeX = -changeX;
            changeY = -changeY;
            score = score + 1;
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
    
    
  keyCode = 0;
}

function check_paddle_collision(){
    
    
}


