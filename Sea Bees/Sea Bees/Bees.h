#pragma once
class Bees
{
public:
	//Limitations
	float timeInterval; //default 1s
	double maxAltitude; //meters
	float carryingCapacity; //gram
	float maxSpeed; //m/s

	//Positional Variables
	double posX; //Position on East/West axis
	double posY; //Position on North/South axis
	double posZ; //Altitude

	//Directional Variables
	int orientation; //left right direction in degrees relative to North: 0 = North, 90 = east, 180 = south, 270 = west
	int pitch; //up down direction in degrees relative to the horizon: 0 = neutral, 90 max, -90 min

	//Movement Variables
	float velocity; // m/s
	float acceleration; // m/s^2

	Bees(double X, double Y, double Z, float interval);
	void turnLeft();
	void turnRight();
	void ascend();
	void descend();
	void changeOrientation(int newOrientation, int newPitch);
	void move();
	void look(); //look in a 90 degree wedge left and right, and 90 degree wedge up and down
	float radians(int degrees);
	virtual ~Bees();
};

