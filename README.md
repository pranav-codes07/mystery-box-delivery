# Mystery Box Delivery System

This is my submission for Nexgensis assignment.

## Assumptions
Since some points were not clear in the document, I assumed the following:

1. For routing, I assumed the agent will deliver to the nearest package first to reduce total distance.
2. If two agents have same distance, I assigned package to agent with smaller ID like A1 first.
3. I used Euclidean distance formula to calculate distance.
4. For best agent, I checked who covered less distance with good delivery.

## How to Run
python main.py
After running, it will create a report.json file.
