# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations
**What I built:**
- I created an active environment
- I added to test_decay file new functions which checks that an error is raised and shows us speed comparison
**Speed comparison (loop vs NumPy):**
- loop :2.6978 s
- numpy : 0.0003 s
- speed-up: 9297.04 timesfaster
**Tests:** all passing?: Yes
**Conclusion:**
- (2-3 sentences: what worked, what you learned, any problems)