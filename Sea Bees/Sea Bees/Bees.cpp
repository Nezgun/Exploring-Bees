#include "stdafx.h"
#include "Bees.h"


Bees::Bees(double X, double Y, double Z, float interval)
{
	//Bee Initialization
	currentAction = 0;

	//Limitations
	timeInterval = interval;

	//Positional Variables
	double position [3] = { X, Y, Z };

	//Operations

	//v = v0 + at
	//displacement = v0 * t + 1/2 * a * t^2
	//v^2 = v0^2 + 2 * a * displacement
}

Bees::Bees() {
	//Bee Initialization
	currentAction = 0;
	this->type = type;

	//Limitations
	timeInterval = 1;

	//Positional Variables
	double position[3] = { 0, 0, 0 };
}

void Bees::doActions()
{

}

Bees::~Bees()
{

}

