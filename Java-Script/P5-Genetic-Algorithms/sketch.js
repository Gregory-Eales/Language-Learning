// physics variables

var scaler;
var pop;
var energy;

function setup() {
    
    // graphics setup
    console.log("Set up Canvas")
    createCanvas(windowWidth, windowWidth*2/3);
    scaler = windowWidth;
    
    // generate population
    
    pop = new Population(10);
    energy = new Energy(30);
    

}

function draw() {
    // draw background
    createCanvas(windowWidth, windowWidth*2/3)
    scaler = windowWidth;
    background(0);
    
    // update organism states
    
    // update organism movement
    pop.update_positions();
    
    // generate food
    
    // draw organisms
    pop.draw_population();
    energy.draw_energy();
    // draw food
   
}


class Organism {
    
    constructor(clr, size, location){
        // genetics or attributes
        this.clr = clr;
        this.x = location[0];
        this.y = location[1];
        this.size = size;
        this.weights = 1;
        this.energy = 1;
    }
    
    // methods
    
    draw(){
        console.log("Made it to draw");
        fill(this.clr[0], this.clr[1], this.clr[2]);
        rect(this.x, this.y, this.size, this.size);
    }
    
    greedy_move(){
        
        var bit_to_move = 0;
        var smallest_delta = 10*scaler;
        var dy;
        var dx;
        
        for (var i = 0; i < energy.bits.length; i++){
            dy = energy.bits[i].y - this.y;
            dx = energy.bits[i].x - this.x;
            if (dy + dx < smallest_delta){
                smallest_delta = dy + dx;
                bit_to_move = i;
            }
        }
        
        dx = (energy.bits[bit_to_move].x - this.x)
        dy = (energy.bits[bit_to_move].y - this.y)
        
        this.x = this.x + dx/Math.abs(dx)
        this.y = this.y + dy/Math.abs(dy)
    }
}

function GenerateRandomOrganism(){
    
    // genetics or attributes
    
    clr = [random(1, 200), random(1, 200), random(1, 200)];
    loc = [random(1, scaler), random(1, scaler*2/3)];
    size = random(scaler/60, scaler/40);
    
    return new Organism(clr, size, loc);
    
}

function GenerateRandomEnergy(){
    
    // genetics or attributes
    
    clr = [random(1, 255), random(1, 255), random(1, 255)];
    loc = [random(1, scaler), random(1, scaler*2/3)];
    size = random(scaler/220, scaler/210);
    clr = [255, 255, 255]
    return new EnergyBit(loc, size, clr);
    
}

function generate_offspring(Organsim1, Organism2){
    
    // generate new offspring
}


class Population {
    
    
    constructor(pop_size){
        console.log("Started pop generation");
        this.pop = new Array();
        for (var i = 0; i < pop_size; i++){
            this.pop.push(GenerateRandomOrganism())
        }
        console.log("finished pop gen");
    }
    
    draw_population(){
        for (var i = 0; i < this.pop.length; i++){
            this.pop[i].draw()
        }
    }
    
    update_positions(){
        for (var i = 0; i < this.pop.length; i++){
            this.pop[i].greedy_move()
        }
    }
}


class Energy{
    
    constructor(energy_size){
        console.log("Started energy generation");
        this.bits = new Array();
        for (var i = 0; i < energy_size; i++){
            this.bits.push(GenerateRandomEnergy())
        }
        console.log("finished energy gen");
    }
    
    draw_energy(){
        for (var i = 0; i < this.bits.length; i++){
            this.bits[i].draw()
        }
    }
}

class EnergyBit{
    
    constructor(pos, mass, color){
        this.x = pos[0];
        this.y = pos[1];
        this.mass = mass;
        this.color = color;
    }
    
    draw(){
        fill(this.color[0], this.color[1], this.color[2]);
        circle(this.x, this.y, this.mass)
    }
}
