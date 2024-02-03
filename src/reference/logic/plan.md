# Logic Plan

 - Timer:
  - Need time library

 - Meter:
  - Gets a boost whenever the player makes a mistake

 - Power:
  - If this runs down to 0%, it's game over! Wait a few seconds while the Meter speeds up.

 - Classes:
  - Game Class:
	- Handles everything like timer
 
  - Robot Class:
  	- Contains the Meter, equates to the robot girlfriend

  - Helper Class:
  	- Used for characters which help the player out
	  - Cajun, Dad, Stoner, Drill Seargant

 - Binary Coded Decimal for a code to lower the Robot's Meter when it gets red (last resort)

 - Hardware Class:
	- Interacts with hardware and generates sequences

- Easter Egg

- Main Loop Order:
  1) Read hardware
  2) Do what robot needs to do
  3) Do what helper needs to do
  4) Update GUI
  5) Increase timer
  6) Repeat