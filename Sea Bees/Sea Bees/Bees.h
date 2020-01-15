#pragma once
class Bees
{
public:
	int currentAction;
	int type;

	//Limitations
	float timeInterval; //default 1s

	//Positional Variables
	double position[3]; //0 = X, Position on East/West, 1 = Y, Position on North/South, 2 = Z, Altitude

	Bees(double X, double Y, double Z, float interval);
	Bees();
	void doActions();
	virtual ~Bees();
};

