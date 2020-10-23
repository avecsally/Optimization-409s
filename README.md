# Optimization-409s
### Game Schedule for U.S. National Football League
Fall 2020 Optimization

Jianing Zhang, Junyi Qian, Yue Zheng, Ziqiao Yan

NFL is the professional American football league consisting of 32 teams, divided equally between the National Football Conference (NFC) and the American Football Conference (AFC). Each conference is further divided into four division of four clubs and every NFL team is based in the contiguous United States. Since the analysis including all the teams right-away was estimated to be computationally intensive, Liang was asked to develop a preliminary analysis for a subset of teams, namely for teams in the East, North, and South divisions. This setup was agreed by the NFL schedulers to approximate the overall problem sufficiently well to come up with recommendations. Figure 1 shows all the 24 teams that are included in the analysis.

The scheduling of games for the selected subset of teams is constrained by the following four main rules:

1. The season was limited to 12 weeks.
2. Each team would play once per week.
3. All 12 games that a team played would need to be against a different opponent.
4. Each team would play at most six home games (i.e., on their home stadium).


Whereas the overall goal was to reduce the total distance that the teams travelled, there were also other considerations, such as the fairness of the game schedule for all teams and the fairness of the game schedule for broad casting companies. With these thoughts in mind, Liang embarked on the analysis of the NFL game scheduling.

Assignment
In this workshop, you will build an integer programming model and use the results of the optimization to support your recommendations. Make a report of about 3 pages (excluding figures, graphs and appendices) summarizing your results, your interpretation of the results and your conclusions and recommendations. You can include graphs and outputs in an appendix, but make sure to summarize and interpret the results in your report as well.



### The Plain Vanilla Schedule

To start, develop a schedule that minimizes the total travel distance of all teams. The distances between the home stadiums of each team are shown in miles in the file “distance.cvs”. When calculating the distances that teams travel, you can assume that after each game the team that played away will travel back to their home stadium before the next game. Include in your model the four main rules.

- What are the decision variables in this problem?
The decision variable should be considered as a binary indication of weather home team $h$ would play against away team $a$ on week $w$. For example, if $x_{h,a,w}$ equals to 1, is means that the home team $h$ would play against with away team $a$ on week $w$. Otherwise, the game does not happen.

- What is the objective function? What are the constraints?
The objective function which minimizes the total travel distance of all teams should be the summed product of all the teams travel distances through out the 12 weeks. If we assume the travel distance from the origin to destination as $d_{h,a}$， the objective function should be defined as

$min\sum_{h,a,w}x_{h,a,w}\cdot 2d_{h,a} $


The constraints for the schedualing, as discussed in the problem statement as follows

The season was limited to 12 weeks.
Each team would play once per week.
All 12 games that a team played would need to be against a different opponent.
Each team would play at most six home games (i.e., on their home stadium).
- Write down the mathematical formulation of the problem.
$min\sum_{h,a,w}x_{h,a,w}\cdot 2d_{h,a} $

subject to

The season was limited to 12 weeks:
$\sum_{h}\sum_{w}[x_{h,a,w}+x_{h,a,w}]=12$
