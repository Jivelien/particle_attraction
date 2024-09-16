# Particles interaction

## Design decision
- 240916 : Particles should not be responsible of the distance computation. 
Positions can still be use for that, but we will need an higher object for business rules, 
as it will allow use to choice between different configurations,
such as closed-bordered computation or torus (left-right and up-down linked) one.