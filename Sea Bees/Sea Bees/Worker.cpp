#include "stdafx.h"
#include "Worker.h"


Worker::Worker()
{
	//Limits
	maxAltitude = 10; //meters
	carryingCapacity = 1; //gram
	maxSpeed = 2; //m/s

	//Directional Variables
	int orientation = 0; //left right direction in degrees relative to North: 0 = North, 90 = east, 180 = south, 270 = west
	int pitch = 0; //up down direction in degrees relative to the horizon: 0 = neutral, 90 max, -90 min

	//Movement Variables
	float velocity = 0; // m/s
	float acceleration = 0; // m/s^2

	//Inventory
	float load = 0;

	//Destination
	double destination[3] = { 0, 0, -1 };
}

void Worker::turnLeft()
{
	orientation = (orientation - 1) % 360;
}

void  Worker::turnRight()
{
	orientation = (orientation + 1) % 360;
}

void  Worker::ascend()
{
	if (pitch < 90)
	{
		pitch++;
	}
}

void  Worker::descend()
{
	if (pitch > 0)
	{
		pitch--;
	}
}

void Worker::changeOrientation(int newOrientation, int newPitch)
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

void Worker::move()
{
	position[0] = position[0] + cos(radians(orientation)) * velocity * timeInterval + cos(radians(orientation)) * acceleration * pow(timeInterval, 2);
	position[1] = position[1] + sin(radians(orientation)) * velocity * timeInterval + sin(radians(orientation)) * acceleration * pow(timeInterval, 2);
	position[2] = position[2] + sin(radians(pitch)) * velocity * timeInterval + sin(radians(pitch)) * acceleration * pow(timeInterval, 2);

}

void Worker::look()
{

}

float Worker::radians(int degrees)
{
	return (degrees * PI) / 180;
}

void Worker::setDestination(double X, double Y, double Z)
{
	destination[0] = X;
	destination[1] = Y;
	destination[2] = Z;
}


void Worker::action_Movement()
{
	float dist = distance();

}

float Worker::distance()
{
	return sqrt(pow(destination[0] - position[0], 2) + pow(destination[1] - position[1], 2) + pow(destination[2] - position[2], 2));
}

int Worker::changeOrientation()
{
	float dist = distance();


	/*
	Step 1. Get Orientation

	*/
}

int Worker::changePitch()
{

}

Worker::~Worker()
{
}
