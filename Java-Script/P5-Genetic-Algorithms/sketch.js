// physics variables

var scale;

function setup() {
    
    // graphics setup
    createCanvas(windowWidth, windowWidth*2/3);
    scale = windowWidth;
    
    var org1 = Organism
    
    // generate population
    

}

function draw() {
    // draw background
    createCanvas(windowWidth, windowWidth*2/3)
    scale = windowWidth;
    background(0);
    
    // update organism states
    
    // update organism movement
    
    // generate food
   
}


class Organism {
    
    constructor(color, size, location, weights, energy){
        // genetics or attributes
        this.color = color;
        this.x = location[0];
        this.y = location[1];
        this.size = size;
        this.weights = weights;
        this.energy = energy;
    }
    
    // Getters
    
    get energy(){
        return this.energy;
    }
    
    get color(){
        return this.color;
    }
    
    get location(){
        return this.location;
    }
    
    get weights(){
        return this.weights;
    }
    
    get size(){
        return size;
    }
    
    // methods
    
    draw(){
        fill(this.color[0], color[1], color[2]);
        rect(this.x, this.y, this.size, this.size);
    }
}

function GenRandomOrganism(){
    
    // genetics or attributes
    
    color = color;
    location = [x, y];
    size = size;
    
    return org;
    
    // methods or actions
    
}





function generate_offspring(Organsim1, Organism2){
    
    // generate new offspring
}



