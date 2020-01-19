#pragma once
#include "Bees.h"
#include <cmath>


class Worker :
	public Bees
{
public:
	const double PI = 3.14159265;

	//Limits
	double maxAltitude; //meters
	float carryingCapacity; //gram
	float maxSpeed; //m/s

	//Directional Variables
	int orientation; //left right direction in degrees relative to North: 0 = North, 90 = east, 180 = south, 270 = west
	int pitch; //up down direction in degrees relative to the horizon: 0 = neutral, 90 max, -90 min

	//Movement Variables
	float velocity; // m/s
	float acceleration; // m/s^2

	//Inventory
	float load;

	//Destination
	double destination [3];

	Worker();

	//Movement Functions
	void turnLeft();
	void turnRight();
	void ascend();
	void descend();
	void changeOrientation(int newOrientation, int newPitch);
	void move();
	void setDestination(double X, double Y, double Z);

	//Action Functions
	void action_Movement();

	//Support Functions
	float radians(int degrees);
	float distance();
	void changePitch();
	void changeOrientation();


	void look(); //look in a 90 degree wedge left and right, and 90 degree wedge up and down
	virtual ~Worker();
};

