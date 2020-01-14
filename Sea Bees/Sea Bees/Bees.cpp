#include "stdafx.h"
#include "Bees.h"
#include <cmath>

const double PI = 3.14159265;


Bees::Bees(double X, double Y, double Z, float interval)
{
	//Bee Initialization
	//Limitations
	timeInterval = interval;
	maxAltitude = 10; //meters
	carryingCapacity = 1; //gram
	maxSpeed = 2; //m/s
	//Positional Variables
	posX = X; //Position on East/West axis
	posY = Y; //Position on North/South axis
	posZ = Z; //Altitude

	//Directional Variables
	int orientation; //left right direction in degrees relative to North: 0 = North, 90 = east, 180 = south, 270 = west
	int pitch; //up down direction in degrees relative to the horizon: 0 = neutral, 90 max, -90 min

	//Movement Variables
	float velocity; // m/s
	float acceleration; // m/s^2

	//Operations

	//v = v0 + at
	//displacement = v0 * t + 1/2 * a * t^2
	//v^2 = v0^2 + 2 * a * displacement
}

void Bees::turnLeft()
{
	orientation = (orientation - 1) % 360;
}

void  Bees::turnRight()
{
	orientation = (orientation + 1) % 360;
}

void  Bees::ascend()
{
	if (pitch < 90)
	{
		pitch++;
	}
}

void  Bees::descend()
{
	if (pitch > 0)
	{
		pitch--;
	}
}

void Bees::changeOrientation(int newOrientation, int newPitch)
{
	int leftCheck;
	int rightCheck;

	leftCheck = (newOrientation + orientation) % 360;
	rightCheck = ((newOrientation - newOrientation) + orientation) % 360;

	if (leftCheck > rightCheck)
	{
		while (orientation != newOrientation)
		{
			turnLeft();
		}
	}
	else
	{
		while (orientation != newOrientation)
		{
			turnRight();
		}
	}

	if (newPitch > pitch)
	{
		while (newPitch > pitch)
		{
			ascend();
		}
	}
	else
	{
		while (newPitch < pitch)
		{
			descend();
		}
	}
}

void Bees::move()
{
	posZ = posZ + sin(radians(pitch)) * velocity * timeInterval + sin(radians(pitch)) * acceleration * pow(timeInterval, 2);

}

void Bees::look()
{

}

float Bees::radians(int degrees)
{
	return (degrees * PI) / 180;
}


Bees::~Bees()
{

}

