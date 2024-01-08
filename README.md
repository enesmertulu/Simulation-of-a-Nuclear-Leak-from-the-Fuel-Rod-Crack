# Simulation-of-a-Nuclear-Leak-from-the-Fuel-Rod-Crack

## INTRODUCTION

In a nuclear reactor, the coolant is used to remove the waste heat from the cycle. In a 
typical PWR, there are three cycles which are primary, secondary, and tertiary cycles. 
The primary cycle is the cycle that mostly interacts with the radioactivity in the reactor 
core.

![image](https://github.com/enesmertulu/Simulation-of-a-Nuclear-Leak-from-the-Fuel-Rod-Crack/assets/95104931/f456832a-3d07-4936-a635-2d92dfed6dcd)

Figure 1 - PWR Nuclear Power Plant’s Schematic Diagram

However, if a crack occurs in the fuel rods, from this crack nuclear materials can leak to the coolant. 
To avoid an environmental disaster, NRC’s limit of 131-I concentration in the water is 4x10^4  Bq/g for PWRs. 

In this study, the PWR’s thermal power is 3411 MW_th with the operation pressure of 15.5 MPa, and the inlet 
and outlet temperatures of 286℃ and 326℃, respectively. In our fuel rods, some cracks occur about 2%. 
From these cracks 131-I leaks to the coolant about 9x10^(-8) per cycle. In addition to these, 0.029 atoms 
of 131-I are produced from each fission.

The coolant stays in the reactor for 𝑡(1) seconds and completes the rest of the cycle in 𝑡(2)
seconds. Every time that the coolant enters the reactor for 𝑡1 seconds, it becomes more 
reactive because of the leaking. So, one of the main purposes is to calculate the 
concentration of 131-I in the water that goes to the environment in the frame of NRC’s 
limitations.

![image](https://github.com/enesmertulu/Simulation-of-a-Nuclear-Leak-from-the-Fuel-Rod-Crack/assets/95104931/b443617a-3f05-4261-85bd-0bd4a1ec782f)

Figure 2 – The Cycle Diagram with Times

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Apache License
Version 2.0, January 2004

Copyright (c) 2024 Enes Mert Ulu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
