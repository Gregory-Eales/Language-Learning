/*

The Game Project

1 - Background Scenery

Use p5 drawing functions such as rect, ellipse, line, triangle and
point to draw the scenery as set out in the code comments. The items
should appear next to the text titles.

Each bit of scenery is worth two marks:

0 marks = not a reasonable attempt
1 mark = attempted but it's messy or lacks detail
2 marks = you've used several shape functions to create the scenery

I've given titles and chosen some base colours, but feel free to
imaginatively modify these and interpret the scenery titles loosely to
match your game theme.


WARNING: Do not get too carried away. If you're shape takes more than 5 lines
of code to draw then you've probably over done it.


*/

function setup()
{
	createCanvas(1024, 576);
}

function draw()
{
	background(100, 155, 255); //fill the sky blue

	noStroke();
	fill(0,155,0);
	rect(0, 432, 1024, 144); //draw some green ground
    
	//1. a cloud in the sky
	//... add your code here
    
	noStroke();
	fill(255);
	ellipse(100, 100, 50, 50);
    ellipse(130, 100, 50, 50);
    ellipse(160, 100, 50, 50);
    ellipse(100, 120, 50, 50);
    ellipse(130, 120, 50, 50);
    ellipse(160, 120, 50, 50);

	//2. a mountain in the distance
	//... add your code here

	noStroke();
    fill(204);
    triangle(420, 432, 580, 432, 500, 150);
    fill(255);
    triangle(480, 220, 520, 221, 500, 150);

	//3. a tree
	//... add your code here

	noStroke();
	fill(255);
	text("tree", 800, 346);
    rect(800, 400, 20, 50);
    fill(50, 50, 50);
    triangle(780, 400, 840, 400, 810, 250);
    triangle(780, 350, 840, 350, 810, 200);

	//4. a canyon
	//NB. the canyon should go from ground-level to the bottom of the screen

	//... add your code here

	noStroke();
	fill(255);
	text("canyon", 100, 480);
    fill(100, 155, 255);
    rect(100, 420, 100, 200);
    
    

	//5. a collectable token - eg. a jewel, fruit, coins
	//... add your code here

	noStroke();
	fill(255);
	text("collectable item", 400, 400);
}
